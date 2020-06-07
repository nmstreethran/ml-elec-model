"""Plotting NUTS 3 boundaries for BE, DE, DK, NL, NO, SE, UK

This script executes nuts.py to obtain nomenclature of territorial units
for statistics (NUTS) data at level 3 from Eurostat for the following
countries: BE, DE, DK, NL, NO, SE, UK. It then creates a plot of the
these boundaries.
"""

# import libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
# import contextily as ctx

# import data
from nuts import nuts3

# convert to Web Mercator projection
nuts3 = nuts3.to_crs(crs='EPSG:3857')

# plot the territories
mpl.rcParams['font.sans-serif'] = ['Lato', 'sans-serif']
fig, ax = plt.subplots(1, figsize=(5, 9.5))
nuts3.plot(column='CNTR_CODE', ax=ax, legend=True, cmap='viridis',
    legend_kwds={'bbox_to_anchor': (0, 0, .99, .33)})
plt.ylabel('Latitude (Web Mercator)')
plt.xlabel('Longitude (Web Mercator)')
# ctx.add_basemap(ax, crs=bzn.crs.to_string())
