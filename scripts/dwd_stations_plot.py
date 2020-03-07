# %%
"""Plotting German weather station data

Weather data from Deutscher Wetterdienst (DWD)
Nomenclature of territorial units for statistics (NUTS) data
at level 3 from Eurostat
"""

# %%
# import libraries
from bokeh.models import ColumnDataSource, CategoricalColorMapper
from bokeh.plotting import figure
from bokeh.tile_providers import get_provider, Vendors
from bokeh.io import output_file, save
from bokeh.embed import components
from bokeh.palettes import viridis
from pyproj import Proj, transform
import pandas as pd
from os import path, system

# %%
# check if weather station data exists
if path.exists('data/dwd_stations_geo.csv') == False:
    system('python scripts/nuts_de.py')

# %%
# load the data
data = pd.read_csv('data/dwd_stations_geo.csv')

# %%
# transform latitudes and longitudes from wgs84 to web mercator projection
lons = tuple(data['longitude'])
lats = tuple(data['latitude'])
wgs84 = Proj('epsg:5243')
web = Proj('epsg:3857')
lons, lats = wgs84(lons, lats)
xm, ym = transform(wgs84, web, lons, lats)
data['mercator_x'] = xm
data['mercator_y'] = ym

# %%
# generate unique colours for each state
state = list(set(data['state']))
palette = viridis(len(state))
color_map = CategoricalColorMapper(factors=state,
    palette=palette)

# %%
# create dictionary of source data for geomap
geo_source = ColumnDataSource(data)

# %%
# define map tooltips
TOOLTIPS = [
    ('Station', '@name'), ('id', '@id'), ('Height (m)', '@height'),
    ('State', '@state'), ('NUTS 3', '@NUTS_ID: @NUTS_NAME'),
    ('(Lon, Lat)', '(@longitude, @latitude)')
]

# %%
# set figure title, tooltips and axis types
# set axis types to mercator so that latitudes and longitudes are used
# in the figure
p = figure(
    title='German Meteorological Stations. Data: DWD.de and Eurostat.',
    x_axis_type='mercator', y_axis_type='mercator', tooltips=TOOLTIPS)

# set openstreetmaps overlay
p.add_tile(get_provider(Vendors.CARTODBPOSITRON_RETINA))

# add data points
p.circle(source=geo_source, x='mercator_x', y='mercator_y',
    color={'field': 'state', 'transform': color_map})

# %%
# output the geomap
output_file('plots/dwd_stations.html')
save(p)

# %%
# to export script and div components
script, div = components(p)
# remove script html tags to save as js file
script = script.replace('<script type="text/javascript">', '')
script = script.replace('</script>', '')

# export script as js file
with open('plots/dwd_stations.js', 'w') as f:
    print(script, file=f)
# export div as html file
with open('plots/dwd_stations-div.html', 'w') as f:
    print(div, file=f)
