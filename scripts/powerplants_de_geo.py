"""German renewable energy power generator data with geo location

Combines German Erneuerbare-Energien-Gesetz (EEG, which roughly translates
to Renewable Energy Sources Act) generator data from Netztransparenz.de
(https://www.netztransparenz.de/EEG/Anlagenstammdaten) with postcode and
geo location data from GeoNames (https://download.geonames.org/export/zip/)
for the following countries: DE, DK, SE, AT, CH, CZ, FR, LU, NL, PL.
"""

# import libraries
import pandas as pd

# list of TSOs
tsoList = ['50Hertz_Transmission', 'Amprion', 'TenneT_TSO', 'TransnetBW']

# read postcode data
postcodes = pd.read_csv(
    'data/geo/postcodesDE.csv', encoding='utf-8', dtype={'postal_code': str},
    usecols=['postal_code', 'place_name', 'latitude', 'longitude',
    'accuracy', 'admin_name1', 'admin_name2', 'admin_name3'])

for tso in tsoList:
    # read TSO data
    data = pd.read_csv(
        'data/power/de/' + tso + '_2018.csv', encoding='utf-8',
        usecols=['postal_code', 'state', 'installed_capacity',
        'energy_carrier', 'network_operator', 'address', 'city_district',
        'commissioning', 'decommissioning', 'network_connection',
        'network_disconnection'], dtype={'postal_code': str},
        dayfirst=True, parse_dates=['commissioning', 'decommissioning',
        'network_connection', 'network_disconnection'])

    # assign TSO name to new column
    data['TSO'] = tso

    # merge postcode data with TSO data
    data_merged = data.merge(postcodes, on='postal_code', how='left')

    # save as CSV
    data_merged.to_csv(
        'data/power/de/' + tso + '_geo_2018.csv', index=None,
        encoding='utf-8')
