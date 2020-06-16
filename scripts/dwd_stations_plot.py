"""Plotting German weather station data

This script executes dwd_stations.py and dwd_stations_nuts.py to obtain
German weather station data from Deutscher Wetterdienst (DWD), Germany's
meteorological service, and nomenclature of territorial units for
statistics (NUTS) data at level 3 from Eurostat, respectively. nuts_de.py
combines these two datasets. This script then plots the data to produce
an interactive map of weather stations in Germany with tooltips that
contain metadata.
"""

# import libraries
from bokeh.models import ColumnDataSource, CategoricalColorMapper
from bokeh.plotting import figure
from bokeh.tile_providers import get_provider, Vendors
from bokeh.io import output_file, show
from bokeh.embed import components
from bokeh.palettes import viridis
from pyproj import Transformer
import pandas as pd

# import variables from dwd_stations_nuts.py
from dwd_stations_nuts import dwd_de as data

# drop geometry columns
data = data.drop(columns=['geometry', 'point'])

# transform latitudes and longitudes from WGS84 to Web Mercator projection
lons = tuple(data['longitude'])
lats = tuple(data['latitude'])
transformer = Transformer.from_crs(
    'epsg:4326', 'epsg:3857', always_xy=True)
xm, ym = transformer.transform(lons, lats)
data['mercator_x'] = xm
data['mercator_y'] = ym

# generate unique colours for each state
state = list(set(data['state']))
palette = viridis(len(state))
color_map = CategoricalColorMapper(factors=state, palette=palette)

# create dictionary of source data for the map
geo_source = ColumnDataSource(data)

# define map tooltips
TOOLTIPS = [
    ('Station', '@name'), ('id', '@id'), ('Height (m)', '@height'),
    ('State', '@state'), ('NUTS 3', '@NUTS_ID: @NUTS_NAME'),
    ('(Lon, Lat)', '(@longitude, @latitude)')
]

# set figure title, tooltips and axis types
# set axis types to mercator so that latitudes and longitudes are used
# in the figure
p = figure(
    title='German weather stations. Data: DWD.de, Eurostat.',
    x_axis_type='mercator', y_axis_type='mercator', tooltips=TOOLTIPS)

# set OpenStreetMap / CartoDB overlay
p.add_tile(get_provider(Vendors.CARTODBPOSITRON_RETINA))

# add data points
p.circle(source=geo_source, x='mercator_x', y='mercator_y',
    color={'field': 'state', 'transform': color_map})

# open the map
show(p)

"""

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
