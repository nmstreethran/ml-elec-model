Data extraction
===============

Electricity system data from the ENTSO-E Transparency Platform
--------------------------------------------------------------

The :term:`ENTSO-E TP`\  [ENTSO-Ef]_ has a dashboard with various electricity system data tables and visualisations available to the public. All users must first accept the platform's terms and conditions and privacy policy [ENTSO-Eg]_ before gaining access to the dashboard. However, in order to export datasets in various formats (such as ``.csv`` and ``.xml``), as well as gain additional functionalities, it is required to register for a free account\  [4]_ on :term:`ENTSO-E TP`\. :term:`ENTSO-E TP`\'s Restful application programming interface (:term:`API`\) can then be used to automate the data extraction process (see the :term:`API`\  implementation [ENTSO-E2016]_ and user guides [ENTSO-E]_ for more info). Once a free account has been created, request for a security token to access the :term:`API`\  by sending an email to the :term:`ENTSO-E TP`\  Helpdesk (transparency at entsoe dot eu), stating 'Restful :term:`API`\  access' in the subject and the email address used to register for the account. Once granted, the security token can be viewed via account settings.

.. [4] https://transparency.entsoe.eu/usrm/user/createPublicUser

The :term:`ENTSO-E`\  :term:`API`\  Python client [EnergieID2019]_ is used to easily query the required data and return them as Pandas dataframes or series. The queries for generation and installed generation capacity per unit return dataframes, while the query for load returns a series.
``scripts/entsoe-api.py`` is the script used to perform this.

.. code:: py

    import pandas as pd
    from entsoe import EntsoePandasClient
    from entsoe.mappings import DOMAIN_MAPPINGS, BIDDING_ZONES
    # combine domain and bidding zone keys and values into the
    # DOMAIN_MAPPINGS dictionary
    DOMAIN_MAPPINGS.update(BIDDING_ZONES)

The bidding zones in Europe, mapped to their corresponding Energy Identification Codes (:term:`EIC`\s) [ENTSO-Ed]_ as shown in the table below, are used when querying using the Pandas client. Note that ``DE-LU`` only works for timestamps starting 01/10/2018 [ENTSO-Ee]_. Use ``DE-AT-LU`` for timestamps prior to this date.

.. table:: Bidding zones in Europe and their corresponding EICs.

    =================================== ================ ================
    **Zone name**                       **Bidding zone** **EIC**
    =================================== ================ ================
    Albania                             AL               10YAL-KESH—–5
    Belgium                             BE               10YBE———-2
    Bosnia and Herzegovina              BA               10YBA-JPCC—–D
    Bulgaria                            BG               10YCA-BULGARIA-R
    Switzerland                         CH               10YCH-SWISSGRIDZ
    Cyprus                              CY               10YCY-1001A0003J
    Czech Republic                      CZ               10YCZ-CEPS—–N
    Germany and Luxembourg              DE-LU            10Y1001A1001A82H
    Western Denmark                     DK-1             10YDK-1——–W
    Eastern Denmark                     DK-2             10YDK-2——–M
    Estonia                             EE               10Y1001A1001A39I
    Spain                               ES               10YES-REE——0
    Finland                             FI               10YFI-1——–U
    France                              FR               10YFR-RTE——C
    Georgia                             GE              
    Great Britain                       GB               10YGB———-A
    Greece                              GR               10YGR-HTSO—–Y
    Croatia                             HR               10YHR-HEP——M
    Hungary                             HU               10YHU-MAVIR—-U
    Ireland (Single Electricity Market) IE-SEM           10Y1001A1001A59C
    Centre-North, Italy                 IT-CNOR          10Y1001A1001A70O
    Centre-South, Italy                 IT-CSUD          10Y1001A1001A71M
    North, Italy                        IT-NORTH         10Y1001A1001A73I
    Sardinia, Italy                     IT-Sardinia      10Y1001A1001A74G
    Sicily, Italy                       IT-Sicily        10Y1001A1001A75E
    South, Italy                        IT-SUD           10Y1001A1001A788
    Lithuania                           LT               10YLT-1001A0008Q
    Latvia                              LV               10YLV-1001A00074
    Moldova                             MD              
    Montenegro                          ME               10YCS-CG-TSO—S
    North Macedonia                     MK               10YMK-MEPSO—-8
    Netherlands                         NL               10YNL———-L
    Oslo, Norway                        NO-1             10YNO-1——–2
    Kristiansand, Norway                NO-2             10YNO-2——–T
    Trondheim and Molde, Norway         NO-3             10YNO-3——–J
    Tromsø, Norway                      NO-4             10YNO-4——–9
    Bergen, Norway                      NO-5             10Y1001A1001A48H
    Poland                              PL               10YPL-AREA—–S
    Portugal                            PT               10YPT-REN——W
    Romania                             RO               10YRO-TEL——P
    Serbia                              RS               10YCS-SERBIATSOV
    Luleå, Sweden                       SE-1             10Y1001A1001A44P
    Sundsvall, Sweden                   SE-2             10Y1001A1001A45N
    Stockholm, Sweden                   SE-3             10Y1001A1001A46L
    Malmö, Sweden                       SE-4             10Y1001A1001A47
    Slovenia                            SI               10YSI-ELES—–O
    Slovakia                            SK               10YSK-SEPS—–K
    Ukraine                             UA               10YUA-WEPS—–0
    =================================== ================ ================

