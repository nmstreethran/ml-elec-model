Meteorological data
===================

Germany
-------

Weather data for Germany is extracted from :term:`DWD`'s Climate Data Center (:term:`DWD CDC`) OpenData [DWD]_. The data is subject to the server's terms of use [DWD18]_.

A map of German meteorological stations is shown in the map below [#f5]_.

.. figure:: ../images/dwd_stations.png
   :alt: A map of German meteorological stations and their metadata, including the station's name, id and height (m), the state and NUTS 3 region it is located in, and its latitude and longitude, made using data from Deutscher Wetterdienst and Eurostat (© EuroGeographics for the administrative boundaries), and map tiles from OpenStreetMap / CartoDB.

   A map of German meteorological stations and their metadata, including the station's name, id and height (m), the state and NUTS 3 region it is located in, and its latitude and longitude, made using data from Deutscher Wetterdienst and Eurostat (© EuroGeographics for the administrative boundaries), and map tiles from OpenStreetMap / CartoDB.

.. CAUTION::
   The dwdweather2 Python package [panodata2020]_ can be used to access German weather data. However, it is a Python 2.7 library. The library's README states the following: *"This piece of software is in a very early stage. No test cases yet. Only tested with Python 3.6. Use at your own risk."* To avoid dependency issues, create a new virtual environment to install dwdweather2; **DO NOT** install it in the same environment used in this project.

   .. code:: sh

      # create and activate new virtual environment
      # ... and then install dwdweather2
      pip install dwdweather2

      # GeoJSON
      dwdweather stations --type geojson > dwd_stations.geojson

      # CSV
      dwdweather stations --type csv > dwd_stations.csv

.. rubric:: Footnotes

.. [#f5] The interactive map can be viewed on JSFiddle: https://jsfiddle.net/nithiya/h3mnt20c/. See also the following link for a guide on how to plot the map using Bokeh: https://nithiya.gitlab.io/visualisations/mapping-geo-data-bokeh/.
