"""NUTS 3 data for DE

This script obtains nomenclature of territorial units for statistics
(NUTS) data at level 3 from Eurostat
(https://ec.europa.eu/eurostat/web/nuts/background) for DE.
"""

# import libraries
import geopandas as gpd
from os import makedirs
import errno

# GeoJSON NUTS data at level 3 with decimal coordinates and multipolygons
url = (
    'https://ec.europa.eu/eurostat/cache/GISCO/distribution/v2/' +
    'nuts/geojson/NUTS_RG_01M_2016_4326_LEVL_3.geojson')
nuts3 = gpd.read_file(url)

# filter for DE
nuts3 = nuts3.drop(nuts3[~((nuts3.CNTR_CODE=='DE'))].index)

# sort values by NUTS_ID
nuts3 = nuts3.sort_values(['NUTS_ID'])

# reset index
nuts3 = nuts3.reset_index(drop=True)

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
nuts3.to_file(dest + 'nuts3_DE.geojson', driver='GeoJSON')
