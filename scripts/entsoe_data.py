"""Data extraction from ENTSO-E Transparency Platform"s Restful API

Extracts and saves data from the ENTSO-E Transparency Platform
(https://transparency.entsoe.eu/) for the DE-LU bidding zone using the
ENTSO-E API Python client (https://github.com/EnergieID/entsoe-py). Data
are downloaded for a given date range within a particular year.
"""

# import libraries
from entsoe import EntsoePandasClient
from entsoe.mappings import DOMAIN_MAPPINGS, BIDDING_ZONES
from entsoe.exceptions import NoMatchingDataError
from requests.exceptions import RequestException
import pandas as pd
from os import makedirs
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
start = pd.Timestamp('20180101', tz='Europe/Brussels')
end = pd.Timestamp('20180701', tz='Europe/Brussels')

# bidding zone
bzn = 'DE-AT-LU'

# create a directory to store files if it does not already exist
fpaths = [
    'data/power/installed/', 'data/power/generation/',
    'data/prices/', 'data/load/']

for f in fpaths:
    try:
        makedirs(f + 'temp/')
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
        else:
            print('\nBE CAREFUL! Directory %stemp/ already exists.' % f)

# extract data for bidding zone
# day-ahead prices
try:
    df = client.query_day_ahead_prices(bzn, start=start, end=end)
    df = df.rename_axis('timestamp')
    df = df.rename('price')
    df.to_csv(fpaths[2] + 'day_ahead_prices_' + bzn + '.csv')
except NoMatchingDataError:
    print('No matching data found for ' + bzn + ': day_ahead_prices')
except RequestException as e:
    print(str(e) + '\n' + bzn + ': day_ahead_prices')

# load
try:
    df = client.query_load(bzn, start=start, end=end)
    df = df.rename_axis('timestamp')
    df = df.rename('load')
    df.to_csv(fpaths[3] + 'load_' + bzn + '.csv')
except NoMatchingDataError:
    print('No matching data found for ' + bzn + ': load')
except RequestException as e:
    print(str(e) + '\n' + bzn + ': load')

# load forecast
try:
    df = client.query_load_forecast(bzn, start=start, end=end)
    df = df.rename_axis('timestamp')
    df = df.rename('load_forecast')
    df.to_csv(fpaths[3] + 'load_forecast_' + bzn + '.csv')
except NoMatchingDataError:
    print('No matching data found for ' + bzn + ': load_forecast')
except RequestException as e:
    print(str(e) + '\n' + bzn + ': load_forecast')

# generation forecast
try:
    df = client.query_generation_forecast(bzn, start=start, end=end)
    df = df.rename_axis('timestamp')
    df = df.rename('generation_forecast')
    # remove duplicate rows
    df = df.sort_values(by=['timestamp', 'generation_forecast'])
    df = df.drop_duplicates(['timestamp'], keep='last')
    df.to_csv(fpaths[1] + 'generation_forecast_' + bzn + '.csv')
except NoMatchingDataError:
    print('No matching data found for ' + bzn + ': generation_forecast')
except RequestException as e:
    print(str(e) + '\n' + bzn + ': generation_forecast')

# wind and solar forecast
try:
    df = client.query_wind_and_solar_forecast(
        bzn, start=start, end=end, psr_type=None)
    df = df.rename_axis('timestamp')
    df.to_csv(fpaths[1] + 'wind_and_solar_forecast_' + bzn + '.csv')
except NoMatchingDataError:
    print(
        'No matching data found for ' + bzn + ': wind_and_solar_forecast')
except RequestException as e:
    print(str(e) + '\n' + bzn + ': wind_and_solar_forecast')

# generation
try:
    df = client.query_generation(
        bzn, start=start, end=end, psr_type=None)
    df = df.rename_axis('timestamp')
    df.to_csv(fpaths[1] + 'generation_' + bzn + '.csv')
except NoMatchingDataError:
    print('No matching data found for ' + bzn + ': generation')
except RequestException as e:
    print(str(e) + '\n' + bzn + ': generation')

# installed generation capacity
try:
    df = client.query_installed_generation_capacity(
        bzn, start=start, end=end, psr_type=None)
    df = df.rename_axis('timestamp')
    df.to_csv(
        fpaths[0] + 'installed_generation_capacity_' + bzn + '.csv')
except NoMatchingDataError:
    print(
        'No matching data for ' + bzn + ': installed_generation_capacity')
except RequestException as e:
    print(str(e) + '\n' + bzn + ': installed_generation_capacity')

# # installed generation capacity per unit
# try:
#     df = client.query_installed_generation_capacity_per_unit(
#         bzn, start=start, end=end, psr_type=None)
#     df = df.rename_axis('id')
#     # manually replace accented characters
#     df['Name'] = df['Name'].str.replace('Ã¼', 'ü')
#     df['Name'] = df['Name'].str.replace('Ã¤', 'ä')
#     df['Name'] = df['Name'].str.replace('Ã¶', 'ö')
#     df['Name'] = df['Name'].str.replace('Ã', 'ß')
#     df.to_csv(
#         fpaths[0] + 'installed_generation_capacity_per_unit_' + bzn
#         + '.csv', encoding='utf-8')
# except NoMatchingDataError:
#     print(
#         'No matching data found for ' + bzn +
#         ': installed_generation_capacity_per_unit')
# except RequestException as e:
#     print(
#         str(e) + '\n' + bzn + ': installed_generation_capacity_per_unit')

# # unavailability of production units
# try:
#     df = client.query_unavailability_of_production_units(
#         bzn, start=start, end=end)
#     df.to_csv(
#         fpaths[0] + 'unavailability_of_production_units_' + bzn + '.csv')
# except NoMatchingDataError:
#     print(
#         'No matching data for ' + bzn +
#         ': unavailability_of_production_units')
# except RequestException as e:
#     print(str(e) + '\n' + bzn + ': unavailability_of_production_units')

# # unavailability of generation units
# try:
#     df = client.query_unavailability_of_generation_units(
#         bzn, start=start, end=end, docstatus=None)
#     df.to_csv(
#         fpaths[0] + 'unavailability_of_generation_units_' + bzn + '.csv')
# except NoMatchingDataError:
#     print(
#         'No matching data found for ' + bzn +
#         ': unavailability_of_generation_units')
# except RequestException as e:
#     print(str(e) + '\n' + bzn + ': unavailability_of_generation_units')

# # withdrawn unavailability of generation units
# try:
#     df = client.query_withdrawn_unavailability_of_generation_units(
#         bzn, start=start, end=end)
#     df.to_csv(
#         fpaths[0] + 'withdrawn_unavailability_of_generation_units_' +
#         bzn + '.csv')
# except NoMatchingDataError:
#     print(
#         'No matching data for ' + bzn +
#         ': withdrawn_unavailability_of_generation_units')
# except RequestException as e:
#     print(
#         str(e) + '\n' + bzn +
#         ': withdrawn_unavailability_of_generation_units')

# # generation per plant
# try:
#     df = client.query_generation_per_plant(
#         bzn, start=start, end=end, lookup_bzones=True)
#     df.to_csv(fpaths[0] + 'generation_per_plant_' + bzn + '.csv')
# except NoMatchingDataError:
#     print('No matching data for ' + bzn + ': generation_per_plant')
# except RequestException as e:
#     print(str(e) + '\n' + bzn + ': generation_per_plant')
