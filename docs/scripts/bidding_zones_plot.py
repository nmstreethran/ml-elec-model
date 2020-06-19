"""Plotting bidding zones for the focus countries and interconnections

This script plots approximate NO and SE electricity market bidding zones
from Electricity Map (https://github.com/tmrowco/electricitymap-contrib),
and all other bidding zones using nomenclature of territorial units for
statistics (NUTS) data from Eurostat
(https://ec.europa.eu/eurostat/web/nuts/background).
"""

# import libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
import geopandas as gpd

# import data
zones = gpd.read_file('scripts/bidding_zones.geojson')

# convert to Web Mercator projection
zones = zones.to_crs(crs='EPSG:3857')

# plot styles
plt.style.use('seaborn')
mpl.rcParams['font.sans-serif'] = ['Lato', 'sans-serif']
mpl.rcParams['text.color'] = 'black'
mpl.rcParams['axes.labelcolor'] = 'black'

# configure plot
fig, ax = plt.subplots(1, figsize=(15, 15))
zones.plot(column='zone', ax=ax, legend=True, cmap='viridis',
    legend_kwds={'loc': 'lower right'})
plt.ylabel('Latitude (Web Mercator)')
plt.xlabel('Longitude (Web Mercator)')
plt.show()
