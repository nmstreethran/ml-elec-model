Regions
=======

In this section, the term 'focus countries' refers to four European countries: Germany, Denmark, Norway, and Sweden.

The table below lists countries that will be referred in this document, together with their country codes. Country codes are according to ISO_3166-1 alpha-2.

.. table:: Countries and country codes.

   +--------------+---------------------+----------------+
   | Country code | Country             | Focus country? |
   +==============+=====================+================+
   | AT           | Austria             |                |
   +--------------+---------------------+----------------+
   | CH           | Switzerland         |                |
   +--------------+---------------------+----------------+
   | CZ           | Czech Republic      |                |
   +--------------+---------------------+----------------+
   | DE           | Germany             | Yes            |
   +--------------+---------------------+----------------+
   | DK           | Denmark             | Yes            |
   +--------------+---------------------+----------------+
   | FI           | Finland             |                |
   +--------------+---------------------+----------------+
   | LT           | Lithuania           |                |
   +--------------+---------------------+----------------+
   | LU           | Luxembourg          |                |
   +--------------+---------------------+----------------+
   | NL           | Netherlands         |                |
   +--------------+---------------------+----------------+
   | NO           | Norway              | Yes            |
   +--------------+---------------------+----------------+
   | PL           | Poland              |                |
   +--------------+---------------------+----------------+
   | SE           | Sweden              | Yes            |
   +--------------+---------------------+----------------+

Territories
-----------

The nomenclature of territorial units for statistics (:term:`NUTS`) [Eurostat]_ classifies territorial units in Europe in different levels [Ofgem2014]_:

- :term:`NUTS` 0: country-level
- :term:`NUTS` 1: major socio-economic regions
- :term:`NUTS` 2: basic regions for the application of regional policies
- :term:`NUTS` 3: small regions for specific diagnoses

The map below illustrates NUTS 3 boundaries for the focus countries.

.. figure:: ../images/nuts3.png
   :alt: NUTS 3 boundaries for the focus countries. Data from Eurostat (© EuroGeographics for the administrative boundaries).

   NUTS 3 boundaries for the focus countries. Data from Eurostat (© EuroGeographics for the administrative boundaries).

Transmission system operators and interconnections
--------------------------------------------------

Europe has multiple :term:`TSO`\s [ENTSO-Ea]_ and cross-border interconnections. These are listed for the focus countries, along with bidding zones, in the table below.

.. table:: TSOs and cross-border interconnections in the focus countries. Data: European Network of Transmission System Operators for Electricity.

   +--------------------+--------------------+--------------------+--------------------+
   | Country            | TSOs               | Cross-border       | Bidding            |
   |                    |                    | interconnections   | zones              |
   +====================+====================+====================+====================+
   | DK                 | Energinet          | DE, NO, SE         | DK1, DK2           |
   +--------------------+--------------------+--------------------+--------------------+
   | DE                 | TransnetBW,        | AT, CH, CZ, DK,    | DE-LU              |
   |                    | TenneT TSO,        | FR, LU, NL, PL,    |                    |
   |                    | Amprion,           | SE                 |                    |
   |                    | 50Hertz            |                    |                    |
   |                    | Transmission       |                    |                    |
   +--------------------+--------------------+--------------------+--------------------+
   | NO                 | Statnett           | DK, FI, NL, SE     | NO1, NO2, NO3,     |
   |                    |                    |                    | NO4, NO5           |
   +--------------------+--------------------+--------------------+--------------------+
   | SE                 | Svenska            | DK, DE, FI, LT,    | SE1, SE2, SE3,     |
   |                    | Kraftnät           | NO, PL             | SE4                |
   +--------------------+--------------------+--------------------+--------------------+

Bidding zones
-------------

A bidding zone is the largest geographical area within which market participants are able to exchange energy without capacity allocation. There are three types of bidding zones:

