"""Plotting NUTS 0 boundaries for focus countries and interconnections

This script plots nomenclature of territorial units
for statistics (NUTS) data at level 0 (national borders) from Eurostat
(https://ec.europa.eu/eurostat/web/nuts/background) for the following
countries: DE, DK, NO, and SE, AT, CH, CZ, FI, LT, LU, NL, PL.
"""

# import libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
import geopandas as gpd

# import data
nuts0 = gpd.read_file('scripts/nuts0.geojson')

# convert to Web Mercator projection
nuts0 = nuts0.to_crs(crs='EPSG:3857')

# plot styles
plt.style.use('seaborn')
mpl.rcParams['font.sans-serif'] = ['Lato', 'sans-serif']

# configure plot
fig, ax = plt.subplots(1, figsize=(15, 15))
nuts0.plot(column='CNTR_CODE', ax=ax, legend=True, cmap='viridis',
    legend_kwds={'loc': 'lower right'})
plt.ylabel('Latitude (Web Mercator)')
plt.xlabel('Longitude (Web Mercator)')
plt.show()
