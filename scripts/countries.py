"""National boundaries for DE and its interconnections

This script obtains national boundaries based on nomenclature of
territorial units for statistics (NUTS) data at level 0 from Eurostat
(https://ec.europa.eu/eurostat/web/nuts/background) for the following
countries: DE, DK, SE, AT, CH, CZ, LU, NL, PL. Overseas territories of FR
are excluded, so NUTS 1 is used for FR instead.
"""

# import libraries
import geopandas as gpd
from os import makedirs
import errno
import pandas as pd

# GeoJSON NUTS data at level 1 with decimal coordinates and multipolygons
url1 = (
    'https://ec.europa.eu/eurostat/cache/GISCO/distribution/v2/' +
    'nuts/geojson/NUTS_RG_01M_2016_4326_LEVL_1.geojson')
nuts1 = gpd.read_file(url1)

# exclude RUP FR - RÉGIONS ULTRAPÉRIPHÉRIQUES FRANÇAISES' (FRY) /
# French Overseas Territories
nuts1 = nuts1[~nuts1.NUTS_ID.str.contains('FRY')]
nuts1 = nuts1.drop(nuts1[~((nuts1.CNTR_CODE=='FR'))].index)

# clear NUTS data except polygons
nuts1 = nuts1.drop(
    ['id', 'COAST_TYPE', 'MOUNT_TYPE', 'FID',
    'NUTS_ID', 'URBN_TYPE', 'NUTS_NAME'], axis=1)

# dissolve to combine polygons
nuts1 = nuts1.dissolve(by='LEVL_CODE')

# create new column with country name
nuts1['CNTR'] = 'FRANCE'

# clear axis name
nuts1 = nuts1.rename_axis('')

# GeoJSON NUTS data at level 3 with decimal coordinates and multipolygons
url0 = (
    'https://ec.europa.eu/eurostat/cache/GISCO/distribution/v2/' +
    'nuts/geojson/NUTS_RG_01M_2016_4326_LEVL_0.geojson')
nuts0 = gpd.read_file(url0)

# filter for DE and interconnections (except FR)
nuts0 = nuts0.drop(nuts0[~(
    (nuts0.CNTR_CODE=='AT')|(nuts0.CNTR_CODE=='CH')|
    (nuts0.CNTR_CODE=='CZ')|(nuts0.CNTR_CODE=='DE')|
    (nuts0.CNTR_CODE=='DK')|(nuts0.CNTR_CODE=='LU')|
    (nuts0.CNTR_CODE=='NL')|(nuts0.CNTR_CODE=='PL')|
    (nuts0.CNTR_CODE=='SE'))].index)

# clear NUTS data except polygons
nuts0 = nuts0.drop(
    ['id', 'COAST_TYPE', 'MOUNT_TYPE', 'FID',
    'NUTS_ID', 'URBN_TYPE', 'LEVL_CODE'], axis=1)

# rename NUTS_ID column to CNTR
nuts0 = nuts0.rename(columns={'NUTS_NAME': 'CNTR'})

# concatenate nuts0 and nuts1 to form countries dataframe
countries = gpd.GeoDataFrame(
    pd.concat([nuts0, nuts1], ignore_index=True), crs=[nuts0, nuts1][0].crs)

# save as GeoJSON
# create directory to store data
dest = 'data/geography/polygons/'
try:
    makedirs(dest)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print ('\nBE CAREFUL! Directory ' + dest + ' already exists.')

# save dataframe
countries.to_file(dest + 'countries.geojson', driver='GeoJSON')
