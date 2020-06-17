"""Plotting German weather station data

This script plots German weather station data from Deutscher Wetterdienst
(DWD), Germany's meteorological service
(https://www.dwd.de/EN/climate_environment/cdc/cdc_node.html), and
nomenclature of territorial units for statistics (NUTS) data at level 3
from Eurostat (https://ec.europa.eu/eurostat/web/nuts/background). It
produces an interactive map of weather stations in Germany with tooltips
that contain metadata.
"""

# import libraries
from bokeh.models import ColumnDataSource, CategoricalColorMapper
from bokeh.plotting import figure
from bokeh.tile_providers import get_provider, Vendors
from bokeh.io import show
from bokeh.palettes import viridis
from pyproj import Transformer
import pandas as pd

# import data from csv
data = pd.read_csv('scripts/dwd_stations.csv')

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
