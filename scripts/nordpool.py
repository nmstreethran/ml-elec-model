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
import configparser
from urllib.error import HTTPError

# %%
# import user-defined configurations
config = configparser.ConfigParser()
config.read('config.ini')

# %%
# define start and end dates of data
start = config['start']['year'] + config['start']['month'] + \
    config['start']['day']
end = config['end']['year'] + config['end']['month'] + \
    config['end']['day']

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
    z.strip() for z in config.get('NordPool', 'datasets').split('\n')]
# remove empty strings
datasets = list(filter(None, datasets))

# %%
# read and parse data
for dataset in datasets:
    # different header level for N2EX volume dataset
    if 'n2ex-day-ahead-auction-volumes' in dataset:
        try:
            data = pd.read_html(
                repourl + dataset + '_' + yr + '_' +
                config['NordPool']['resolution'] + '.xls', header=[3],
                thousands=None, decimal=',', encoding='utf-8')[0]
        except HTTPError as exception:
            if exception.code != 404:
                raise
            else:
                print ('\nSorry! This dataset does not exist: ' + dataset
                    + '_' + yr + '_' + config['NordPool']['resolution'])
                continue
    elif 'n2ex' in dataset and 'prices' in dataset:
        try:
            data = pd.read_html(
                repourl + dataset + '_' + yr + '_' +
                config['NordPool']['resolution'] + '_' +
                config['NordPool']['N2EXcurrency'] + '.xls', header=[2],
                thousands=None, decimal=',', encoding='utf-8')[0]
        except HTTPError as exception:
            if exception.code != 404:
                raise
            else:
                print ('\nSorry! This dataset does not exist: ' + dataset
                    + '_' + yr + '_' + config['NordPool']['resolution'] +
                    '_' + config['NordPool']['N2EXcurrency'])
                continue
    elif 'prices' in dataset or 'regulating-power' in dataset:
        try:
            data = pd.read_html(
                repourl + dataset + '_' + yr + '_' +
                config['NordPool']['resolution'] + '_' +
                config['NordPool']['currency'] + '.xls', header=[2],
                thousands=None, decimal=',', encoding='utf-8')[0]
        except HTTPError as exception:
            if exception.code != 404:
                raise
            else:
                print ('\nSorry! This dataset does not exist: ' + dataset
                    + '_' + yr + '_' + config['NordPool']['resolution'] +
                    '_' + config['NordPool']['currency'])
                continue
    # elif 'elspot-capacities' or 'elspot-flow' in dataset:
    #     for country in countries:
    #         data = pd.read_html(
    #             repourl + dataset + '-' + country + '_' + yr + '_' +
    #             config['NordPool']['resolution'] + '.xls',
    #             header=[2], thousands=None, decimal=',',
    #             encoding='utf-8')[0]
    else:
        try:
            data = pd.read_html(
                repourl + dataset + '_' + yr + '_' +
                config['NordPool']['resolution'] + '.xls', header=[2],
                thousands=None, decimal=',', encoding='utf-8')[0]
        except HTTPError as exception:
            if exception.code != 404:
                raise
            else:
                print ('\nSorry! This dataset does not exist: ' + dataset
                    + '_' + yr + '_' + config['NordPool']['resolution'])
                continue
    
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
    if 'n2ex' in dataset and 'prices' in dataset:
        data.to_csv(path + '/' + dataset + '_' + yr + '_' +
            config['NordPool']['resolution'] + '_' +
            config['NordPool']['N2EXcurrency'] + '.csv', index=None)
    elif 'prices' in dataset:
        data.to_csv(path + '/' + dataset + '_' + yr + '_' +
            config['NordPool']['resolution'] + '_' +
            config['NordPool']['currency'] + '.csv', index=None)
    else:
        data.to_csv(path + '/' + dataset + '_' + yr + '_' +
            config['NordPool']['resolution'] + '.csv', index=None)
