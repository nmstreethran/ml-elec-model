# %%
# import libraries
from scipy import spatial
import pandas as pd
import numpy as np

# %%
postcodes = pd.read_csv(
    'data/geography/postcodes/postcodesDE.csv', encoding='utf-8',
    usecols=['postal_code', 'latitude', 'longitude'],
    dtype={'postal_code': str})
# take the first postcode value when there are duplicates, drop all others
postcodes = postcodes.drop_duplicates(['postal_code'])

# %%
# load data
tsoList = ['50Hertz_Transmission', 'Amprion', 'TenneT_TSO', 'TransnetBW']
tso = pd.DataFrame()
for t in tsoList:
    df = pd.read_csv(
    'data/power/installed/' + t + '.csv', encoding='utf-8',
    usecols=['EEG_plant_key', 'postal_code', 'energy_carrier'],
    dtype={'postal_code': str})
    tso = pd.concat([tso, df], ignore_index=True)

# %%
metList = ['solar', 'wind']
for m in metList:
    met = pd.read_csv(
        'data/meteorology/' + m + '/stations.csv', encoding='utf-8',
        usecols=['station_id', 'latitude', 'longitude'])
    # rename lat and lon columns for met data
    met = met.rename(
        columns={'longitude': 'met_lon', 'latitude': 'met_lat'})

    # filter for solar and wind power plants
    if m == 'solar':
        tsoData = tso.drop(tso[~((tso.energy_carrier == 'Solar'))].index)
    else:
        tsoData = tso.drop(tso[~(
            (tso.energy_carrier == 'Onshore wind') |
            (tso.energy_carrier == 'Offshore wind'))].index)

    tsoData = tsoData.drop(['energy_carrier'], axis=1)

    # merge postcode and TSO data
    tsoData = pd.merge(tsoData, postcodes, on=['postal_code'], how='left')

    # create list of met station coordinates
    lonList = met['met_lon']
    latList = met['met_lat']
    coordList = list(zip(lonList, latList))

    # create nearest neighbour tree with coordinate list
    tree = spatial.KDTree(coordList)

    # create new empty columns to store tree data
    tsoData['distance'] = np.nan
    tsoData['met_lon'] = np.nan
    tsoData['met_lat'] = np.nan

    # find nearest met station for each power plant in TSO data
    for idx in range(len(tsoData)):
        stn = tree.query(
            [(tsoData.loc[idx, 'longitude'], tsoData.loc[idx, 'latitude'])])
        if stn[1][0] < len(coordList):
            tsoData.loc[idx, 'distance'] = stn[0][0]
            tsoData.loc[idx, 'met_lon'] = coordList[stn[1][0]][0]
            tsoData.loc[idx, 'met_lat'] = coordList[stn[1][0]][1]

    # merge TSO and met data
    tsoData = pd.merge(tsoData, met, on=['met_lon', 'met_lat'], how='left')

    tsoData = tsoData.sort_values(by=['distance'])

    tsoData.to_csv('data/' + m + '.csv', encoding='utf-8', index=False)
