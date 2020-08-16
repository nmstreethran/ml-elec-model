Aggregated data
===============

The following is an interactive map of wind energy generators aggregated by postal code in Germany. The tooltips show their approximate location, the closest wind meteorological station, total installed capacity, and the responsible transmission system operator.

.. bokeh-plot:: ../scripts/wind_agg_plot.py
   :source-position: none

The scripts ``scripts/rpp.py`` and ``scripts/rpp_agg.py`` are used to obtain the data used. ``scripts/wind_agg_plot.py`` is used to plot the above.

It is worth noting that the aggregated data omits power plants with no postal code information, and as a result, the approximate location could not be derived and the plant is not included in the plot. This applies mostly to offshore wind turbine installations.

Data sources:

- German Erneuerbare-Energien-Gesetz (EEG, which roughly translates to Renewable Energy Sources Act) power generator data from Netztransparenz.de (https://www.netztransparenz.de/EEG/Anlagenstammdaten)
- postcode and geo location data from GeoNames (https://download.geonames.org/export/zip/)
- meteorological station data from Deutscher Wetterdienst (DWD), Germany's meteorological service (https://www.dwd.de/EN/climate_environment/cdc/cdc_node.html)
