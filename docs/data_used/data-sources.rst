Data sources
============

Data repository: https://gitlab.com/nithiya/ml-elec-model-data

Unless otherwise stated, CSV datasets use UTF-8 character encoding, ``.`` for decimals, and ``,`` as the separator.

Geography
---------

Polygons
~~~~~~~~

Bidding zone polygons
`````````````````````

``data/geography/polygons/bidding_zones.geojson``

**Last download date: 10.07.2020**

This file contains polygons representing the following bidding zones, which are derived from nomenclature of territorial units for statistics (:term:`NUTS`) 2016 level 0 regions:

- Switzerland (CH)
- Czech Republic (CZ)
- Germany, Austria, and Luxembourg (DE-AT-LU)
- the Netherlands (NL)
- Poland (PL)

For France (FR), :term:`NUTS` 2016 level 1 regions were obtained and merged in order to exclude France's overseas territories from the bidding zone polygon.

It also contains polygons representing the Eastern Denmark (DK-2) and Western Denmark (DK-1) bidding zones, which are derived from :term:`NUTS` 2016 level 2 regions.

Polygons approximately representing bidding zones in Sweden are from `Tomorrow's electricityMap <https://github.com/tmrowco/electricitymap-contrib>`__'s `third-party maps <https://github.com/tmrowco/electricitymap-contrib/tree/master/web/third_party_maps>`__. These polygons were originally derived from `Natomraden.se <https://www.natomraden.se/>`__.

It is created by running the Python script ``scripts/zones.py``. The script parses the following datasets:

- from `Eurostat <https://gisco-services.ec.europa.eu/distribution/v2/nuts/nuts-2016-files.html>`__:
   - NUTS_RG_01M_2016_4326_LEVL_0.geojson
   - NUTS_RG_01M_2016_4326_LEVL_1.geojson
   - NUTS_RG_01M_2016_4326_LEVL_2.geojson
- from `Tomorrow's electricityMap <https://github.com/tmrowco/electricitymap-contrib/tree/master/web/third_party_maps>`__:
   - SE-SE1.json
   - SE-SE2.json
   - SE-SE3.json
   - SE-SE4.json

Country polygons
````````````````

``data/geography/polygons/countries.geojson``

**Last download date: 05.07.2020**

This file contains polygons for the following countries based on :term:`NUTS` 2016 regions:

- Austria
- Switzerland
- Czech Republic
- Germany
- Denmark
- France - excluding overseas territories
- Luxembourg
- the Netherlands
- Poland
- Sweden

It is created by running the Python script ``scripts/countries.py``. The script parses the following dataset from `Eurostat <https://gisco-services.ec.europa.eu/distribution/v2/nuts/nuts-2016-files.html>`__:

- NUTS_RG_01M_2016_4326_LEVL_0.geojson
- NUTS_RG_01M_2016_4326_LEVL_1.geojson

Metadata
````````

Complete metadata is in the `metadata.pdf <https://gisco-services.ec.europa.eu/distribution/v2/nuts/nuts-2016-metadata.pdf>`__ file. See also the `Eurostat website <https://ec.europa.eu/eurostat/web/nuts/background>`__.

**File naming**

pattern: theme_spatilatype_resolution_year_projection_subset.format

example: NUTS_RG_01M_2016_4326_LEVL_0.geojson

theme: 4-character code of theme (NUTS)

spatialtype: RG: regions (multipolygons)

resolution: 01M; map scale the data is optimized (generalised) for.

year: the year of :term:`NUTS` regulation (2016). See https://ec.europa.eu/eurostat/web/nuts/history.

projection: 4-digit EPSG code, see https://spatialreference.org/ref/epsg/.

- EPSG:4326 (WGS84, coordinates in decimal degrees)

subset: one of :term:`NUTS` levels

- LEVL_0: :term:`NUTS` level 0 (countries)
- LEVL_1: :term:`NUTS` level 1
- LEVL_2: :term:`NUTS` level 2
- LEVL_3: :term:`NUTS` level 3

