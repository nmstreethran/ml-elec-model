"""Download postcode data for DE

Extract postcode and geo location data from GeoNames
(https://download.geonames.org/export/zip/) for DE.
"""

# import libraries
from io import BytesIO
from requests import get
from zipfile import BadZipFile, ZipFile
from os import makedirs, remove
import errno
import pandas as pd

# URL to extract data
url = 'https://download.geonames.org/export/zip/DE.zip'

# create directory to store data
dest = 'data/geography/postcodes/'
try:
    makedirs(dest + 'temp/')
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print ('\nBE CAREFUL! Directory ' + dest + 'temp/ already exists.')

# columns
cols = ['country_code', 'postal_code', 'place_name', 'admin_name1',
    'admin_code1', 'admin_name2', 'admin_code2', 'admin_name3',
    'admin_code3', 'latitude', 'longitude', 'accuracy']

# download contents of zip file into directory
try:
    r = get(url)
    z = ZipFile(BytesIO(r.content))
    z.extractall(dest + 'temp/')
# exception if no zip file exists
except BadZipFile:
    print ('No data exists for DE')

# load data and assign column names
data = pd.read_csv(
    dest + 'temp/DE.txt', sep='\t', header=None, names=cols,
    encoding='utf-8')

# save as CSV
data.to_csv(dest + 'postcodesDE.csv', index=None, encoding='utf-8')
