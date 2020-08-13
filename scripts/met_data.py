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
from datetime import datetime
from glob import glob

# define start and end dates of data (within the same year)
start = '20180101'
end = '20180701'

# define current year; translates to YYYY-01-01 00:00:00
yr = pd.to_datetime(datetime.now().year, format='%Y')

# convert dates to datetime
start = pd.to_datetime(start, format='%Y%m%d')
end = pd.to_datetime(end, format='%Y%m%d')

# list of datasets to download
datasets = [
    ('sun', 'SD'), ('wind', 'FF'), ('cloudiness', 'N'),
    ('precipitation', 'RR'), ('air_temperature', 'TU'),
    ('cloud_type', 'CS'), ('dew_point', 'TD'), ('pressure', 'P0'),
    ('soil_temperature', 'EB'), ('visibility', 'VV'), ('solar', 'ST')]

# read CSV file with list of stations
metStations = pd.read_csv(
    'https://gitlab.com/api/v4/projects/19753809/repository/files/' +
    'meteorology%2Fstations.csv/raw?ref=master',
    encoding='utf-8')

for d, D in datasets:
    # hourly data repository URL
    repourl = (
        'https://opendata.dwd.de/climate_environment/CDC/' +
        'observations_germany/climate/hourly/' + d + '/')

    dest = 'data/meteorology/' + d + '/'
    try:
        makedirs(dest + 'temp/')
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
        else:
            print(
                '\nBE CAREFUL! Directory ' + dest + 'temp/ already exists.')

    # filter meteorological data based on energy carrier
    stations = metStations[metStations['type'].str.contains(d)]

    for idx in range(len(stations)):
        # station ID
        stn = stations.loc[idx, 'station_id']

        # add leading zeros to station ID if less than 5 digits long
        stn_id = str(stn).zfill(5)

        # # convert dates to strings
        # sd = stations.loc[idx, 'start_date'].strftime('%Y%m%d')
        # ed = stations.loc[idx, 'end_date'].strftime('%Y%m%d')

        # get zip file download URLs
        # for solar data
        if d == 'solar':
            url = repourl + 'stundenwerte_' + D + '_' + stn_id + '_row.zip'

        # for historical data (not solar)
        elif end < yr:
            # # if ed falls within the current year
            # # change it to be the last day of the previous year
            # if ed >= yr.strftime('%Y%m%d'):
            #     ed = (yr - timedelta(days=1)).strftime('%Y%m%d')
            for f in glob(
                'historical/stundenwerte_' + D + '_' + stn_id +
                    '_*_hist.zip'):
                url = (repourl + f)

        # for recent data (current year, not solar)
        else:
            url = (
                repourl + 'recent/stundenwerte_' + D + '_' + stn_id +
                '_akt.zip')

        # download contents of zip file into temporary directory
        try:
            r = get(url)
            z = ZipFile(BytesIO(r.content))
            z.extractall(dest + 'temp/')
        # exception if no zip file exists
        except BadZipFile:
            print('No data exists for station ' + stn_id)

        # read weather data for station
        for f in glob(
            'temp/produkt_' + D.lower() + '_stunde_*_' +
                stn_id + '.txt'):
            data = pd.read_csv(
                dest + f, sep=';', encoding='ISO-8859-1')

        # rename timestamp column
        data.rename(columns={data.columns[1]: 'TIMESTAMP'}, inplace=True)

        # convert timestamp to datetime
        data['TIMESTAMP'] = pd.to_datetime(
            data['TIMESTAMP'], format='%Y%m%d%H')

        # filter for date range
        data = data.drop(data[
            (data.TIMESTAMP < start) | (data.TIMESTAMP > end)].index)

        # set end timestamps as index
        data.set_index(['TIMESTAMP'], inplace=True)

        # save as CSV
        data.to_csv(dest + stn_id + '.csv', encoding='utf-8')
