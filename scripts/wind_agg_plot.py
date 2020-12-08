"""Plotting postcode-aggregated German wind power generator data

This script plots an interactive map of wind energy generators aggregated by
postal code in Germany. The tooltips show their approximate location, the
closest wind meteorological station, total installed capacity, and the
responsible transmission system operator.
Data sources:
- German Erneuerbare-Energien-Gesetz (EEG, which roughly translates to
    Renewable Energy Sources Act) power generator data from
    Netztransparenz.de (https://www.netztransparenz.de/EEG/Anlagenstammdaten)
- postcode and geo location data from GeoNames
    (https://download.geonames.org/export/zip/)
- meteorological station data from Deutscher Wetterdienst (DWD),
    Germany's meteorological service
    (https://www.dwd.de/EN/climate_environment/cdc/cdc_node.html)
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
    'power%2Finstalled%2Fwind%5Fagg%2Ecsv/raw?ref=master')

data = pd.read_csv(url, encoding='utf-8')

# transform latitudes and longitudes from WGS84 to Web Mercator projection
lons = tuple(data['longitude'])
lats = tuple(data['latitude'])
transformer = Transformer.from_crs('epsg:4326', 'epsg:3857', always_xy=True)
xm, ym = transformer.transform(lons, lats)
data['mercator_x'] = xm
data['mercator_y'] = ym

# fill missing values
data = data.fillna('?')

# rounding floats
data = data.round(
    {'latitude': 3, 'longitude': 3, 'accuracy': 3, 'met_lat': 3,
        'met_lon': 3, 'distance': 3, 'installed_capacity': 0})

# generate unique colours for each state
state = list(set(data['state']))
palette = viridis(len(state))
color_map = CategoricalColorMapper(factors=state, palette=palette)

# create dictionary of source data for the map
geo_source = ColumnDataSource(data)

# define map tooltips
TOOLTIPS = [
    ('Installed capacity (kW)', '@installed_capacity'),
    ('Location', '@postal_code, @city_district, @state'),
    ('(lon, lat, acc)', '(@longitude, @latitude, @accuracy)'),
    ('TSO', '@TSO'),
    ('Met station (lon, lat, diff)',
        '@station_id (@met_lon, @met_lat, @distance)')]

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
