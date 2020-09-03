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
from bokeh.io import show
from bokeh.palettes import viridis
from pyproj import Transformer
import pandas as pd

# GitLab raw file base URL
url = (
    'https://gitlab.com/api/v4/projects/19753809/repository/files/' +
    'meteorology%2Fstations%2Ecsv/raw?ref=master')

data = pd.read_csv(
    url, encoding='utf-8', usecols=[
        'station_id', 'station_height', 'latitude', 'longitude',
        'station_name', 'state', 'type'])

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
    x_axis_type='mercator', y_axis_type='mercator', tooltips=TOOLTIPS,
    output_backend='webgl', sizing_mode='scale_both')

# set OpenStreetMap / CartoDB overlay
p.add_tile(get_provider(Vendors.CARTODBPOSITRON_RETINA))

# add data points
p.circle(
    x='mercator_x', y='mercator_y', source=geo_source,
    color={'field': 'state', 'transform': color_map})

# open the map
show(p)
