"""Data extraction from ENTSO-E Transparency Platform"s Restful API

Extracts and saves data for each bidding zone using the ENTSO-E API
Python client (https://github.com/EnergieID/entsoe-py). Data are
downloaded for a given date range within a particular year.
"""

# import libraries
from entsoe import EntsoePandasClient
from entsoe.mappings import DOMAIN_MAPPINGS, BIDDING_ZONES
from entsoe.exceptions import NoMatchingDataError
from requests.exceptions import RequestException
import pandas as pd
import os
import errno
from getpass import getpass

# combine domain and bidding zone keys and values into the
# DOMAIN_MAPPINGS dictionary
DOMAIN_MAPPINGS.update(BIDDING_ZONES)

# request user to input security token in the command line
token = getpass('Enter your ENTSO-E security token: ')

# use security token to access the API
# through the ENTSO-E Pandas client
client = EntsoePandasClient(api_key=token)

# define time range of data to be extracted
start = pd.Timestamp('20190101', tz='Europe/Brussels')
end = pd.Timestamp('20190630', tz='Europe/Brussels')

# # list of bidding zones
bznList = [
    'DE-LU', 'DK-1', 'DK-2', 'NO-1', 'NO-2', 'NO-3',
    'NO-4', 'NO-5', 'SE-1', 'SE-2', 'SE-3', 'SE-4']

# create a directory to store files if it does not already exist
path = 'data/entsoe'
try:
    os.makedirs(path)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print ('\nBE CAREFUL! Directory %s already exists.' % path)

# extract data for each bidding zone
for bzn in bznList:
    try:
        df = client.query_day_ahead_prices(bzn, start=start, end=end)
        df.to_csv(path + '/' + 'day_ahead_prices_' + bzn + '.csv')
    except NoMatchingDataError:
        print('No matching data found for ' + bzn + ': day_ahead_prices')
    except RequestException as e:
        print(str(e) + '\n' + bzn + ': day_ahead_prices')

    try:
        df = client.query_load(bzn, start=start, end=end)
        df.to_csv(path + '/' + 'load__' + bzn + '.csv')
    except NoMatchingDataError:
        print('No matching data found for ' + bzn + ': load')
    except RequestException as e:
        print(str(e) + '\n' + bzn + ': load')

    try:
        df = client.query_load_forecast(bzn, start=start, end=end)
        df.to_csv(path + '/' + 'load_forecast_' + bzn + '.csv')
    except NoMatchingDataError:
        print('No matching data found for ' + bzn + ': load_forecast')
    except RequestException as e:
        print(str(e) + '\n' + bzn + ': load_forecast')

    try:
        df = client.query_generation_forecast(bzn, start=start, end=end)
        df.to_csv(path + '/' + 'generation_forecast_' + bzn + '.csv')
    except NoMatchingDataError:
        print(
            'No matching data found for ' + bzn + ': generation_forecast')
    except RequestException as e:
        print(str(e) + '\n' + bzn + ': generation_forecast')

    try:
        df = client.query_wind_and_solar_forecast(
            bzn, start=start, end=end, psr_type=None)
        df.to_csv(path + '/' + 'wind_and_solar_forecast_' + bzn + '.csv')
    except NoMatchingDataError:
        print(
            'No matching data found for ' + bzn +
            ': wind_and_solar_forecast')
    except RequestException as e:
        print(str(e) + '\n' + bzn + ': wind_and_solar_forecast')

    try:
        df = client.query_generation(
            bzn, start=start, end=end, psr_type=None)
        df.to_csv(path + '/' + 'generation__' + bzn + '.csv')
    except NoMatchingDataError:
        print('No matching data found for ' + bzn + ': generation')
    except RequestException as e:
        print(str(e) + '\n' + bzn + ': generation')

    try:
        df = client.query_installed_generation_capacity(
            bzn, start=start, end=end, psr_type=None)
        df.to_csv(
            path + '/' + 'installed_generation_capacity__' + bzn + '.csv')
    except NoMatchingDataError:
        print(
            'No matching data for ' + bzn +
            ': installed_generation_capacity')
    except RequestException as e:
        print(str(e) + '\n' + bzn + ': installed_generation_capacity')

    try:
        df = client.query_installed_generation_capacity_per_unit(
            bzn, start=start, end=end, psr_type=None)
        df.to_csv(
            path + '/' + 'installed_generation_capacity_per_unit_' + bzn
            + '.csv')
    except NoMatchingDataError:
        print(
            'No matching data found for ' + bzn +
            ': installed_generation_capacity_per_unit')
    except RequestException as e:
        print(
            str(e) + '\n' + bzn +
            ': installed_generation_capacity_per_unit')

    try:
        df = client.query_unavailability_of_production_units(
            bzn, start=start, end=end)
        df.to_csv(
            path + '/' + 'unavailability_of_production_units_' + bzn
            + '.csv')
    except NoMatchingDataError:
        print(
            'No matching data for ' + bzn +
            ': unavailability_of_production_units')
    except RequestException as e:
        print(str(e) + '\n' + bzn + ': unavailability_of_production_units')

    try:
        df = client.query_unavailability_of_generation_units(
            bzn, start=start, end=end, docstatus=None)
        df.to_csv(
            path + '/' + 'unavailability_of_generation_units_' + bzn +
            '.csv')
    except NoMatchingDataError:
        print(
            'No matching data found for ' + bzn +
            ': unavailability_of_generation_units')
    except RequestException as e:
        print(str(e) + '\n' + bzn + ': unavailability_of_generation_units')

    try:
        df = client.query_withdrawn_unavailability_of_generation_units(
            bzn, start=start, end=end)
        df.to_csv(
            path + '/' + 'withdrawn_unavailability_of_generation_units_' +
            bzn + '.csv')
    except NoMatchingDataError:
        print(
            'No matching data for ' + bzn +
            ': withdrawn_unavailability_of_generation_units')
    except RequestException as e:
        print(
            str(e) + '\n' + bzn +
            ': withdrawn_unavailability_of_generation_units')

    # try:
    #     df = client.query_generation_per_plant(
    #         bzn, start=start, end=end, lookup_bzones=True)
    #     df.to_csv(path + '/' + 'generation_per_plant_' + bzn + '.csv')
    # except NoMatchingDataError:
    #     print('No matching data for ' + bzn + ': generation_per_plant')
    # except RequestException as e:
    #     print(str(e) + '\n' + bzn + ': generation_per_plant')
