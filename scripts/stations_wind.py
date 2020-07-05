"""Meteorological stations with hourly wind data in DE

Automatically extracts, processes and saves list of stations with hourly
wind data in DE for a given date range within a particular year. Data
from Deutscher Wetterdienst (DWD), Germany's meteorological service
(https://www.dwd.de/EN/climate_environment/cdc/cdc_node.html).
"""

# import libraries
import pandas as pd
from os import makedirs
import errno
from datetime import datetime

# define start and end dates of data
start = '2018010100'
end = '2018070100'

# current year; translates to YYYY-01-01 00:00:00
yr = pd.to_datetime(datetime.now().year, format='%Y')

# convert times to datetime
start = pd.to_datetime(start, format='%Y%m%d%H')
end = pd.to_datetime(end, format='%Y%m%d%H')

# hourly wind data repository URL
url = (
    'https://opendata.dwd.de/climate_environment/CDC/' +
    'observations_germany/climate/hourly/wind/')

# roughly tanslate column titles into English
cols = ['station_id', 'start_date', 'end_date', 'station_height',
    'latitude', 'longitude', 'station_name', 'state']

# extract the data, skipping first two rows and assigning column names
if start < yr or end < yr:
    # historical data (not current year)
    stations = pd.read_fwf(
        url + 'historical/FF_Stundenwerte_Beschreibung_Stationen.txt',
        encoding='ISO-8859-1', skiprows=2, names=cols,
        parse_dates=['start_date', 'end_date'])
else:
    # recent data (current year)
    stations = pd.read_fwf(
        url + 'recent/FF_Stundenwerte_Beschreibung_Stationen.txt',
        encoding='ISO-8859-1', skiprows=2, names=cols,
        parse_dates=['start_date', 'end_date'])

# filter stations with data between start and end dates
stations = stations.drop(
    stations[(stations.start_date > start)|(stations.end_date < end)].index)

# create directory to store files
dest = 'data/meteorology/wind_hourly/'
try:
    makedirs(dest)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print ('\nBE CAREFUL! Directory ' + dest + ' already exists.')

# save as file
stations.to_csv(dest + 'stations.csv', encoding='utf-8', index=None)
