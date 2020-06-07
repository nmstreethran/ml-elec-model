"""NUTS data for BE, DE, DK, NL, NO, SE, UK

This script obtains nomenclature of territorial units for statistics
(NUTS) data at level 3 from Eurostat for the following countries: BE,
DE, DK, NL, NO, SE, UK.
"""

# import libraries
import pandas as pd
from shapely.geometry import Point
import geopandas as gpd

# GeoJSON NUTS data at level 3 with decimal coordinates and multipolygons
url = 'https://ec.europa.eu/eurostat/cache/GISCO/distribution/v2/nuts/geojson/NUTS_RG_01M_2016_4326_LEVL_3.geojson'
nuts = gpd.read_file(url)

# filter for the following countries: BE, DE, DK, NL, NO, SE, UK
nuts = nuts.drop(
    nuts[~((nuts.CNTR_CODE=='BE')|(nuts.CNTR_CODE=='DE')|
    (nuts.CNTR_CODE=='DK')|(nuts.CNTR_CODE=='NL')|
    (nuts.CNTR_CODE=='NO')|(nuts.CNTR_CODE=='SE')|
    (nuts.CNTR_CODE=='UK'))].index)

# sort values by NUTS_ID
nuts = nuts.sort_values(['NUTS_ID'])

# filter for NUTS 3
nuts3 = nuts.loc[nuts['LEVL_CODE']==3].copy()
nuts3 = nuts3.reset_index(drop=True)
