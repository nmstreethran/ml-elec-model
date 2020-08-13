# import libraries
from scipy import spatial
import pandas as pd
import numpy as np

postcodes = pd.read_csv(
    'data/geography/postcodes/postcodesDE.csv', encoding='utf-8',
    usecols=['postal_code', 'latitude', 'longitude'])

# take the first postcode value when there are duplicates, drop all others
postcodes = postcodes.drop_duplicates(['postal_code'])

# read meteorological station data
stns = pd.read_csv(
    'data/meteorology/stations.csv', encoding='utf-8',
    usecols=['station_id', 'latitude', 'longitude', 'type'])

# rename lat and lon columns for met data
stns = stns.rename(columns={'longitude': 'met_lon', 'latitude': 'met_lat'})

# list of intermittent energy carriers
eList = ['wind']
# eList = ['wind', 'solar']

for m in eList:
    # read installed power plants data
    pp = pd.read_csv(
        'data/power/installed/' + m + '.csv',
        encoding='utf-8', usecols=['EEG_plant_key', 'postal_code'])

    # merge postcode and power plant data
    pp = pd.merge(pp, postcodes, on=['postal_code'])

    # filter meteorological data based on energy carrier
    met = stns[stns['type'].str.contains(m)]

    # drop type column
    met = met.drop(columns=['type'])

    # create list of met station coordinates
    lonList = met['met_lon']
    latList = met['met_lat']
    coordList = list(zip(lonList, latList))

    # create nearest neighbour tree with coordinate list
    tree = spatial.KDTree(coordList)

    # create new empty columns to store tree data
    pp['distance'] = np.nan
    pp['met_lon'] = np.nan
    pp['met_lat'] = np.nan

    # find nearest met station for each power plant in power plant data
    for idx in range(len(pp)):
        stn = tree.query(
            [(pp.loc[idx, 'longitude'], pp.loc[idx, 'latitude'])])
        if stn[1][0] < len(coordList):
            pp.loc[idx, 'distance'] = stn[0][0]
            pp.loc[idx, 'met_lon'] = coordList[stn[1][0]][0]
            pp.loc[idx, 'met_lat'] = coordList[stn[1][0]][1]

    # merge power plant and met data
    pp = pd.merge(pp, met, on=['met_lon', 'met_lat'], how='left')

    # sort data by distance value
    pp = pp.sort_values(by=['distance'])

    # save data as CSV file
    pp.to_csv(
        'data/power/installed/' + m + '_met_loc.csv',
        encoding='utf-8', index=False)
