"""Plotting bidding zones for the focus countries and interconnections

This script executes zones_no_se.py to obtain approximate NO and SE
electricity market bidding zones from Electricity Map
(https://github.com/tmrowco/electricitymap-contrib), and zones.py to
obtain all other bidding zones using nomenclature of territorial units
for statistics (NUTS) data from Eurostat
(https://ec.europa.eu/eurostat/web/nuts/background). It then creates a
plot of the bidding zones.
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
from zones import zones

# convert to Web Mercator projection
zones = zones.to_crs(crs='EPSG:3857')

# ## Bokeh plot
# load data source
geo_source = GeoJSONDataSource(geojson=zones.to_json())

# generate unique colours for each bidding zone
zoneList = list(zones['zone'])
palette = viridis(len(zoneList))
color_map = CategoricalColorMapper(factors=zoneList, palette=palette)

# define map tooltips
TOOLTIPS = [('Zone', '@zone')]

# set figure title, tooltips and axis types
# set axis types to mercator so that latitudes and longitudes are used
# in the figure
p = figure(title='Bidding zones. Data: tmrowco, Eurostat.',
    tooltips=TOOLTIPS, x_axis_type='mercator', y_axis_type='mercator')

# set OpenStreetMap / CartoDB overlay
p.add_tile(get_provider(Vendors.CARTODBPOSITRON_RETINA))

# add data and configure plot
p.patches('xs', 'ys', fill_color={'field': 'zone', 'transform': color_map},
    source=geo_source, line_color='white', line_width=.5)

# open the map
show(p)

"""

# output the map and save to a custom path
output_file('charts/bidding_zones/zones_plot.html')

# to export script and div components
script, div = components(p)
# remove script HTML tags to save as JavaScript file
script = script.replace('<script type="text/javascript">', '')
script = script.replace('</script>', '')

# export script as JavaScript file
with open('charts/bidding_zones/zones.js', 'w') as f:
    print(script, file=f)
# export div as HTML file
with open('charts/bidding_zones/zones-div.html', 'w') as f:
    print(div, file=f)
# export div as JavaScript file
# (so that it can be read by zones.html)
with open('charts/bidding_zones/zones-div.js', 'w') as f:
    print('document.write(`' + div + '\n`);', file=f)
"""

# ## Matplotlib plot
# plot styles
plt.style.use('seaborn')
mpl.rcParams['font.sans-serif'] = ['Lato', 'sans-serif']

# configure plot
fig, ax = plt.subplots(1, figsize=(10, 10))
zones.plot(column='zone', ax=ax, legend=True, cmap='viridis',
    legend_kwds={'bbox_to_anchor': (0, 0, 1.27, .52)})
plt.ylabel('Latitude (Web Mercator)')
plt.xlabel('Longitude (Web Mercator)')
plt.show()
