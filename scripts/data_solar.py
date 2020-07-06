"""Hourly solar data extraction for Germany

Automatically extracts, processes and saves hourly solar data for
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

# define start and end dates of data
start = '20180101'
end = '20180701'

# convert dates to datetime
start = pd.to_datetime(start, format='%Y%m%d')
end = pd.to_datetime(end, format='%Y%m%d')

# hourly solar data repo URL
repourl = (
    'https://opendata.dwd.de/climate_environment/CDC/' +
    'observations_germany/climate/hourly/solar/')

# create directory to store files
dest = 'data/meteorology/solar_hourly/'
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
    'meteorology%2Fsolar_hourly%2Fstations.csv/raw?ref=master',
    encoding='utf-8', parse_dates=['start_date', 'end_date'])

for idx in range(len(stations)):
    # station ID
    stn = stations.loc[idx, 'station_id']

    # convert dates to strings
    sd = stations.loc[idx, 'start_date'].strftime('%Y%m%d')
    ed = stations.loc[idx, 'end_date'].strftime('%Y%m%d')

    # add leading zeros to station ID if less than 5 digits long
    stn_id = str(stn).zfill(5)

    # data download URL
    url = repourl + 'stundenwerte_ST_' + stn_id + '_row.zip'

    # download contents of zip file into temporary directory
    try:
        r = get(url)
        z = ZipFile(BytesIO(r.content))
        z.extractall(dest + 'temp/')
    # exception if no zip file exists
    except BadZipFile:
        print ('No data exists for station ' + stn_id)

    # roughly tanslate data column titles to English
    dcols = ['station_id', 'timestamp_end', 'QLoNC',
        'longwave_downward_radiation', 'diffuse_radiation',
        'incoming_radiation', 'sunshine_duration', 'zenith_angle',
        'end_of_interval', 'end_of_record']

    # read weather data for station
    data = pd.read_csv(
        dest + 'temp/produkt_st_stunde_' + sd + '_' + ed + '_' + stn_id +
        '.txt', sep=';', encoding='ISO-8859-1', header=0, names=dcols)

    # convert timestamp to datetime
    data['timestamp_end'] = pd.to_datetime(
        data['timestamp_end'], format='%Y%m%d%H:%M')

    # filter for date range
    data = data.drop(
        data[(data.timestamp_end < start)|(data.timestamp_end > end)].index)

    # set end timestamps as index
    data.set_index(['timestamp_end'], inplace=True)

    # save as CSV
    data.to_csv(dest + stn_id + '.csv', encoding='utf-8')
