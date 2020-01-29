# %%
"""Data extraction from ENTSO-E Transparency Platform's Restful API

Automatically extracts, processes and saves data for each bidding
zone in the North Sea region using the ENTSO-E API Python client
(https://github.com/EnergieID/entsoe-py). Data are downloaded for a
given date range within a particular year.
"""

# %%
# import libraries
from entsoe import EntsoePandasClient
from entsoe.mappings import DOMAIN_MAPPINGS, BIDDING_ZONES
import pandas as pd
import os
import errno
import configparser

# %%
# combine domain and bidding zone keys and values into the
# DOMAIN_MAPPINGS dictionary
DOMAIN_MAPPINGS.update(BIDDING_ZONES)

# %%
# request user to input security token in the command line
token = input('Enter your ENTSO-E security token: ')

# %%
# use security token to access the API
# through the ENTSO-E Pandas client
client = EntsoePandasClient(api_key=token)

# %%
# import user-defined configurations
config = configparser.ConfigParser()
config.read('config/entsoe-api.conf')

# %%
# define attributes for the data to be extracted
start = pd.Timestamp(
    config['start']['year'] + config['start']['month'] +
    config['start']['day'], tz='Europe/Brussels')
end = pd.Timestamp(
    config['end']['year'] + config['end']['month'] +
    config['end']['day'], tz='Europe/Brussels')

# %%
# list of bidding zones
biddingZones = [
    z.strip() for z in config.get('biddingZones', 'biddingZones').split('\n')]
# remove empty strings
biddingZones = list(filter(None, biddingZones))

#%%
# list of bidding zones for crossborder flows
crossborderZones = [
    z.strip() for z in config.get('crossborderFlows', 'zones').split('\n')]
# remove empty strings
crossborderZones = list(filter(None, crossborderZones))

# %%
# list of datasets to download
datasets = [
    z.strip() for z in config.get('datasets', 'datasets').split('\n')]
# remove empty strings
datasets = list(filter(None, datasets))

# %%
# create a directory to store files if it does not exist
path = 'data/entsoe_api'
try:
    os.makedirs(path)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print ('\nBE CAREFUL! Directory %s already exists.' % path)

# %%
for dataset in datasets:

    if biddingZones != []:
        # extracting data for each bidding zone in a loop
        # for country_code in biddingZones:

        if dataset == 'day_ahead_prices':
            for country_code in biddingZones:
                ts = client.query_day_ahead_prices(
                    country_code, start=start, end=end)
                ts.to_csv(
                    path + '/' + dataset + '_' + country_code + '.csv')

        elif dataset == 'load':
            for country_code in biddingZones:
                ts = client.query_load(country_code, start=start, end=end)
                ts.to_csv(
                    path + '/' + dataset + '_' + country_code + '.csv')

        elif dataset == 'load_forecast':
            for country_code in biddingZones:
                ts = client.query_load_forecast(
                    country_code, start=start, end=end)
                ts.to_csv(
                    path + '/' + dataset + '_' + country_code + '.csv')

        elif dataset == 'generation_forecast':
            for country_code in biddingZones:
                ts = client.query_generation_forecast(
                    country_code, start=start, end=end)
                ts.to_csv(
                    path + '/' + dataset + '_' + country_code + '.csv')

        elif dataset == 'withdrawn_unavailability_of_generation_units':
            for country_code in biddingZones:
                ts = client.query_withdrawn_unavailability_of_generation_units(
                    country_code, start=start, end=end)
                ts.to_csv(
                    path + '/' + dataset + '_' + country_code + '.csv')

        elif dataset == 'wind_and_solar_forecast':
            for country_code in biddingZones:
                ts = client.query_wind_and_solar_forecast(
                    country_code, start=start,end=end, psr_type=None)
                ts.to_csv(
                    path + '/' + dataset + '_' + country_code + '.csv')

        elif dataset == 'generation':
            for country_code in biddingZones:
                ts = client.query_generation(
                    country_code, start=start,end=end, psr_type=None)
                ts.to_csv(
                    path + '/' + dataset + '_' + country_code + '.csv')

        elif dataset = 'installed_generation_capacity':
            for country_code in biddingZones:
                ts = client.query_installed_generation_capacity(
                    country_code, start=start,end=end, psr_type=None)
                ts.to_csv(
                    path + '/' + dataset + '_' + country_code + '.csv')

        elif dataset = 'imbalance_prices':
            for country_code in biddingZones:
                ts = client.query_imbalance_prices(
                    country_code, start=start,end=end, psr_type=None)
                ts.to_csv(
                    path + '/' + dataset + '_' + country_code + '.csv')

        elif dataset == 'unavailability_of_generation_units':
            for country_code in biddingZones:
                ts = client.query_unavailability_of_generation_units(
                    country_code, start=start,end=end, docstatus=None)
                ts.to_csv(
                    path + '/' + dataset + '_' + country_code + '.csv')

    if crossborderZones != []:
        for zones in crossborderZones:
            zones = zones.split(', ')
            z = str(zones)[1:-1]
            ts = client.query_crossborder_flows(z, start=start,end=end)
            zones = '_'.join(zones)
            ts.to_csv(
                path + '/crossborder_flows_' + zones + '.csv')