1. national borders (e.g., Belgium or the Netherlands - majority of bidding zones in Europe
2. larger than national borders (e.g., Germany and Luxembourg)
3. smaller zones within individual countries (e.g., Norway or Sweden)

The table below lists bidding zones in focus countries and their interconnections by country and market operator [NordPool]_, [EPEXSPOT]_.

.. table:: Bidding zones and market operators in focus countries and their interconnections.

   +---------+-----------------+-----------------+
   | Country | Markets         | Zones           |
   +=========+=================+=================+
   | AT      |                 | AT              |
   +---------+-----------------+-----------------+
   | CH      |                 | CH              |
   +---------+-----------------+-----------------+
   | CZ      |                 | CZ              |
   +---------+-----------------+-----------------+
   | DE      | EEX, EPEX       | DE-LU           |
   +---------+-----------------+-----------------+
   | DK      | EEX, Nord Pool  | DK1, DK2        |
   +---------+-----------------+-----------------+
   | FI      |                 | FI              |
   +---------+-----------------+-----------------+
   | LT      |                 | LT              |
   +---------+-----------------+-----------------+
   | LU      |                 | DE-LU           |
   +---------+-----------------+-----------------+
   | NL      | APX             | NL              |
   +---------+-----------------+-----------------+
   | NO      | EEX, Nord Pool  | NO1, NO2, NO3,  |
   |         |                 | NO4, NO5        |
   +---------+-----------------+-----------------+
   | PL      |                 | PL              |
   +---------+-----------------+-----------------+
   | SE      | EEX, Nord Pool  | SE1, SE2, SE3,  |
   |         |                 | SE4             |
   +---------+-----------------+-----------------+

Prior to 01/10/2018, Germany was part of the DE-AT-LU bidding zone, together with Austria (AT) and Luxembourg (LU), which had split into the DE-LU and AT bidding zones, as reported by European Network of Transmission Systems Operators for Electricity (:term:`ENTSO-E`) below [ENTSO-Ee]_:

   *[...] DE-AT-LU bidding zone split on the 23rd of August. BZN|DE-AT-LU will be separated into 2 new bidding zones BZN|DE-LU and BZN|AT.*

   *New bidding zones will be active from the 1st of October, however, first data submissions, like month ahead forecasts, are expected from the 1st of September.*

   *Validity end date for BZN|DE-AT-LU is the end of September 2018. [...]*

Mapping bidding zones to :term:`NUTS` 3 territories is straightforward for DE, AT, CH, CZ, FI, LT, LU, NL, and PL (bidding zone type 1 for all except DE, which is type 2) -- all :term:`NUTS` 3 territories in these countries are part of the same bidding zone.

Denmark is both conveniently separated into two zones that are easily distinguishable. These are Western Denmark (:term:`NUTS` IDs with prefixes DK03-DK05) and Eastern Denmark (:term:`NUTS` IDs with prefixes DK01-DK02).

There is no clear indication of the bidding zone boundaries for Norway and Sweden, so some assumptions were made. Both countries have multiple smaller bidding zones (type 3) with flexible borders. This was done to optimise allocation of resources and reduce the overall price of electricity [EuropeanCommission2010]_. Norway has five zones and Sweden has four zones. By cross-referencing Nord Pool market data [NordPool]_, :term:`NUTS` 3 data and county maps of Norway and Sweden [Wikipedia2019]_, [Wikipedia2019a]_, the territories are split into the bidding zones as shown in the table below. Nord Pool associates each bidding zone with a major reference city in that zone. However, there were six cities for Norway instead of the expected five. Historical Nord Pool market data for Norway suggests that two cities, Trondheim and Molde, have had the same system price since 2003. The ELSPOT area change log also confirms that Trondheim and Molde are city references for the NO3 bidding zone [NordPoola]_. Therefore, these two cities are grouped into the same bidding zone, which also satisfies what the maps suggest.

.. table:: Bidding zones and their territories for Norway and Sweden, approximated based on Nord Pool market data, NUTS 3 data and county maps of Norway and Sweden.

   +-----------------+-----------------+-----------------+-----------------+
   | Bidding         | Reference       | Counties        | NUTS 3 IDs      |
   | zone            | cities          |                 |                 |
   +=================+=================+=================+=================+
   | NO1             | Oslo            | Oslo, Akershus, | NO011-034       |
   |                 |                 | Hedmark,        |                 |
   |                 |                 | Oppland,        |                 |
   |                 |                 | Østfold,        |                 |
   |                 |                 | Buskerud,       |                 |
   |                 |                 | Vestfold,       |                 |
   |                 |                 | Telemark        |                 |
   +-----------------+-----------------+-----------------+-----------------+
   | NO2             | Kristiansand    | Aust-Agder,     | NO041-043       |
   |                 |                 | Vest-Agder,     |                 |
   |                 |                 | Rogaland        |                 |
   +-----------------+-----------------+-----------------+-----------------+
   | NO3             | Trondheim,      | Sogn og         | NO052-060       |
   |                 | Molde           | Fjordane, Møre  |                 |
   |                 |                 | og Romsdal,     |                 |
   |                 |                 | Trøndelag       |                 |
   +-----------------+-----------------+-----------------+-----------------+
   | NO4             | Tromsø          | Nordland,       | NO071-073       |
   |                 |                 | Troms, Finnmark |                 |
   +-----------------+-----------------+-----------------+-----------------+
   | NO5             | Bergen          | Hordaland       | NO051           |
   +-----------------+-----------------+-----------------+-----------------+
   | SE1             | Luleå           | Norrbotten      | SE332           |
   +-----------------+-----------------+-----------------+-----------------+
   | SE2             | Sundsvall       | Gävleborg,      | SE313-331       |
   |                 |                 | Västernorrland, |                 |
   |                 |                 | Jämtland,       |                 |
   |                 |                 | Västerbotten    |                 |
   +-----------------+-----------------+-----------------+-----------------+
   | SE3             | Stockholm       | Stockholm,      | SE110-211,      |
   |                 |                 | Uppsala,        | SE214,          |
   |                 |                 | Södermanland,   | SE232-312       |
   |                 |                 | Östergötland,   |                 |
   |                 |                 | Örebro,         |                 |
   |                 |                 | Västmanland,    |                 |
   |                 |                 | Jönköping,      |                 |
   |                 |                 | Gotland, Västra |                 |
   |                 |                 | Götaland,       |                 |
   |                 |                 | Värmland,       |                 |
   |                 |                 | Dalarna         |                 |
   +-----------------+-----------------+-----------------+-----------------+
   | SE4             | Malmö           | Kronoberg,      | SE212-213,      |
   |                 |                 | Kalmar,         | SE221-231       |
   |                 |                 | Blekinge,       |                 |
   |                 |                 | Halland, Skåne  |                 |
   +-----------------+-----------------+-----------------+-----------------+

Approximate bidding zone polygons are available from the tmrowco/electricitymap-contrib repository [tmrowco2020]_.

Combining all of these produces the following map.

.. bokeh-plot:: scripts/zones_plot.py
   :source-position: none

Approximate bidding zones of focus countries and their interconnections, made using polygons by tmrowco and Eurostat (© EuroGeographics for the administrative boundaries), and map tiles from OpenStreetMap / CartoDB.
