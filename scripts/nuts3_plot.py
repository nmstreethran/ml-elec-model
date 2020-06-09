"""Plotting NUTS 3 boundaries for focus countries

This script executes nuts3.py to obtain nomenclature of territorial units
for statistics (NUTS) data at level 3 from Eurostat for the following
countries: DE, DK, NO, and SE. It then creates a plot of the
these boundaries.
"""

# import libraries
from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource, CategoricalColorMapper
from bokeh.plotting import figure
from bokeh.palettes import viridis
from bokeh.tile_providers import get_provider, Vendors
from bokeh.embed import components
import matplotlib as mpl
import matplotlib.pyplot as plt

# import data
from nuts3 import nuts3

# convert to Web Mercator projection
nuts3 = nuts3.to_crs(crs='EPSG:3857')

# ## Bokeh plot
# load data source
geo_source = GeoJSONDataSource(geojson=nuts3.to_json())

# generate unique colours for each country
countries = list(set(nuts3['CNTR_CODE']))
palette = viridis(len(countries))
color_map = CategoricalColorMapper(factors=countries, palette=palette)

# define map tooltips
TOOLTIPS = [('NUTS', '@NUTS_ID: @NUTS_NAME')]

# set figure title, tooltips and axis types
# set axis types to mercator so that latitudes and longitudes are used
# in the figure
p = figure(title='NUTS 3 boundaries. Data: Eurostat.',
    tooltips=TOOLTIPS, x_axis_type='mercator', y_axis_type='mercator')

# set OpenStreetMap / CartoDB overlay
p.add_tile(get_provider(Vendors.CARTODBPOSITRON_RETINA))

# add data and configure plot
p.patches('xs', 'ys',
    fill_color={'field': 'CNTR_CODE', 'transform': color_map},
    source=geo_source, line_color='white', line_width=.5)

# # output the map and save to a custom path
# output_file('charts/nuts/nuts_plot.html')
# open the map
show(p)

# # to export script and div components
# script, div = components(p)
# # remove script HTML tags to save as JavaScript file
# script = script.replace('<script type="text/javascript">', '')
# script = script.replace('</script>', '')

# # export script as JavaScript file
# with open('charts/nuts/nuts.js', 'w') as f:
#     print(script, file=f)
# # export div as HTML file
# with open('charts/nuts/nuts-div.html', 'w') as f:
#     print(div, file=f)
# # export div as JavaScript file
# # (so that it can be read by nuts.html)
# with open('charts/nuts/nuts-div.js', 'w') as f:
#     print('document.write(`' + div + '\n`);', file=f)

# ## Matplotlib plot
mpl.rcParams['font.sans-serif'] = ['Lato', 'sans-serif']
fig, ax = plt.subplots(1, figsize=(10, 10))
nuts3.plot(column='CNTR_CODE', ax=ax, legend=True, cmap='viridis',
    legend_kwds={'bbox_to_anchor': (0, 0, .99, .13)})
plt.ylabel('Latitude (Web Mercator)')
plt.xlabel('Longitude (Web Mercator)')
