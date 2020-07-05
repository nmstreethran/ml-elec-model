"""Hourly wind data extraction for Germany

Automatically extracts, processes and saves hourly wind data for
a given date range within a particular year. Data are downloaded and
stored in separate directories created for each state and weather
station in Germany. Data from Deutscher Wetterdienst (DWD), Germany's
meteorological service
(https://www.dwd.de/EN/climate_environment/cdc/cdc_node.html).
"""

# import libraries
import pandas as pd
from os import makedirs
import errno
from requests import get
from zipfile import BadZipFile, ZipFile
from io import BytesIO
from datetime import datetime, timedelta

# define start and end dates of data (within the same year)
start = '2018010100'
end = '2018070100'

# define current year; translates to YYYY-01-01 00:00:00
yr = pd.to_datetime(datetime.now().year, format='%Y')

# convert dates to datetime
start = pd.to_datetime(start, format='%Y%m%d%H')
end = pd.to_datetime(end, format='%Y%m%d%H')

# hourly wind data repository URL
repourl = (
    'https://opendata.dwd.de/climate_environment/CDC/' +
    'observations_germany/climate/hourly/wind/')

# create directory to store files
dest = 'data/meteorology/wind_hourly/'
try:
    makedirs(dest + 'temp/')
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print ('\nBE CAREFUL! Directory ' + dest + 'temp/ already exists.')

# read CSV file with list of stations
stations = pd.read_csv(
    'https://gitlab.com/api/v4/projects/19753809/repository/files/' +
    'meteorology%2Fwind_hourly%2Fstations.csv/raw?ref=master',
    encoding='utf-8', parse_dates=['start_date', 'end_date'])

for idx in range(len(stations)):
    # station ID
    stn = stations.loc[idx, 'station_id']

    # add leading zeros to station ID if less than 5 digits long
    stn_id = str(stn).zfill(5)

    # data download URLs
    # historical data
    if end < yr:
        # convert dates to strings
        sd = stations.loc[idx, 'start_date'].strftime('%Y%m%d')
        ed = stations.loc[idx, 'end_date'].strftime('%Y%m%d')
        # if ed falls within the current year
        # change it to be the last day of the previous year
        if ed >= yr.strftime('%Y%m%d'):
            ed = (yr - timedelta(days=1)).strftime('%Y%m%d')
        # zip file URL
        url = (
            repourl + 'historical/stundenwerte_FF_' + stn_id + '_'
            + sd + '_' + ed + '_hist.zip')
    else:
        # recent data (current year) zip file URL
        url = repourl + 'recent/stundenwerte_FF_' + stn_id + '_akt.zip'

    # download contents of zip file into temporary directory
    try:
        r = get(url)
        z = ZipFile(BytesIO(r.content))
        z.extractall(dest + 'temp/')
    # exception if no zip file exists
    except BadZipFile:
        print ('No data exists for station ' + stn_id)

    # roughly tanslate data column titles to English
    dcols = ['station_id', 'timestamp_end', 'QLoNC', 'mean_wind_speed',
        'mean_wind_direction', 'end_of_record']

    # read weather data for station
    data = pd.read_csv(
        dest + 'temp/produkt_ff_stunde_' + sd + '_' + ed + '_' + stn_id +
        '.txt', sep=';', encoding='ISO-8859-1', header=0, names=dcols)

    # convert timestamp to datetime
    data['timestamp_end'] = pd.to_datetime(
        data['timestamp_end'], format='%Y%m%d%H')

    # filter for date range
    data = data.drop(
        data[(data.timestamp_end < start)|(data.timestamp_end > end)].index)

    # set end timestamps as index
    data.set_index(['timestamp_end'], inplace=True)

    # save as CSV
    data.to_csv(dest + stn_id + '.csv', encoding='utf-8')
