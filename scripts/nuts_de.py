# %%
"""Weather station and NUTS data for Germany

Weather data from Deutscher Wetterdienst (DWD)
Nomenclature of territorial units for statistics (NUTS) data
at level 3
"""

# %%
# import libraries
import pandas as pd
from shapely.geometry import Point
import geopandas
from os import path, system

# %%
# geojson nuts data at level 3 with decimal coordinates and multipolygons
url = 'https://ec.europa.eu/eurostat/cache/GISCO/distribution/v2/nuts/geojson/NUTS_RG_60M_2016_4326_LEVL_3.geojson'
nuts = geopandas.read_file(url)

# %%
# filter for Germany (DE)
nuts = nuts.loc[nuts['CNTR_CODE']=='DE']

# %%
# reset index
nuts = nuts.reset_index()

# %%
# delete redundant columns
nuts = nuts.drop(['index', 'id', 'LEVL_CODE', 'FID', 'CNTR_CODE'], axis=1)

# %%
# get weather station data
if path.exists('data/dwd_stations.csv') == False:
    system('python scripts/dwd_stations.py')
dwd = pd.read_csv('data/dwd_stations.csv')
# create empty columns for nuts entries
dwd['point'] = ''
dwd['NUTS_ID'] = ''

# %%
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

# %%
# merge the rest of the data together
dwd_de = nuts.merge(dwd, on='NUTS_ID')

# %%
# save as csv
dwd_de.to_csv('data/dwd_stations_geo.csv', index=False)
