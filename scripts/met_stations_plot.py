"""Plotting German weather station data

This script obtains German weather station data from Deutscher Wetterdienst
(DWD), Germany's meteorological service
(https://www.dwd.de/EN/climate_environment/cdc/cdc_node.html) and
plots the data to produce an interactive map of weather stations in
Germany with tooltips that contain metadata.
"""

# import libraries
from bokeh.models import ColumnDataSource, CategoricalColorMapper, Plot
from bokeh.plotting import figure
from bokeh.tile_providers import get_provider, Vendors
from bokeh.io import output_file, show
from bokeh.palettes import viridis
from pyproj import Transformer
import pandas as pd

# GitLab raw file base URL
url = (
    'https://gitlab.com/api/v4/projects/19753809/repository/files/' +
    'meteorology%2F')

# list of datasets to download
datasets = [
    'sun', 'wind', 'cloudiness','precipitation',
    'air_temperature', 'cloud_type', 'dew_point', 'pressure',
    'soil_temperature', 'visibility', 'solar']

# create empty dataframe to store data
data = pd.DataFrame()

for d in datasets:
    # import data
    df = pd.read_csv(
        url + d + '%2Fstations.csv/raw?ref=master', encoding='utf-8')
    
    # create new dataframe with station ID and dataset type
    df_type = pd.DataFrame({'station_id': df['station_id']})
    df_type[d] = d

    # concatenate datasets
    data = pd.concat([data, df], ignore_index=True)

    # drop duplicate rows
    data = data.drop_duplicates(['station_id'])

    # merge with dataframe with dataset type
    data = pd.merge(data, df_type, on=['station_id'], how='outer')

# fill null values in the dataset columns
data[datasets] = data[datasets].fillna('none')

# merge all dataset values into new column
data['type'] = data[datasets].agg(', '.join, axis=1)

# drop date and dataset columns
data = data.drop(columns=['start_date', 'end_date'])
data = data.drop(columns=datasets)

# remove 'none' strings and underscores
data['type'] = data['type'].str.replace('none, ', '')
data['type'] = data['type'].str.replace(', none', '')
data['type'] = data['type'].str.replace('_', ' ')

# transform latitudes and longitudes from WGS84 to Web Mercator projection
lons = tuple(data['longitude'])
lats = tuple(data['latitude'])
transformer = Transformer.from_crs('epsg:4326', 'epsg:3857', always_xy=True)
xm, ym = transformer.transform(lons, lats)
data['mercator_x'] = xm
data['mercator_y'] = ym

# generate unique colours for each state
states = list(set(data['state']))
palette = viridis(len(states))
color_map = CategoricalColorMapper(factors=states, palette=palette)

# create dictionary of source data for the map
geo_source = ColumnDataSource(data)

# define map tooltips
TOOLTIPS = [
    ('Station', '@station_name'), ('ID', '@station_id'),
    ('Height (m)', '@station_height'), ('State', '@state'),
    ('Type', '@type'), ('(Lon, Lat)', '(@longitude, @latitude)')]

# set output backend for the glyph API
p = Plot(output_backend='webgl')

# set figure title, tooltips and axis types
# set axis types to mercator so that latitudes and longitudes are used
# in the figure
# set output backend for the plotting API
p = figure(
    x_axis_type='mercator', y_axis_type='mercator',
    tooltips=TOOLTIPS, output_backend='webgl')

# set OpenStreetMap / CartoDB overlay
p.add_tile(get_provider(Vendors.CARTODBPOSITRON_RETINA))

# add data points
p.circle(
    x='mercator_x', y='mercator_y', source=geo_source,
    color={'field': 'state', 'transform': color_map})

# open the map
show(p)

# Bokeh components

"""

# import libraries
from bokeh.embed import components

# output the map and save to a custom path
output_file('charts/dwd_stations/dwd_stations_plot.html')

# to export script and div components
script, div = components(p)
# remove script HTML tags to save as JavaScript file
script = script.replace('<script type="text/javascript">', '')
script = script.replace('</script>', '')

# export script as JavaScript file
with open('charts/dwd_stations/dwd_stations.js', 'w') as f:
    print(script, file=f)
# export div as HTML file
with open('charts/dwd_stations/dwd_stations-div.html', 'w') as f:
    print(div, file=f)
# export div as JavaScript file
# (so that it can be read by dwd_stations.html)
with open('charts/dwd_stations/dwd_stations-div.js', 'w') as f:
    print('document.write(`' + div + '\n`);', file=f)
"""
