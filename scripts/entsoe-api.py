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
# define attributes for the data to be extracted
# timestamps for the first half of 2019
start = pd.Timestamp('20190101', tz='Europe/Brussels')
end = pd.Timestamp('20190601', tz='Europe/Brussels')

# %%
# list of bidding zones in the North Sea region
bz_ns = [
    # Belgium, Germany + Luxembourg
    'BE', 'DE-LU',
    # Denmark, France, Great Britain
    'DK-1', 'DK-2', 'FR', 'GB',
    # Irish Single Electricity Market, Netherlands
    'IE-SEM', 'NL',
    # Norway
    'NO-1', 'NO-2', 'NO-3', 'NO-4', 'NO-5',
    # Sweden
    'SE-1', 'SE-2', 'SE-3', 'SE-4'
    ]

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
# extracting data for each bidding zone in a loop
for country_code in bz_ns:
    # create a dataframe for the generation data
    # with the above attributes
    # generation per production type
    ts_gen = client.query_generation(
        country_code, start=start, end=end, psr_type=None)
    # save as CSV
    ts_gen.to_csv(path + '/generation_' + country_code + '.csv')
    
    # load
    ts_load = client.query_load(country_code, start=start, end=end)
    # save as CSV
    ts_load.to_csv(
        path + '/load_' + country_code + '.csv', header=['Load'])
    
    # installed generation capacity per unit
    ts_cap = client.query_installed_generation_capacity_per_unit(
        country_code, start=start, end=end, psr_type=None)
    ts_cap.to_csv(
        path + '/installed_capacity_' + country_code + '.csv')
