# %%
"""Nord Pool market data extraction

Using Pandas to automatically extract and process historical market
data from Nord Pool's website and save as a CSV file, for a given
year. This script has been tested for the following datasets of
hourly resolution:
- Elspot prices, volumes, flows and capacities
- N2EX day-ahead auction prices, capacities and volumes
- market coupling capacities and flows
"""

# %%
# import libraries
import pandas as pd
import numpy as np
import os
import errno
from datetime import datetime
from itertools import cycle, islice

# %%
# define start and end dates of data (must be from the same year)
# YYYYMMDD
start = 20190101
end = 20190601

# %%
# convert times to datetime
start = pd.to_datetime(start, format='%Y%m%d')
end = pd.to_datetime(end, format='%Y%m%d')
# year string
yr = start.strftime('%Y')
# empty list to contain list of hours
hours = []
# add zero padding
for hour in list(range(0, 24)):
    hour = str(hour).zfill(2)
    hours.append(hour)

# %% 
# market data repo url
repourl = 'https://www.nordpoolgroup.com/globalassets/marketdata-excel-files/'

# %%
# create directories to store files for each state if they do not exist
path = 'data/market/nordpool'
try:
    os.makedirs(path)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print ('\nBE CAREFUL! Directory %s already exists.' % path)

# %%
# list of datasets to download
datasets = [
    # Elspot
    'elspot-prices_' + yr + '_hourly_eur',
    'elspot-volumes_' + yr + '_hourly',
    'elspot-flow-dk_' + yr + '_hourly',
    'elspot-flow-no_' + yr + '_hourly',
    'elspot-flow-se_' + yr + '_hourly',
    'elspot-capacities-dk_' + yr + '_hourly',
    'elspot-capacities-no_' + yr + '_hourly',
    'elspot-capacities-se_' + yr + '_hourly',
    # N2EX
    'n2ex-day-ahead-auction-prices_' + yr + '_hourly_eur',
    'n2ex-market-coupling-capacities_' + yr + '_hourly',
    'n2ex-day-ahead-auction-volumes_' + yr + '_hourly',
    # other
    'market-coupling-capacities_' + yr + '_hourly',
    'market-coupling-flow_' + yr + '_hourly'
    ]

# %%
# read and parse data
for dataset in datasets:
    # different header level for N2EX volume dataset
    if 'n2ex-day-ahead-auction-volumes' in dataset:
        data = pd.read_html(
            repourl + dataset + '.xls', header=[3], thousands=None,
            decimal=',', encoding='utf-8')[0]
    else:
        data = pd.read_html(
            repourl + dataset + '.xls', header=[2], thousands=None,
            decimal=',', encoding='utf-8')[0]
    
    # iterate list of hours over dataset
    it = cycle(hours)
    # change range of hours to start hour
    data['Hours'] = list(islice(it, len(data)))
    # create new column with timestamp (date and start hour)
    data['timestamp'] = data.iloc[:, 0] + '-' + data.iloc[:, 1]
    # convert to datetime
    data['timestamp'] = pd.to_datetime(
        data['timestamp'], format='%d-%m-%Y-%H')
    
    # rename Norwegian bidding zones in elspot prices dataset
    if 'elspot-prices' in dataset:
        data = data.rename(columns={
            'Oslo': 'NO1', 'Kr.sand': 'NO2', 'Molde': 'NO3',
            'Tromsø': 'NO4', 'Bergen': 'NO5'})
        # drop Trondheim because it's the same as Molde
        data = data.drop(['Tr.heim'], axis=1)
    
    # delete old columns with date and hours
    if 'n2ex' in dataset:
    # N2EX datasets have hours in CET/CEST and UTC
    # use CET/CEST as standard for all datasets
        data = data.drop(data.columns[0:3], axis=1)
    else:
        data = data.drop(data.columns[0:2], axis=1)
    
    # list of column names
    cols = data.columns.tolist()
    # move timestamp column to the beginning
    cols = cols[-1:] + cols[:-1]
    data = data[cols]
    
    # save as CSV
    data.to_csv(path + '/' + dataset + '.csv', index=None)
