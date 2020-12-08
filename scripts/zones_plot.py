"""Plotting bidding zones for DE and its interconnections

This script plots approximate SE electricity market bidding zones
from Tomorrow's electricityMap
(https://github.com/tmrowco/electricitymap-contrib), and bidding zones for
DE, AT, CH, CZ, DK, FR, LU, NL, PL using nomenclature of territorial units
for statistics (NUTS) data from Eurostat
(https://ec.europa.eu/eurostat/web/nuts/background).
"""

# import libraries
import geopandas as gpd
import matplotlib as mpl
import matplotlib.pyplot as plt

# import data
zones = gpd.read_file(
    'https://gitlab.com/api/v4/projects/19753809/repository/files/' +
    'geography%2Fpolygons%2Fbidding%5Fzones%2Egeojson/raw?ref=master')

# plot styles
plt.style.use('seaborn')
mpl.rcParams['font.sans-serif'] = ['Lato', 'sans-serif']

# configure plot
fig, ax = plt.subplots(1, figsize=(13, 13))
zones.plot(
    column='zone', ax=ax, legend=True, cmap='viridis',
    legend_kwds={'loc': 'lower right'})
plt.ylabel('Latitude')
plt.xlabel('Longitude')
plt.show()

"""Bokeh plot

from bokeh.io import show
from bokeh.models import GeoJSONDataSource, CategoricalColorMapper, Plot
from bokeh.plotting import figure
from bokeh.palettes import viridis

# load data source
geo_source = GeoJSONDataSource(geojson=zones.to_json())

# generate unique colours for each bidding zone
zoneList = list(zones['zone'])
palette = viridis(len(zoneList))
color_map = CategoricalColorMapper(factors=zoneList, palette=palette)

# define map tooltips
TOOLTIPS = [('Zone', '@zone'), ('(Lon, Lat)', '($x, $y)')]

# set output backend for the glyph API
p = Plot(output_backend='webgl')

# set figure tooltips and axis types
# set axis types to mercator so that latitudes and longitudes are used
# in the figure
# set output backend for the plotting API
p = figure(
    tooltips=TOOLTIPS, output_backend='webgl', sizing_mode='scale_width',
    plot_width=4, plot_height=6)

# hover settings
p.hover.point_policy = 'follow_mouse'

# add data and configure plot
p.patches(
    'xs', 'ys', fill_color={'field': 'zone', 'transform': color_map},
    source=geo_source, line_color='white', line_width=.5)

# open the map
show(p)
"""
