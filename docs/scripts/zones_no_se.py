"""Bidding zones in Norway and Sweden

This script obtains approximate Norwegian and Swedish electricity market
bidding zones from tmrowco/electricitymap-contrib.
"""

# import libraries
import geopandas as gpd
import pandas as pd

# root url for approximate NO and SE bidding zone polygons from tmrowco
url = 'https://raw.githubusercontent.com/tmrowco/electricitymap-contrib/master/web/third_party_maps/'

# create empty lists to store a list of bidding zones
# and a list of files to obtain from the url
bznList = []
urlList = []
# NO has 5 bidding zones
for num in range(1, 6):
    bznList.append('NO-' + str(num))
    urlList.append('NO-NO' + str(num) + '.json')
# SE has 4 bidding zones
for num in range(1, 5):
    bznList.append('SE-' + str(num))
    urlList.append('SE-SE' + str(num) + '.json')

# create an empty list and dictionary to store geo dataframes
dfList = []
urlDict = {}

# read geojson files for each zone and store them in the list
for zone in urlList:
    urlDict[zone] = gpd.read_file(url + zone)
    dfList.append(urlDict[zone])

# concatenate the geo dataframes
bzn = gpd.GeoDataFrame(pd.concat(dfList, ignore_index=True),
    crs=dfList[0].crs)

# assign bidding zone list to dataframe
bzn['zone'] = bznList

# drop ID column
bzn = bzn.drop(['id'], axis=1)
