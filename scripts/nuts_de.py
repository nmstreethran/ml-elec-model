"""Weather station and NUTS data for Germany

This script executes dwd_stations.py to obtain German weather station data
from Deutscher Wetterdienst (DWD), Germany's meteorological service. This
data is then combined with nomenclature of territorial units for statistics
(NUTS) data at level 3 from Eurostat.
"""

# import libraries
import pandas as pd
from shapely.geometry import Point
import geopandas as gpd

# import data from dwd_stations.py
from dwd_stations import stn as dwd

# geojson nuts data at level 3 with decimal coordinates and multipolygons
url = 'https://ec.europa.eu/eurostat/cache/GISCO/distribution/v2/nuts/geojson/NUTS_RG_60M_2016_4326_LEVL_3.geojson'
nuts = gpd.read_file(url)

# filter for Germany (DE)
nuts = nuts.loc[nuts['CNTR_CODE']=='DE']

# reset index
nuts = nuts.reset_index()

# delete redundant columns
nuts = nuts.drop(['index', 'id', 'LEVL_CODE', 'FID', 'CNTR_CODE'], axis=1)

# create empty columns for nuts entries
# use gpd.Series to assign geometry dtype
dwd['point'] = gpd.GeoSeries()
dwd['NUTS_ID'] = ''

# reset index
dwd = dwd.reset_index(drop=True)

# iterate over datasets
for idx in range(len(dwd)):
    # coordinates of weather stations
    dwd.loc[idx, 'point'] = Point(
        dwd.loc[idx, 'longitude'], dwd.loc[idx, 'latitude'])
    for inx in range(len(nuts)):
        # if weather station is located within the polygon corresponding
        # to the nuts entry, copy the nuts id
        if nuts.loc[inx, 'geometry'].contains(dwd.loc[idx, 'point']) == True:
            dwd.loc[idx, 'NUTS_ID'] = nuts.loc[inx, 'NUTS_ID']

# merge the rest of the data together
dwd_de = nuts.merge(dwd, on='NUTS_ID')

# # save as csv
# dwd_de.to_csv('data/dwd_stations_geo.csv', index=False)
