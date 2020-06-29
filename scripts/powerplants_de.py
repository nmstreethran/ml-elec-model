"""German renewable energy power plant data

Extracts German Erneuerbare-Energien-Gesetz (EEG, which roughly translates
to Renewable Energy Sources Act) plant data from Netztransparenz.de
(https://www.netztransparenz.de/EEG/Anlagenstammdaten)
and uses the postcode to derive the approximate coordinates and address.
"""

# import libraries
from geopy.geocoders import Nominatim
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import io
import requests
import zipfile
import os
import errno

# base URL to extract data
urlBase = ('https://www.netztransparenz.de/portals/1/Netztransparenz ' +
    'Anlagenstammdaten 2018 ')

# list of TSOs
tsoList = ['50Hertz Transmission', 'Amprion', 'TenneT TSO', 'TransnetBW']

# create directory to store data
dest = 'data/power/de/'
try:
    os.makedirs(dest)
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
        r = requests.get(url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(dest)
    # exception if no zip file exists
    except zipfile.BadZipFile:
        print ('No data exists for ' + tso)

    # read CSV as dataframe
    data = pd.read_csv(
        dest + tso + '_Anlagenstammdaten_2018.csv', encoding='ISO-8859-1',
        decimal=',', sep=';')

    # roughly tanslate column titles into English
    data = data.set_axis(['EEG_plant_key', 'NB_BNR', 'network_operator',
        'street_land_lot', 'ZIP', 'city_district', 'municipality_key',
        'state', 'installed_capacity', 'energy_carrier',
        'feed_in_voltage_level', 'power_measurement', 'controllability',
        'commissioning', 'decommissioning', 'network_access',
        'network_outlet'], axis='columns', inplace=False)

    # set geo locator and user agent
    geolocator = Nominatim(user_agent='ml_elec_model')

    # create empty columns for geo data and address
    # use gpd.Series to assign geometry dtype
    data['geometry'] = gpd.GeoSeries()
    data['address'] = ''

    # iterate over dataset to obtain address and geometry
    for idx in range(len(data)):
        location = geolocator.geocode(data.loc[idx, 'ZIP'])
        data.loc[idx, 'geometry'] = Point(
            location.longitude, location.latitude)
        data.loc[idx, 'address'] = location.address

    # save as CSV
    data.to_csv(
    dest + tso + '_2018.csv', index=False, encoding='ISO-8859-1')