Generation data
~~~~~~~~~~~~~~~

:term:`ENTSO-E TP`\  aggregates data by following electricity production types [ENTSO-Eb]_:

- Biomass
- Fossil brown coal/lignite
- Fossil gas
- Fossil hard coal
- Fossil oil
- Geothermal
- Hydro pumped storage
- Hydro run-of-river and poundage
- Hydro water reservoir
- Nuclear
- Other
- Other renewable
- Solar
- Waste
- Wind offshore
- Wind onshore

The actual generation per production type dataset is the actual net electricity generation output in MW, aggregated by production type for each bidding zone per market time unit. These are available at different resolutions depending on the country, which is summarised below.

Temporal resolution of actual generation per production type dataset by country:

- 15 minutes: AT, DE, HU, LU, NL
- 30 minutes: CY, IE, UK
- 1 hour: BA, BE, BG, CH, CZ, DK, EE, ES, FI, FR, GE, GR, HR, IT, LT, LV, ME, MK, NO, PL, PT, RO, RS, SE, SI, SK

Each data point represents the average of all available instantaneous net generation output values on each market time unit. The values are estimated if unknown. The actual outputs of small-scale generating units may be estimated if there are no real-time measurements from these units. The data are published on :term:`ENTSO-E TP`\  no later than one hour after the operational period.

The installed capacity per production unit dataset contains information about production units (existing and planned) with an installed generation capacity of at least 100 MW, which includes the following:

- unit name
- code
- installed net generation capacity (MW)
- voltage connection level (kV)
- bidding zone (denoted using :term:`EIC`\s)
- production type (e.g., fossil gas, wind offshore)

This information is published annually on :term:`ENTSO-E TP`\  at the start of the year and is valid for the three following years.

Load data
~~~~~~~~~

This dataset represents the actual total load in MW per bidding zone per market time unit. These are available at different resolutions depending on the country, which is summarised in below.

Temporal resolution of electricity load dataset by country:

- 15 minutes: AL, BE, DE, HU, LU, NL
- 30 minutes: CY, IE, UK
- 1 hour: AT, BA, BG, CH, CZ, DK, EE, ES, FI, FR, GE, GR, HR, IT, LT, LV, MD, ME, MK, NO, PL, PT, RO, RS, SI, SK, SE, UA

The total load is defined as equal to the sum of power generated by plants on both :term:`TSO`\  and :term:`DNO`\  networks, from which the following are deduced:

- the balance (export-import) of exchanges on interconnections between neighbouring bidding zones
- the power absorbed by energy storage resources

The load is calculated using the average of real-time load values per bidding zone per market time unit.

.. code:: md

    Actual total load (including losses without stored energy)
    = Net generation – Exports + Imports – Absorbed energy

For these calculations, the net generation is preferred. However, gross generation may be used if it is available with the better precision. The :term:`TSO`\s responsible for each area decide whether to use gross or net generation, but they are required to keep their choice consistent per bidding zone. Absorbed energy is also provided as separate information with the aggregated generation output of the hydro pumped storage. The physical flow on the tie line is measured as agreed by neighbouring :term:`TSO`\s or bidding zones, where applicable. This dataset is published on :term:`ENTSO-E TP`\  no later than one hour after the end of the operating period.

Day-ahead market prices data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The day-ahead prices are published for each bidding zone at every market time unit, in the relevant currency per MWh. It is published no later than an hour after gate closure. In case of implicit allocation, the gate closure time is interpreted as the output time of the matching algorithms. The data is primarily owned and provided to the :term:`ENTSO-E TP`\  by power exchanges or :term:`TSO`\s. This dataset is available at hourly resolution.

Meteorological data
-------------------

German meteorological data from Deutscher Wetterdienst
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Weather data for Germany is extracted from :term:`DWD`\'s Climate Data Center (:term:`DWD CDC`\) OpenData [DWD]_. The data is subject to the server's terms of use [DWD18]_.

A map of German meteorological stations is shown below\  [5]_.

.. figure:: images/dwd_stations.png
    :alt: A map of German meteorological stations and their metadata, including the station's name, id and height (m), the state and NUTS 3 region it is located in, and its latitude and longitude, made using data from Deutscher Wetterdienst and Eurostat, and map tiles from OpenStreetMap.

    A map of German meteorological stations and their metadata, including the station's name, id and height (m), the state and NUTS 3 region it is located in, and its latitude and longitude, made using data from Deutscher Wetterdienst and Eurostat, and map tiles from OpenStreetMap.

.. [5] The interactive map can be viewed on JSFiddle: https://jsfiddle.net/nithiya/h3mnt20c/. See also the following link for a guide on how to plot the map using Bokeh: https://nithiya.gitlab.io/visualisations/mapping-geo-data-bokeh/.

``scripts/windHourly_de.py`` and ``scripts/solarHourly_de.py`` are the scripts used to extract hourly wind and solar data respectively.
