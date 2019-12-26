# %%
"""Hourly wind data extraction from Deutscher Wetterdienst

Automatically extracts, processes and saves hourly wind data for
a given date range within a particular year. Data are downloaded and
stored in separate directories created for each state and weather
station in Germany.
"""

# %%
# import libraries
import pandas as pd
import os
import errno
import requests
import glob
import zipfile
import io
from datetime import datetime, timedelta
import configparser

# %%
# import user-defined configurations
config = configparser.ConfigParser()
config.read('config.ini')

# %%
# define start and end dates of data
start = config['start']['year'] + config['start']['month'] + \
    config['start']['day'] + config['start']['hour']
end = config['end']['year'] + config['end']['month'] + \
    config['end']['day'] + config['end']['hour']

# %%
# current year; translates to YYYY-01-01 00:00:00
yr = pd.to_datetime(datetime.now().year, format='%Y')

# %%
# convert times to datetime
start = pd.to_datetime(start, format='%Y%m%d%H')
end = pd.to_datetime(end, format='%Y%m%d%H')

# %% 
# hourly wind data repo url
repourl = ('https://opendata.dwd.de/climate_environment/CDC/'
    'observations_germany/climate/hourly/wind/')

# %% 
# read fixed width formatted text file
# with list of weather stations in DE
# first, extract list of column names (separated by space(s))
if start < yr or end < yr:
    # historical data (not current year)
    cols_stn = pd.read_csv(
        repourl + 'historical/FF_Stundenwerte_Beschreibung_Stationen.txt',
        sep=r'\s+', nrows=1).columns.tolist()
else:
    # recent data (current year)
    cols_stn = pd.read_csv(
        repourl + 'recent/FF_Stundenwerte_Beschreibung_Stationen.txt',
        sep=r'\s+', nrows=1).columns.tolist()

# %%
# then, extract the data,
# skipping first two rows and assigning column names
# encoding used due to presence of accented latin characters (e.g., ü)
if start < yr or end < yr:
    # historical data (not current year)
    df_stn = pd.read_fwf(
        repourl + 'historical/FF_Stundenwerte_Beschreibung_Stationen.txt',
        encoding='ISO-8859-1', skiprows=2, names=cols_stn)
else:
    # recent data (current year)
    df_stn = pd.read_fwf(
        repourl + 'recent/FF_Stundenwerte_Beschreibung_Stationen.txt',
        encoding='ISO-8859-1', skiprows=2, names=cols_stn)

# %%
# tanslate column titles to English
df_stn = df_stn.set_axis([
    'station_id', 'start_date', 'end_date', 'station_height', 'latitude',
    'longitude', 'station_name', 'state'], axis='columns', inplace=False)

# %%
# convert dtypes for start_date and end_date to datetime
df_stn['start_date'] = pd.to_datetime(df_stn['start_date'], format='%Y%m%d')
df_stn['end_date'] = pd.to_datetime(df_stn['end_date'], format='%Y%m%d')

# %%
# filter stations with data between start and end dates
df_stn = df_stn.drop(
    df_stn[(df_stn.start_date > start)|(df_stn.end_date < end)].index)

# %%
# list of states
states = df_stn['state'].unique()
for state in states:
    # create directories to store files
    # for each state if they do not exist
    path = 'data/met/de/wind_hourly/' + state.replace(' ', '')
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
        else:
            print ('\nBE CAREFUL! Directory %s already exists.' % path)
    
    # list of station ids and start + end dates in the state
    df_state = df_stn.loc[df_stn['state']==state]
    station_ids = df_state['station_id'].tolist()
    start_dates = df_state['start_date'].tolist()
    end_dates = df_state['end_date'].tolist()
    # combine station ids with start and end dates
    stations = list(zip(station_ids, start_dates, end_dates))
    
    # download and extract data
    for stn, sd, ed in stations:
        # add leading zeros to station ids if less than 5 digits
        stn = stn.zfill(5)
        # file download directory
        dest = path + '/' + stn
        # historical data (not current year)
        if start < yr or end < yr:
            # convert datetime to string
            sd_str = sd.strftime('%Y%m%d')
            ed_str = ed.strftime('%Y%m%d')
            # if the end date falls within the current year
            if ed_str >= yr.strftime('%Y%m%d'):
                # change end date to be the
                # last day of the previous year
                ed_str = (yr - timedelta(days=1)).strftime('%Y%m%d')
                # zip file url
            url = (repourl + 'historical/stundenwerte_FF_' + stn + '_'
                + sd_str + '_' + ed_str + '_hist.zip')
        else:
            # recent data (current year) zip file url
            url = repourl + 'recent/stundenwerte_FF_' + stn + '_akt.zip'
        
        # download contents of zip file into directory
        try:
            r = requests.get(url)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall(dest)
        # exception if no zip file exists
        except zipfile.BadZipFile:
            print ('No data exists for station ' + stn + ' in ' + state)
        
        # read weather data for station
        for file in glob.glob(dest + '/produkt*.txt'):
            df_station = pd.read_csv(file, sep=';')
            
            # tanslate column titles to English
            df_station = df_station.set_axis([
                'station_id', 'timestamp_end', 'QLoNC', 'mean_wind_speed',
                'mean_wind_direction', 'end_of_record'],
                axis='columns', inplace=False)
            
            # convert to datetime
            df_station['timestamp_end'] = pd.to_datetime(
                df_station['timestamp_end'], format='%Y%m%d%H')
            
            # filter for date range
            df_station = df_station.drop(
                df_station[(df_station.timestamp_end < start)|
                (df_station.timestamp_end > end)].index)
            
            # set end timestamps as index
            df_station.set_index(['timestamp_end'], inplace=True)
            df_station.to_csv(dest + '/wind_hourly_' + stn + '.csv')
