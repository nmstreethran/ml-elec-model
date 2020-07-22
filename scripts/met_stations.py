"""Meteorological stations with hourly data in DE

Automatically extracts, processes and saves list of stations with hourly
data in DE for a given date range within a particular year. Data
from Deutscher Wetterdienst (DWD), Germany's meteorological service
(https://www.dwd.de/EN/climate_environment/cdc/cdc_node.html).
"""

# import libraries
import pandas as pd
from os import makedirs
import errno
from datetime import datetime

# define start and end dates of data
start = '20180101'
end = '20180701'

# current year; translates to YYYY-01-01 00:00:00
yr = pd.to_datetime(datetime.now().year, format='%Y')

# convert times to datetime
start = pd.to_datetime(start, format='%Y%m%d')
end = pd.to_datetime(end, format='%Y%m%d')

# roughly tanslate column titles into English
cols = [
    'station_id', 'start_date', 'end_date', 'station_height',
    'latitude', 'longitude', 'station_name', 'state']

# list of datasets to download
datasets = [
    ('sun', 'SD'), ('wind', 'FF'), ('cloudiness', 'N'),
    ('precipitation', 'RR'), ('air_temperature', 'TU'),
    ('cloud_type', 'CS'), ('dew_point', 'TD'), ('pressure', 'P0'),
    ('soil_temperature', 'EB'), ('visibility', 'VV'), ('solar', 'ST')]

for d, D in datasets:
    # hourly data repository URL
    url = (
        'https://opendata.dwd.de/climate_environment/CDC/' +
        'observations_germany/climate/hourly/' + d + '/')

    # file URL, depending on directory structure
    if d == 'solar':
        furl = url + 'ST_Stundenwerte_Beschreibung_Stationen.txt'
    elif end < yr:
        # historical data (not current year)
        furl = (
            url + 'historical/' + D +
            '_Stundenwerte_Beschreibung_Stationen.txt')
    else:
        # recent data (current year)
        furl = (
            url + 'recent/' + D +
            '_Stundenwerte_Beschreibung_Stationen.txt')

    # extract the data, skipping first two rows and assigning column names
    stations = pd.read_fwf(
        furl, encoding='ISO-8859-1', skiprows=2, names=cols,
        parse_dates=['start_date', 'end_date'])

    # filter stations with data between start and end dates
    stations = stations.drop(stations[
        (stations.start_date > start)|(stations.end_date < end)].index)

    # drop duplicate rows
    stations = stations.drop_duplicates(['station_id'])

    # create directory to store files
    dest = 'data/meteorology/' + d + '/'
    try:
        makedirs(dest)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
        else:
            print ('\nBE CAREFUL! Directory ' + dest + ' already exists.')

    # save as file
    stations.to_csv(dest + 'stations.csv', encoding='utf-8', index=None)
