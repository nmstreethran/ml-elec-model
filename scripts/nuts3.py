"""NUTS 3 data for DE, DK, NO, and SE

This script obtains nomenclature of territorial units for statistics
(NUTS) data at level 3 from Eurostat for the following countries: DE, DK,
NO, SE.
"""

# import libraries
import pandas as pd
from shapely.geometry import Point
import geopandas as gpd

# GeoJSON NUTS data at level 3 with decimal coordinates and multipolygons
url = 'https://ec.europa.eu/eurostat/cache/GISCO/distribution/v2/nuts/geojson/NUTS_RG_01M_2016_4326_LEVL_3.geojson'
nuts3 = gpd.read_file(url)

# filter for the following countries: BE, DE, DK, NL, NO, SE, UK
nuts3 = nuts3.drop(
    nuts3[~((nuts3.CNTR_CODE=='DE')|(nuts3.CNTR_CODE=='DK')|
    (nuts3.CNTR_CODE=='NO')|(nuts3.CNTR_CODE=='SE'))].index)

# sort values by NUTS_ID
nuts3 = nuts3.sort_values(['NUTS_ID'])

# reset index
nuts3 = nuts3.reset_index(drop=True)
