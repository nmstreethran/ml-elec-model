"""German renewable power generator data

Extracts German Erneuerbare-Energien-Gesetz (EEG, which roughly translates
to Renewable Energy Sources Act) power generator data from
Netztransparenz.de (https://www.netztransparenz.de/EEG/Anlagenstammdaten).
"""

# import libraries
from io import BytesIO
from requests import get
from zipfile import BadZipFile, ZipFile
from os import makedirs
import errno
import pandas as pd

# base URL to extract data
urlBase = (
    'https://www.netztransparenz.de/portals/1/Netztransparenz ' +
    'Anlagenstammdaten 2018 ')

# list of TSOs and the file name
tsoList = [
    ('50Hertz Transmission',
    '50Hertz Transmission GmbH EEG-Zahlungen Stammdaten 2018'),
    ('Amprion', 'Netztransparenz Anlagenstammdaten 2018 Amprion GmbH'),
    ('TenneT TSO', 'TenneT TSO GmbH Anlagenstammdaten 2018'),
    ('TransnetBW', 'TransnetBW_Anlagenstammdaten_2018')
]

# create directory to store data
dest = 'data/power/installed/'
try:
    makedirs(dest + 'temp/')
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print ('\nBE CAREFUL! Directory ' + dest + 'temp/ already exists.')

# roughly tanslate column titles into English
cols = [
    'EEG_plant_key', 'NB_BNR', 'network_operator', 'address',
    'postal_code', 'city_district', 'municipality_key', 'state',
    'installed_capacity', 'energy_carrier', 'feed_in_voltage_level',
    'power_measurement', 'controllability', 'commissioning',
    'decommissioning', 'network_connection', 'network_disconnection']

for tso, f in tsoList:
    # URL of zip file for each TSO
    url = urlBase + tso + ' GmbH.zip'

    # download contents of zip file into directory
    try:
        r = get(url)
        z = ZipFile(BytesIO(r.content))
        z.extractall(dest + 'temp/')
    # exception if no zip file exists
    except BadZipFile:
        print ('No data exists for ' + tso)

    # read downloaded CSV file and assign translated column names
    # with additional settings for encoding, decimals, dates, etc.
    data = pd.read_csv(
        dest + 'temp/' + f + '.csv', encoding='ISO-8859-1', decimal=',',
        sep=';', header=0, names=cols, dayfirst=True, thousands='.',
        parse_dates=['commissioning', 'decommissioning',
        'network_connection', 'network_disconnection'],
        dtype={'NB_BNR': str, 'postal_code': str, 'municipality_key': str})

    # roughly translate values into English
    data.energy_carrier.replace(
        ['Wasser', 'Biomasse', 'Wind an Land', 'Deponiegas',
        'Wind auf See', 'Klärgas', 'Geothermie', 'Grubengas'],
        ['Hydro', 'Biomass', 'Onshore wind', 'Landfill gas',
        'Offshore wind', 'Sewage gas', 'Geothermal', 'Mine gas'],
        inplace=True)

    data.power_measurement.replace(
        ['Nein', 'Ja'], ['No', 'Yes'], inplace=True)

    data.controllability.replace(
        ['nicht regelbar', '70 % Begrenzung', 'regelbar n. § 9 Abs. 2 EEG',
        'regelbar n § 9 Abs. 2 EEG', 'regelbar n. § 9 Abs. 1 EEG',
        'regelbar n § 9 Abs. 1 EEG', 'regelbar nach § 9 Abs. 1 EEG'],
        ['not adjustable', '70 % limit',
        'adjustable according to § 9 Abs. 2 EEG',
        'adjustable according to § 9 Abs. 2 EEG',
        'adjustable according to § 9 Abs. 1 EEG',
        'adjustable according to § 9 Abs. 1 EEG',
        'adjustable according to § 9 Abs. 1 EEG'], inplace=True)

    data.state.replace(
        ['Ausschließliche Wirtschaftszone', 'Ausland'],
        ['exclusive economic zone', 'foreign country'], inplace=True)

    # replace space with underscore in file name
    fname = tso.replace(' ', '_')

    # save as new CSV
    data.to_csv(dest + fname + '.csv', index=None, encoding='utf-8')
