"""NUTS data for the focus countries and interconnections

This script obtains nomenclature of territorial units for statistics
(NUTS) data at level 0 from Eurostat for DE, AT, CH, CZ, FI, LT, LU, NL,
and PL, and NUTS data at level 2 for DK.
"""

# import libraries
import pandas as pd
import geopandas as gpd

# import NO and SE zones
from zones_no_se import bzn, bznList

# GeoJSON NUTS data at level 0 with decimal coordinates and multipolygons
url0 = 'https://ec.europa.eu/eurostat/cache/GISCO/distribution/v2/nuts/geojson/NUTS_RG_01M_2016_4326_LEVL_0.geojson'
nuts0 = gpd.read_file(url0)

# filter for the following countries: DE, AT, CH, CZ, FI, LT, LU, NL,
# and PL
nuts0 = nuts0.drop(
    nuts0[~((nuts0.CNTR_CODE=='DE')|(nuts0.CNTR_CODE=='AT')|
    (nuts0.CNTR_CODE=='CH')|(nuts0.CNTR_CODE=='CZ')|
    (nuts0.CNTR_CODE=='FI')|(nuts0.CNTR_CODE=='LT')|
    (nuts0.CNTR_CODE=='LU')|(nuts0.CNTR_CODE=='NL')|
    (nuts0.CNTR_CODE=='PL'))].index)

# GeoJSON NUTS data at level 2 with decimal coordinates and multipolygons
url2 = 'https://ec.europa.eu/eurostat/cache/GISCO/distribution/v2/nuts/geojson/NUTS_RG_01M_2016_4326_LEVL_2.geojson'
nuts2 = gpd.read_file(url2)

# filter for DK
nuts2 = nuts2.drop(nuts2[~((nuts2.CNTR_CODE=='DK'))].index)

# concatenate NUTS dataframes
nuts = gpd.GeoDataFrame(
    pd.concat([nuts0, nuts2], ignore_index=True),
    crs=[nuts0, nuts2][0].crs)

# delete redundant columns
nuts = nuts.drop(['COAST_TYPE', 'MOUNT_TYPE', 'LEVL_CODE', 'FID',
    'CNTR_CODE', 'NUTS_ID', 'NUTS_NAME', 'URBN_TYPE'], axis=1)

# assign bidding zones to a new column
nuts['idx'] = nuts['id']

# manually assign zones for Western DK, Eastern DK, and DE-LU
nutsDK1 = ['DK03', 'DK04', 'DK05']
nutsDK2 = ['DK01', 'DK02']
nutsDELU = ['DE', 'LU']
for nutsID in nutsDK1:
    nuts.loc[nuts['id'] == nutsID, 'idx'] = 'DK-1'
for nutsID in nutsDK2:
    nuts.loc[nuts['id'] == nutsID, 'idx'] = 'DK-2'
for nutsID in nutsDELU:
    nuts.loc[nuts['id'] == nutsID, 'idx'] = 'DE-LU'

# drop ID column
nuts = nuts.drop(['id'], axis=1)

# dissolve to combine polygons of the same bidding zone
nuts = nuts.dissolve(by='idx')

# copy index to zone column
nuts['zone'] = list(nuts.index)

# concatenate NUTS and NO-SE bidding zone dataframes
zones = gpd.GeoDataFrame(
    pd.concat([nuts, bzn], ignore_index=True),
    crs=[nuts, bzn][0].crs)
