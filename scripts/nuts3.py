"""NUTS 3 data for DE, DK, NO, and SE and their interconnections

This script obtains nomenclature of territorial units for statistics
(NUTS) data at level 3 from Eurostat
(https://ec.europa.eu/eurostat/web/nuts/background) for the following
countries: DE, DK, NO, SE, AT, CH, CZ, FI, LT, LU, NL, PL.
"""

# import libraries
import geopandas as gpd

# GeoJSON NUTS data at level 3 with decimal coordinates and multipolygons
url = 'https://ec.europa.eu/eurostat/cache/GISCO/distribution/v2/nuts/geojson/NUTS_RG_01M_2016_4326_LEVL_3.geojson'
nuts3 = gpd.read_file(url)

# filter for focus countries and interconnections
nuts3 = nuts3.drop(
    nuts3[~((nuts3.CNTR_CODE=='DE')|(nuts3.CNTR_CODE=='DK')|
    (nuts3.CNTR_CODE=='NO')|(nuts3.CNTR_CODE=='SE')|
    (nuts3.CNTR_CODE=='AT')|(nuts3.CNTR_CODE=='CH')|
    (nuts3.CNTR_CODE=='CZ')|(nuts3.CNTR_CODE=='FI')|
    (nuts3.CNTR_CODE=='LT')|(nuts3.CNTR_CODE=='LU')|
    (nuts3.CNTR_CODE=='NL')|(nuts3.CNTR_CODE=='PL'))].index)

# sort values by NUTS_ID
nuts3 = nuts3.sort_values(['NUTS_ID'])

# reset index
nuts3 = nuts3.reset_index(drop=True)

"""save as GeoJSON

# import libraries
import os
import errno

# create directory to store data
try:
    os.makedirs('data/')
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise

# save dataframe
nuts3.to_file('data/nuts3.geojson', driver='GeoJSON')
"""
