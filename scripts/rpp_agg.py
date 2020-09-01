"""German renewable power generator data with location and met station

Combines German Erneuerbare-Energien-Gesetz (EEG, which roughly translates
to Renewable Energy Sources Act) power generator data from
Netztransparenz.de (https://www.netztransparenz.de/EEG/Anlagenstammdaten)
with postcode and geo location data from GeoNames
(https://download.geonames.org/export/zip/), and meteorological station
data from Deutscher Wetterdienst (DWD), Germany's meteorological service
(https://www.dwd.de/EN/climate_environment/cdc/cdc_node.html). This script
produces CSV files of wind and/or solar power generators, their approximate
geo location, and their closest meteorological station. The generator
installed capacity is aggregated by postal code.
"""

# import libraries
from scipy import spatial
import pandas as pd
import numpy as np
from os import makedirs
import errno

# GitLab data repository base URL
urlBase = 'https://gitlab.com/api/v4/projects/19753809/repository/files/'

postcodes = pd.read_csv(
    urlBase + 'geography%2Fpostcodes%2FpostcodesDE.csv/raw?ref=master',
    # 'data/geography/postcodes/postcodesDE.csv',
    encoding='utf-8',
    usecols=['postal_code', 'latitude', 'longitude', 'accuracy'])

# take the first postcode value when there are duplicates, drop all others
postcodes = postcodes.drop_duplicates(['postal_code'])

# read meteorological station data
stns = pd.read_csv(
    urlBase + 'meteorology%2Fstations.csv/raw?ref=master',
    # 'data/meteorology/stations.csv',
    encoding='utf-8',
    usecols=['station_id', 'latitude', 'longitude', 'type'])

# rename lat and lon columns for met data
stns = stns.rename(columns={'longitude': 'met_lon', 'latitude': 'met_lat'})

# list of intermittent energy carriers
eList = ['wind']
# eList = ['wind', 'solar']

# create directory to store data
dest = 'data/power/installed/'
try:
    makedirs(dest)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print('\nBE CAREFUL! Directory ' + dest + ' already exists.')

for m in eList:
    # read installed power plants data
    pp = pd.read_csv(
        urlBase + 'power%2Finstalled%2F' + m + '.csv/raw?ref=master',
        # 'data/power/installed/' + m + '.csv',
        encoding='utf-8', usecols=[
            'postal_code', 'installed_capacity',
            'city_district', 'TSO', 'state'])

    # aggregate by postal code
    pp = pd.merge(pp.groupby(
        by='postal_code', as_index=False).installed_capacity.sum(),
        pp.drop(columns='installed_capacity'),
        on=['postal_code']).drop_duplicates(['postal_code'])

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

    # save as CSV
    pp.to_csv(
        dest + m + '_agg.csv', encoding='utf-8', index=False)
