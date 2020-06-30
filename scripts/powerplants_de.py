"""German renewable energy power plant data

Extracts German Erneuerbare-Energien-Gesetz (EEG, which roughly translates
to Renewable Energy Sources Act) plant data from Netztransparenz.de
(https://www.netztransparenz.de/EEG/Anlagenstammdaten).
"""

# import libraries
from io import BytesIO
from requests import get
from zipfile import BadZipFile, ZipFile
from os import makedirs
import errno
import pandas as pd

# base URL to extract data
urlBase = ('https://www.netztransparenz.de/portals/1/Netztransparenz ' +
    'Anlagenstammdaten 2018 ')

# list of TSOs
tsoList = ['50Hertz Transmission', 'Amprion', 'TenneT TSO', 'TransnetBW']

# create directory to store data
dest = 'data/power/de/'
try:
    makedirs(dest)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print ('\nBE CAREFUL! Directory ' + dest + ' already exists.')

# download contents of zip file into directory
for tso in tsoList:
    # URL of zip file for each TSO
    url = urlBase + tso + ' GmbH.zip'
    try:
        r = get(url)
        z = ZipFile(BytesIO(r.content))
        z.extractall(dest)
    # exception if no zip file exists
    except BadZipFile:
        print ('No data exists for ' + tso)

# roughly tanslate column titles into English
cols = ['EEG_plant_key', 'NB_BNR', 'network_operator', 'street_land_lot',
        'postal_code', 'city_district', 'municipality_key', 'state',
        'installed_capacity', 'energy_carrier', 'feed_in_voltage_level',
        'power_measurement', 'controllability', 'commissioning',
        'decommissioning', 'network_access', 'network_outlet']

# assign column names for each dataset
data = pd.read_csv(
    dest + '50Hertz Transmission GmbH EEG-Zahlungen Stammdaten 2018.csv',
    encoding='ISO-8859-1', decimal=',', sep=';',
    dtype={'Netzzugang': str, 'Netzabgang': str})
data = data.set_axis(cols, axis='columns', inplace=False)
data.to_csv(
    dest + '50Hertz_Transmission_2018.csv', index=None,
    encoding='ISO-8859-1')

data = pd.read_csv(
    dest + 'Netztransparenz Anlagenstammdaten 2018 Amprion GmbH.csv',
    encoding='ISO-8859-1', decimal=',', sep=';',
    dtype={'INSTALLIERTE_LEISTUNG': 'str'})
data = data.set_axis(cols, axis='columns', inplace=False)
data.to_csv(
    dest + 'Amprion_2018.csv', index=None, encoding='ISO-8859-1')

data = pd.read_csv(
    dest + 'TenneT TSO GmbH Anlagenstammdaten 2018.csv',
    encoding='ISO-8859-1', decimal=',', sep=';',
    dtype={'PLZ': str, 'Ausserbetriebnahme': str, 'Netzzugang': str,
    'Netzabgang': str})
data = data.set_axis(cols, axis='columns', inplace=False)
data.to_csv(
    dest + 'TenneT_TSO_2018.csv', index=None, encoding='ISO-8859-1')

data = pd.read_csv(
    dest + 'TransnetBW_Anlagenstammdaten_2018.csv',
    encoding='ISO-8859-1', decimal=',', sep=';',
    dtype={'Ausserbetriebnahme': str})
data = data.set_axis(cols, axis='columns', inplace=False)
data.to_csv(
    dest + 'TransnetBW_2018.csv', index=None, encoding='ISO-8859-1')
