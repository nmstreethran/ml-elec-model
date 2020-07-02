"""Weather station and NUTS data for Germany

This script executes dwd_stations.py to obtain German weather station data
from Deutscher Wetterdienst (DWD), Germany's meteorological service
(https://www.dwd.de/EN/climate_environment/cdc/cdc_node.html). This
data is then combined with nomenclature of territorial units for
statistics (NUTS) data at level 3 from Eurostat
(https://ec.europa.eu/eurostat/web/nuts/background).
"""

# import libraries
from shapely.geometry import Point
import geopandas as gpd
from os import makedirs
import errno

# import data from dwd_stations.py
from dwd_stations import stn as dwd

# GeoJSON NUTS data at level 3 with decimal coordinates and multipolygons
url = ('https://ec.europa.eu/eurostat/cache/GISCO/distribution/v2/' +
    'nuts/geojson/NUTS_RG_01M_2016_4326_LEVL_3.geojson')
nuts = gpd.read_file(url)

# filter for Germany (DE)
nuts = nuts.loc[nuts['CNTR_CODE']=='DE']

# reset index
nuts = nuts.reset_index()

# delete redundant columns
nuts = nuts.drop(['index', 'id', 'LEVL_CODE', 'FID', 'CNTR_CODE'], axis=1)

# create empty columns for NUTS entries
# use gpd.Series to assign geometry dtype
dwd['point'] = gpd.GeoSeries()
# use 'none' to deal with missing data later
dwd['NUTS_ID'] = 'none'

# reset index
dwd = dwd.reset_index(drop=True)

# iterate over datasets
for idx in range(len(dwd)):
    # coordinates of weather stations
    dwd.loc[idx, 'point'] = Point(
        dwd.loc[idx, 'longitude'], dwd.loc[idx, 'latitude'])
    for inx in range(len(nuts)):
        # if weather station is located within the polygon corresponding
        # to the NUTS entry, copy the NUTS ID
        if nuts.loc[inx, 'geometry'].contains(dwd.loc[idx, 'point']) == True:
            dwd.loc[idx, 'NUTS_ID'] = nuts.loc[inx, 'NUTS_ID']

# merge the rest of the data together
dwd_de = nuts.merge(dwd, on='NUTS_ID', how='right')

# deal with unavailable NUTS data
dwd_de['NUTS_NAME'] = dwd_de['NUTS_NAME'].fillna('none')

# save as CSV
# create directory to store data
try:
    makedirs('data/met/de/')
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print ('\nBE CAREFUL! Directory already exists.')

# save dataframe
dwd_de.to_csv(
    'data/met/de/dwd_stations.csv', index=False, encoding='utf-8')
