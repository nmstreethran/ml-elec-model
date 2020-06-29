"""NUTS 0 data for DE, DK, NO, and SE and their interconnections

This script obtains nomenclature of territorial units for statistics
(NUTS) data at level 0 from Eurostat
(https://ec.europa.eu/eurostat/web/nuts/background) for the following
countries: DE, DK, NO, SE, AT, CH, CZ, FI, LT, LU, NL, PL.
"""

# import libraries
import geopandas as gpd
import os
import errno

# GeoJSON NUTS data at level 3 with decimal coordinates and multipolygons
url = ('https://ec.europa.eu/eurostat/cache/GISCO/distribution/v2/' +
    'nuts/geojson/NUTS_RG_01M_2016_4326_LEVL_0.geojson')
nuts0 = gpd.read_file(url)

# filter for focus countries and interconnections
nuts0 = nuts0.drop(
    nuts0[~((nuts0.CNTR_CODE=='DE')|(nuts0.CNTR_CODE=='DK')|
    (nuts0.CNTR_CODE=='NO')|(nuts0.CNTR_CODE=='SE')|
    (nuts0.CNTR_CODE=='AT')|(nuts0.CNTR_CODE=='CH')|
    (nuts0.CNTR_CODE=='CZ')|(nuts0.CNTR_CODE=='FI')|
    (nuts0.CNTR_CODE=='LT')|(nuts0.CNTR_CODE=='LU')|
    (nuts0.CNTR_CODE=='NL')|(nuts0.CNTR_CODE=='PL'))].index)

# sort values by NUTS_ID
nuts0 = nuts0.sort_values(['NUTS_ID'])

# reset index
nuts0 = nuts0.reset_index(drop=True)

# save as GeoJSON
# create directory to store data
try:
    os.makedirs('data/geo/')
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print ('\nBE CAREFUL! Directory already exists.')

# save dataframe
nuts0.to_file('data/geo/nuts0.geojson', driver='GeoJSON')