Each subset makes complete coverage (RG data).
No subset code - all :term:`NUTS` levels are in the same file. It means quadruple coverage (RG data); any point hits 4 (or 0) polygons.

format: ``.geojson`` (https://geojson.org)

License and copyright information
`````````````````````````````````

NUTS 2016
+++++++++

© European Union, 1995 - today

Eurostat has a policy of encouraging free re-use of its data, both for non-commercial and commercial purposes. All statistical data, metadata, content of web pages or other dissemination tools, official publications and other documents published on its website, with the exceptions listed below, can be reused without any payment or written licence provided that:

- the source is indicated as Eurostat;
- when re-use involves modifications to the data or text, this must be stated clearly to the end user of the information.

In addition to the general copyright and licence policy applicable to the whole Eurostat website, the following specific provisions apply to the Administrative units / Statistical units datasets downloaded. The download and usage of these data is subject to the acceptance of the following clauses:

- The Commission agrees to grant the non-exclusive and not transferable right to use and process the Eurostat/GISCO geographical data downloaded from this page (the "data").
- The permission to use the data is granted on condition that: (1) the data will not be used for commercial purposes; (2) the source will be acknowledged. A copyright notice, as specified below, will have to be visible on any printed or electronic publication using the data downloaded from this page.
- Data source will have to be acknowledged in the legend of the map and in the introductory page of the publication with the following copyright notice: **© EuroGeographics for the administrative boundaries**.

electricityMap
++++++++++++++

electricityMap by Tomorrow is licensed under the terms of the `MIT License <https://opensource.org/licenses/MIT>`__.

References
``````````

- `NUTS 2016 release notes <https://gisco-services.ec.europa.eu/distribution/v2/nuts/nuts-2016-release-notes.txt>`__
- `GISCO data distribution API <https://gisco-services.ec.europa.eu/distribution/v2/nuts/>`__
- `Eurostat copyright notice and free re-use of data <https://ec.europa.eu/eurostat/about/policies/copyright>`__
- `Administrative units / Statistical units download provisions <https://ec.europa.eu/eurostat/web/gisco/geodata/reference-data/administrative-units-statistical-units>`__

Postal codes
~~~~~~~~~~~~

``data/geography/postcodes/postcodesDE.csv`` is a CSV file containing German postcodes, which is created by running the Python script ``scripts/postcodes.py``. This script downloads data from the `GeoNames Postal Code dataset <https://www.geonames.org/postal-codes/>`__.

License
```````

**The following descriptions are derived from the readme file obtained during download.**

This readme describes the GeoNames Postal Code dataset.
The main GeoNames gazetteer data extract is here: https://download.geonames.org/export/dump/.

This work is licensed under a Creative Commons Attribution 3.0 License.
This means you can use the dump as long as you give credit to geonames (a link on your website to www.geonames.org is ok).
See https://creativecommons.org/licenses/by/3.0/.

For many countries, latitudes and longitudes are determined with an algorithm that searches the place names in the main geonames database
using administrative divisions and numerical vicinity of the postal codes as factors in the disambiguation of place names.

For postal codes and place name for which no corresponding toponym in the main geonames database could be found an average
latitudes and longitudes of 'neighbouring' postal codes is calculated.

Please let GeoNames know if you find any errors in the data set.

The data format is tab-delimited text in UTF-8 encoding, with the following fields:

- postal_code: varchar(20)
- place_name: varchar(180)
- admin_name1: 1. order subdivision (state) varchar(100)
- admin_code1: 1. order subdivision (state) varchar(20)
- admin_name2: 2. order subdivision (county/province) varchar(100)
- admin_code2: 2. order subdivision (county/province) varchar(20)
- admin_name3: 3. order subdivision (community) varchar(100)
- admin_code3: 3. order subdivision (community) varchar(20)
- latitude: estimated latitude (wgs84)
- longitude: estimated longitude (wgs84)
- accuracy: accuracy of latitudes and longitudes from 1=estimated, 4=geonameid, 6=centroid of addresses or shape

Meteorology
-----------

Data downloaded from the Deutscher Wetterdienst (:term:`DWD`; German meteorological service) `Climate Data Center <https://opendata.dwd.de/climate_environment/CDC/>`__ (:term:`CDC`).

**The period of data used is 01.01.2018 - 01.07.2018**

List of stations
~~~~~~~~~~~~~~~~

**Last download date: 01.09.2020**

The file named ``data/meteorology/stations.csv`` contains the list of meteorological stations in Germany for each observation type obtained by running the Python script ``scripts/met_stations.py``.

Translations
````````````

Since the official data is in German, some translations are made.

Column names for lists of meteorological stations:

- Stations_id: station_id
- von_datum: start_date
- bis_datum: end_date
- Stationshoehe: station_height
- geoBreite: latitude
- geoLaenge: longitude
- Stationsname: station_name
- Bundesland: state

Wind
~~~~

**Last download date: 01.09.2020**

Files in the ``data/meteorology/wind`` directory contains historical hourly station observations of wind speed and wind direction for Germany. These files are obtained by running the Python script ``scripts/met_data.py``.

See https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/wind/historical/DESCRIPTION_obsgermany_climate_hourly_wind_historical_en.pdf for the full description. Accessed version (version v006, 2018) was last edited on 19.12.2018.

The file comprises following parameters:

- STATIONS_ID: station identification number
- MESS_DATUM_ENDE: end of measurement interval (yyyymmddhh)
- QN_3: quality level of next columns; coding see paragraph "Quality information"
- F: mean wind speed (m/s)
- D: mean wind direction (Grad)
- eor: end of record; can be ignored

with missing values are marked as -999. The definition of measurement time changed over time and referred to time units MOZ, MEZ or UTC (see the station specific Metadaten_Parameter* for the exact definition). Nowadays, hourly wind speed and wind direction is given as the average of the six 10 min intervals measured in the previous hour (e.g., at UTC 11, the average wind speed and average wind direction during UTC 10 - UTC 11 is given).

License and copyright
~~~~~~~~~~~~~~~~~~~~~

**Terms of use for data on the CDC ftp server**

**Please note:** This `English translation <https://opendata.dwd.de/climate_environment/CDC/Terms_of_use.pdf>`__ is intended as a convenience to non-German-reading customers and has no legal effect for compliance or enforcement purposes. Only the `German version <https://opendata.dwd.de/climate_environment/CDC/Nutzungsbedingungen_German.pdf>`__ shall be legally binding.

**All data in the freely accessible area of the CDC's ftp server are protected by copyright.**

The freely accessible data may be re-used without any restrictions provided that the source reference is indicated, as laid down in the GeoNutzV ordinance ("Verordnung zur Festlegung der Nutzungsbestimmungen für die Bereitstellung von Geodaten des Bundes = Ordinance to Determine the Conditions for Use for the Provision of Spatial Data of the Federation). As to the layout of source references, the :term:`DWD` requests adherence to the following guidelines (cf. § 7 of the :term:`DWD` Law and § 3 of the GeoNutzV ordinance):

- The obligation to indicate the enclosed source references shall apply to any spatial data and other services of the :term:`DWD` that are used without alteration. Source references must also be indicated even if extracts or excerpts are used or if the data format has been changed. Displaying the :term:`DWD` logo shall be considered as meeting the requirement of source reference in meaning of the GeoNutzV ordinance.
- In the event of more advanced alteration, processing, new design or other adaptation, :term:`DWD` at least expects to be mentioned in a central list of references or in an imprint.
- Indication of alteration according to the GeoNutzV ordinance may read as follows: "Data basis: Deutscher Wetterdienst, gridded data reproduced graphically"; "Data basis: Deutscher Wetterdienst, averaged over individual values", or "Data basis: Deutscher Wetterdienst, own elements added".
- If a service provided by the :term:`DWD` is used in a way that does not comply with its intended purpose, the enclosed source references have to be deleted. This shall especially apply to weather warnings for which there is no guarantee that they are delivered to all users at all times completely and without delay.

You will find corresponding explanations and templates for the implementation under: https://www.dwd.de/EN/service/copyright/templates_dwd_as_source.html.

Wherever data or information from third parties is used for the generation of :term:`DWD`-own products and services, the Deutscher Wetterdienst assures that it holds all necessary rights to do so.

Source of geospatial base data: Surveying authorities of the Länder and Federal Agency for Cartography and Geodesy (https://www.bkg.bund.de).

Source of satellite data: EUMETSAT (https://www.eumetsat.int), NOAA (https://www.noaa.gov).

**Please ensure the copyright conditions stated in the data set descriptions are met.**

Power system
------------

Renewable power generators
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Last download date: 02.07.2020**

The script ``scripts/rpp.py`` is used to extract and translate the following data.

The following information is obtained from this site and roughly translated into English: https://www.netztransparenz.de/EEG/Anlagenstammdaten.

Netztransparenz - Erneuerbare-Energien-Gesetz (EEG, which roughly translates to Renewable Energy Sources Act) plant data: EEG system master data for the 2018 annual accounts.

The system master data reported to the transmission system operator by the network operators, who are obliged to purchase and pay for it, as part of the 2018 EEG annual accounts, are available for download as a file.

The file contains the master data of all EEG systems that were reported by the DSOs to the TSOs as part of the 2018 EEG annual report. This can lead to decommissioning during the year as well as to network transitions between two network operators, which results in double mentioning of the system key. In general, the master data reflects the status as of December 31, 2018 or the day of decommissioning or network exit.

The files also include the systems connected directly or indirectly to the transmission system operators' networks. For data protection reasons, the street and house number are not given for systems with an installed output of less than 30 kW.

Datasets are available for each transmission system operator (TSO):

- 50Hertz Transmission
- Amprion
- TenneT TSO
- TransnetBW

These were extracted, translated, combined, and saved into the following datasets, grouped by energy carrier:

- Onshore wind and offshore wind: ``data/power/installed/wind.csv``

Based on these, and the postal code and meteorological datasets, the following files were created, which includes the approximate geographical location of power plants aggregated by postal code and their closest meteorological station:

- Onshore wind and offshore wind: ``data/power/installed/wind_agg.csv``

The script ``scripts/rpp_agg.py`` is used to create the data above.

Translations
````````````

Since the official data is in German, some translations are made.

Column names:

- EEG_Anlagenschluessel: EEG_plant_key
- NB_BNR: NB_BNR
- Netzbetreiber: network_operator
- Straße_Flurstueck: address
- PLZ: postal_code
- Ort_Gemarkung: city_district
- Gemeindeschluessel: municipality_key
- Bundesland: state
- Installierte_Leistung: installed_capacity (kW)
- Energietraeger: energy_carrier
- Einspeisespannungsebene: feed_in_voltage_level
- Leistungsmessung: power_measurement
- Regelbarkeit: controllability
- Inbetriebnahme: commissioning
- Ausserbetriebnahme: decommissioning
- Netzzugang: network_connection
- Netzabgang: network_disconnection

Energy carriers:

- Wasser: hydro
- Biomasse: biomass
- Wind an Land: onshore wind
- Deponiegas: landfill gas
- Wind auf See: offshore wind
- Klärgas: sewage gas
- Geothermie: geothermal
- Grubengas: mine gas

Power measurement:

- Nein: no
- Ja: yes

State:

- Ausschließliche Wirtschaftszone: exclusive economic zone
- Ausland: foreign country

Controllability:

- nicht regelbar: not adjustable
- 70 % Begrenzung: 70 % limit
- regelbar n. § 9 Abs. 2 EEG: adjustable according to § 9 Abs. 2 EEG
- regelbar n. § 9 Abs. 1 EEG: adjustable according to § 9 Abs. 1 EEG

Feed-in voltage level (TBD):

- NS
- MS
- MS/NS
- HöS
- HS
- HS/MS
- HöS/HS

ENTSO-E Transparency Platform data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The script ``scripts/entsoe_data.py`` is used to extract the following data from the European Network of Transmission Systems Operators for Electricity Transparency Platform (:term:`ENTSO-E TP`).

The `ENTSO-E TP <https://transparency.entsoe.eu/>`__ has a dashboard with various electricity system data tables and visualisations available to the public. The **list of data available for free re-use** is `available on the website <https://transparency.entsoe.eu/content/static_content/download?path=/Static%20content/terms%20and%20conditions/191025_List_of_Data_available_for_reuse_v2_cln.pdf>`__. All users must first accept the platform's `terms and conditions and privacy policy <https://transparency.entsoe.eu/content/static_content/Static%20content/terms%20and%20conditions/terms%20and%20conditions.html>`__ before gaining access to the dashboard. However, in order to export datasets in various formats (such as CSV and XML), as well as gain additional functionalities, it is required to `register for a free account <https://transparency.entsoe.eu/usrm/user/createPublicUser>`__ on the :term:`ENTSO-E TP`. The :term:`ENTSO-E TP`'s Restful application programming interface (:term:`API`) can then be used to automate the data extraction process (see the `API implementation <https://transparency.entsoe.eu/content/static_content/download?path=/Static%20content/web%20api/RestfulAPI_IG.pdf>`__ and `user guides <https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html>`__ for more info). Once a free account has been created, request for a security token to access the :term:`API` by sending an email to the :term:`ENTSO-E TP` Helpdesk (transparency at entsoe dot eu), stating 'Restful :term:`API` access' in the subject and the email address used to register for the account. Once granted, the security token can be viewed via account settings.

The `ENTSO-E API Python client (entsoe-py) <https://github.com/EnergieID/entsoe-py>`__ is used to easily query the required data and return them as pandas dataframes or series. The queries for generation and installed generation capacity per unit return dataframes, while the query for load returns a series.

The bidding zones in Germany and its interconnections, mapped to their corresponding `Energy Identification Codes <https://www.entsoe.eu/data/energy-identification-codes-eic/>`__ (:term:`EIC`\s) are used when querying using the pandas client.

**Note:** Note that ``DE-LU`` only works for timestamps starting 01.10.2018. Use `DE-AT-LU` for timestamps prior to this date. (`More info. <https://transparency.entsoe.eu/news/widget?id=5b7c1e9b5092e75a10bab903>`__) Since this project is focussing on the first half of 2018, ``DE-AT-LU`` is used.

Installed generation capacity
`````````````````````````````

**Last download date: 10.07.2020**

Installed generation capacity grouped by generation technology in the DE-AT-LU bidding zone between 01.01.2018 and 01.07.2018: ``installed_generation_capacity_DE-AT-LU.csv``

Generation
``````````

**Last download date: 10.07.2020**

- Time series of 15-minute electricity generation grouped by generation technology in the DE-AT-LU bidding zone between 01.01.2018 and 01.07.2018: ``data/power/generation/generation_DE-AT-LU.csv``
- Time series of day-ahead hourly electricity generation forecast in the DE-AT-LU bidding zone between 01.01.2018 and 01.07.2018: ``data/power/generation/generation_forecast_DE-AT-LU.csv``
- Time series of day-ahead 15-minute electricity generation forecast grouped by generation technology (solar, offshore wind, onshore wind) in the DE-AT-LU bidding zone between 01.01.2018 and 01.07.2018: ``data/power/generation/wind_and_solar_forecast_DE-AT-LU.csv``

Prices
``````

**Last download date: 10.07.2020**

Time series of day-ahead hourly electricity market prices in the DE-AT-LU bidding zone between 01.01.2018 and 01.07.2018: ``data/power/prices/day_ahead_prices_DE-AT-LU.csv``

Load
````

**Last download date: 10.07.2020**

- Time series of 15-minute electricity load in the DE-AT-LU bidding zone between 01.01.2018 and 01.07.2018: ``data/power/load/load_DE-AT-LU.csv``
- Time series of 15-minute electricity load forecast in the DE-AT-LU bidding zone between 01.01.2018 and 01.07.2018: ``data/power/load/load_forecast_DE-AT-LU.csv``
