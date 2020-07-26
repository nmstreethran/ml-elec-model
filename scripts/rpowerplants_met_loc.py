# %%
# import libraries
from scipy import spatial
import pandas as pd
import numpy as np

# %%
# load data
tso = pd.read_csv(
    'data/power/installed/TransnetBW.csv', encoding='utf-8')
postcodes = pd.read_csv(
    'data/geography/postcodes/postcodesDE.csv', encoding='utf-8')
wind = pd.read_csv(
    'data/meteorology/wind/stations.csv', encoding='utf-8')

# %%
# take the first postcode value when there are duplicates, drop all others
postcodes = postcodes.drop_duplicates(['postal_code'])

# %%
# filter for solar and wind power plants
tso = tso.drop(tso[~(
    # (tso.energy_carrier=='Solar')|
    (tso.energy_carrier == 'Onshore wind') |
    (tso.energy_carrier == 'Offshore wind'))].index)

# %%
# rename lat and lon columns for met data
wind = wind.rename(columns={'longitude': 'met_lon', 'latitude': 'met_lat'})

# drop columns
wind = wind.drop(['state', 'start_date', 'end_date'], axis=1)

# %%
# merge postcode and TSO data
tso_loc = pd.merge(tso, postcodes, on=['postal_code'], how='left')

# %%
# create list of met station coordinates
lonList = wind['met_lon']
latList = wind['met_lat']
coordList = list(zip(lonList, latList))

# %%
# create nearest neighbour tree with coordinate list
tree = spatial.KDTree(coordList)

# %%
# create new empty columns to store tree data
tso_loc['distance'] = np.nan
tso_loc['met_lon'] = np.nan
tso_loc['met_lat'] = np.nan

# %%
# find nearest met station for each power plant in TSO data
for idx in range(len(tso_loc)):
    stn = tree.query(
        [(tso_loc.loc[idx, 'longitude'], tso_loc.loc[idx, 'latitude'])])
    if stn[1][0] < len(coordList):
        tso_loc.loc[idx, 'distance'] = stn[0][0]
        tso_loc.loc[idx, 'met_lon'] = coordList[stn[1][0]][0]
        tso_loc.loc[idx, 'met_lat'] = coordList[stn[1][0]][1]

# %%
# merge TSO and met data
tso_wind = pd.merge(tso_loc, wind, on=['met_lon', 'met_lat'], how='left')

# %%
# tso_wind.sort_values(by=['distance'])
# for idx in range(len(tso_wind)):
#     if tso_wind.loc[idx, 'distance'] == np.nan:
#         print(tso_wind.iloc[idx, 9])
# 77888	Sasbachwalden
