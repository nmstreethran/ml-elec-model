"""Bidding zones SE, DE, AT, CH, CZ, FR, LU, NL, and PL

This script first obtains approximate SE bidding zones from Tomorrow's
electricityMap (https://github.com/tmrowco/electricitymap-contrib). It
then obtains all other zones from nomenclature of territorial units for
statistics (NUTS) data at level 0 for DE, AT, CH, CZ, LU, NL, and PL,
NUTS data at level 1 for FR, and NUTS data at level 2 for DK from Eurostat
(https://ec.europa.eu/eurostat/web/nuts/background).
"""

# import libraries
import pandas as pd
import geopandas as gpd
from os import makedirs
import errno

# root URL for approximate SE bidding zone polygons from tmrowco
url = (
    'https://raw.githubusercontent.com/tmrowco/' +
    'electricitymap-contrib/master/web/third_party_maps/')

# create empty lists to store a list of bidding zones
# and a list of files to obtain from the URL
bznList = []
urlList = []
# SE has 4 bidding zones
for num in range(1, 5):
    bznList.append('SE-' + str(num))
    urlList.append('SE-SE' + str(num) + '.json')

# create an empty list and dictionary to store geo dataframes
dfList = []
urlDict = {}

# read GeoJSON files for each zone and store them in the list
for zone in urlList:
    urlDict[zone] = gpd.read_file(url + zone)
    dfList.append(urlDict[zone])

# concatenate the geo dataframes
bzn = gpd.GeoDataFrame(
    pd.concat(dfList, ignore_index=True), crs=dfList[0].crs)

# assign bidding zone list to dataframe
bzn['zone'] = bznList

# drop ID column
bzn = bzn.drop(['id'], axis=1)

# GeoJSON NUTS data at level 0 with decimal coordinates and multipolygons
url0 = (
    'https://ec.europa.eu/eurostat/cache/GISCO/distribution/v2/' +
    'nuts/geojson/NUTS_RG_01M_2016_4326_LEVL_0.geojson')
nuts0 = gpd.read_file(url0)

# filter for the following countries: DE, AT, CH, CZ, LU, NL, and PL
nuts0 = nuts0.drop(nuts0[~(
    (nuts0.CNTR_CODE=='AT')|(nuts0.CNTR_CODE=='CH')|
    (nuts0.CNTR_CODE=='CZ')|(nuts0.CNTR_CODE=='DE')|
    (nuts0.CNTR_CODE=='LU')|(nuts0.CNTR_CODE=='NL')|
    (nuts0.CNTR_CODE=='PL'))].index)

# GeoJSON NUTS data at level 1 with decimal coordinates and multipolygons
url1 = (
    'https://ec.europa.eu/eurostat/cache/GISCO/distribution/v2/' +
    'nuts/geojson/NUTS_RG_01M_2016_4326_LEVL_1.geojson')
nuts1 = gpd.read_file(url1)

# exclude RUP FR - RÉGIONS ULTRAPÉRIPHÉRIQUES FRANÇAISES' (FRY) /
# French Overseas Territories
nuts1 = nuts1[~nuts1.NUTS_ID.str.contains('FRY')]
nuts1 = nuts1.drop(nuts1[~((nuts1.CNTR_CODE=='FR'))].index)

# create new dummy column with country name
nuts1['CNTR'] = 'FR'

# reassign ID
nuts1['id'] = 'FR'

# dissolve to combine polygons
nuts1 = nuts1.dissolve(by='CNTR')

# clear axis name
nuts1 = nuts1.rename_axis('')

# GeoJSON NUTS data at level 2 with decimal coordinates and multipolygons
url2 = (
    'https://ec.europa.eu/eurostat/cache/GISCO/distribution/v2/' +
    'nuts/geojson/NUTS_RG_01M_2016_4326_LEVL_2.geojson')
nuts2 = gpd.read_file(url2)

# filter for DK
nuts2 = nuts2.drop(nuts2[~((nuts2.CNTR_CODE=='DK'))].index)

# concatenate NUTS dataframes
nuts = gpd.GeoDataFrame(
    pd.concat([nuts0, nuts1, nuts2], ignore_index=True),
    crs=[nuts0, nuts1, nuts2][0].crs)

# delete redundant columns
nuts = nuts.drop(
    ['COAST_TYPE', 'MOUNT_TYPE', 'LEVL_CODE', 'FID',
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
    pd.concat([nuts, bzn], ignore_index=True), crs=[nuts, bzn][0].crs)

# create directory to store data
dest = 'data/geography/polygons/'
try:
    makedirs(dest)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print ('\nBE CAREFUL! Directory ' + dest + ' already exists.')

# save dataframe as GeoJSON
zones.to_file(dest + 'bidding_zones.geojson', driver='GeoJSON')
