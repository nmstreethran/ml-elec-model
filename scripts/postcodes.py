"""Download postcode data

Extract postcode and geo location data from GeoNames
(https://download.geonames.org/export/zip/) for the following
countries: DE, DK, NO, SE, AT, CH, CZ, FI, LT, LU, NL, PL.
"""

# import libraries
from io import BytesIO
from requests import get
from zipfile import BadZipFile, ZipFile
from os import makedirs, remove
import errno
import pandas as pd

# base URL to extract data
urlBase = 'https://download.geonames.org/export/zip/'

# list of countries
countries = ['DE', 'DK', 'NO', 'SE', 'AT', 'CH', 'CZ', 'FI', 'LT', 'LU',
    'NL', 'PL']

# create directory to store data
dest = 'data/geo/'
try:
    makedirs(dest)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print ('\nBE CAREFUL! Directory ' + dest + ' already exists.')

# columns
cols = ['country_code', 'postal_code', 'place_name', 'admin_name1',
    'admin_code1', 'admin_name2', 'admin_code2', 'admin_name3',
    'admin_code3', 'latitude', 'longitude', 'accuracy']

for country in countries:
    # URL of zip file for each country
    url = urlBase + country + '.zip'

    # download contents of zip file into directory
    try:
        r = get(url)
        z = ZipFile(BytesIO(r.content))
        z.extractall(dest)
    # exception if no zip file exists
    except BadZipFile:
        print ('No data exists for ' + country)

    # delete readme
    remove(dest + 'readme.txt')

    # load data and assign column names
    data = pd.read_csv(
        dest + country + '.txt', sep='\t', header=None, names=cols,
        encoding='ISO-8859-1')

    # save as CSV
    data.to_csv(dest + 'postcodes' + country + '.csv', index=None,
        encoding='ISO-8859-1')
