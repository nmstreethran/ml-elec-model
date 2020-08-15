Regions
=======

The table below lists countries that will be referred in this document, together with their country codes. Country codes are according to ISO_3166-1 alpha-2 [ISO]_.

.. table:: Countries and country codes.

   +--------------+---------------------+
   | Country code | Country             |
   +==============+=====================+
   | AT           | Austria             |
   +--------------+---------------------+
   | BE           | Belgium             |
   +--------------+---------------------+
   | CH           | Switzerland         |
   +--------------+---------------------+
   | CZ           | Czech Republic      |
   +--------------+---------------------+
   | DE           | Germany             |
   +--------------+---------------------+
   | DK           | Denmark             |
   +--------------+---------------------+
   | ES           | Spain               |
   +--------------+---------------------+
   | FR           | France              |
   +--------------+---------------------+
   | FI           | Finland             |
   +--------------+---------------------+
   | IT           | Italy               |
   +--------------+---------------------+
   | LT           | Lithuania           |
   +--------------+---------------------+
   | LU           | Luxembourg          |
   +--------------+---------------------+
   | NL           | Netherlands         |
   +--------------+---------------------+
   | NO           | Norway              |
   +--------------+---------------------+
   | PL           | Poland              |
   +--------------+---------------------+
   | SE           | Sweden              |
   +--------------+---------------------+
   | UK           | United Kingdom      |
   +--------------+---------------------+

Territories
-----------

The nomenclature of territorial units for statistics (:term:`NUTS`) [Eurostat]_ classifies territorial units in Europe in different levels [Ofgem2014]_:

- :term:`NUTS` 0: country-level
- :term:`NUTS` 1: major socio-economic regions
- :term:`NUTS` 2: basic regions for the application of regional policies
- :term:`NUTS` 3: small regions for specific diagnoses

The map below illustrates the national borders of Germany and its interconnections.

.. figure:: ../images/countries.png
   :alt: NUTS 0 boundaries (national borders) for the Germany and its interconnections. Data from Eurostat (© EuroGeographics for the administrative boundaries).

   NUTS 0 boundaries (national borders) for the Germany and its interconnections. Data from Eurostat (© EuroGeographics for the administrative boundaries).

Local administrative units (:term:`LAU`) are municipalities and communes, which are smaller than :term:`NUTS` 3 areas [Eurostatb]_. The table below shows how :term:`NUTS` and :term:`LAU` correspond to national administrative units in each country [Eurostata]_.

.. table:: Correspondence between the NUTS levels and the national administrative units (last update 11/06/2020, based on NUTS 2021 and LAU 2019). The number of units are shown in brackets. Data: Eurostat.

   +---------+---------------+-------------------+--------------+------------+
   | Country | NUTS 1        | NUTS 2            | NUTS 3       | LAU        |
   | code    |               |                   |              |            |
   +=========+===============+===================+==============+============+
   | AT      | Gruppen von   | Bundesländer (9)  | Gruppen      | Gemeinden  |
   |         | Bundesländern |                   | von          | (2,096)    |
   |         | (3)           |                   | Gemeinden    |            |
   |         |               |                   | (35)         |            |
   +---------+---------------+-------------------+--------------+------------+
   | CH      | N/A (1)       | Grossregionen /   | Kantone /    | Gemeinden  |
   |         |               | Grandes regions / | Cantons /    | / Communes |
   |         |               | Grandi regioni    | Cantoni      | / Comuni   |
   |         |               | (7)               | (26)         | (2,222)    |
   +---------+---------------+-------------------+--------------+------------+
   | CZ      | Území (1)     | Regiony           | Kraje (14)   | Obce       |
   |         |               | soudržnosti (8)   |              | (6,258)    |
   +---------+---------------+-------------------+--------------+------------+
   | DE      | Länder (16)   | Regierungsbezirke | Kreise       | Gemeinden  |
   |         |               | (38)              | (401)        | (11,087)   |
   +---------+---------------+-------------------+--------------+------------+
   | DK      | N/A (1)       | Regioner (5)      | Landsdele    | Kommuner   |
   |         |               |                   | (11)         | (99)       |
   +---------+---------------+-------------------+--------------+------------+
   | FR      | Z.E.A.T + DOM | Régions + DOM     | Départements | Communes   |
   |         | (14)          | (27)              | + DOM        | (34,970)   |
   |         |               |                   | (101)        |            |
   +---------+---------------+-------------------+--------------+------------+
   | LU      | N/A (1)       | N/A (1)           | N/A (1)      | Communes   |
   |         |               |                   |              | (102)      |
   +---------+---------------+-------------------+--------------+------------+
   | NL      | Landsdelen    | Provincies (12)   | N/A (40)     | Gemeenten  |
   |         | (4)           |                   |              | (355)      |
   +---------+---------------+-------------------+--------------+------------+
   | PL      | Makroregiony  | Regiony (17)      | Podregiony   | Gminy      |
   |         | (7)           |                   | (73)         | (2,478)    |
   +---------+---------------+-------------------+--------------+------------+
   | SE      | Grupper av    | Riksområden (8)   | Län (21)     | Kommuner   |
   |         | riksområden   |                   |              | (290)      |
   |         | (3)           |                   |              |            |
   +---------+---------------+-------------------+--------------+------------+

Some datasets provide postcodes, which must be translated into geographical locations for better clustering and comparisons. GeoNames [GeoNames]_ provides open postcode data.

Transmission system operators and interconnections
--------------------------------------------------

Europe has multiple :term:`TSO`\s [ENTSO-Ea]_ and cross-border interconnections. These are listed for Germany and its interconnections, along with bidding zones, in the table below.

.. table:: TSOs and cross-border interconnections in Germany and its interconnections. Data: European Network of Transmission System Operators for Electricity.

   +---------+-----------------------+------------------+-------------------+
   | Country | TSOs                  | Cross-border     | Bidding           |
   |         |                       | interconnections | zones             |
   +=========+=======================+==================+===================+
   | AT      | Austrian Power Grid   |                  | AT                |
   |         | AG, Vorarlberger      |                  |                   |
   |         | Übertragungsnetz GmBH |                  |                   |
   +---------+-----------------------+------------------+-------------------+
   | CH      | Swissgrid ag          |                  | CH                |
   +---------+-----------------------+------------------+-------------------+
   | CZ      | ČEPS a.s.             |                  | CZ                |
   +---------+-----------------------+------------------+-------------------+
   | DE      | TransnetBW GmBH,      | AT, CH, CZ, DK,  | DE-LU (DE-AT-LU   |
   |         | TenneT TSO GmBH,      | FR, LU, NL, PL,  | prior to          |
   |         | Amprion GmBH, 50Hertz | SE               | 01/10/2018)       |
   |         | Transmission GmBH     |                  |                   |
   +---------+-----------------------+------------------+-------------------+
   | DK      | Energinet.dk          | DE, NO, SE       | DK-1, DK-2        |
   +---------+-----------------------+------------------+-------------------+
   | FR      | Réseau de Transport   | BE, CH, DE, ES,  | FR                |
   |         | d’Electricité         | IT, UK           |                   |
   +---------+-----------------------+------------------+-------------------+
   | LU      | Creos Luxembourg S.A. |                  | LU                |
   +---------+-----------------------+------------------+-------------------+
   | NL      | TenneT TSO B.V.       |                  | NL                |
   +---------+-----------------------+------------------+-------------------+
   | PL      | Polskie Sieci         |                  | PL                |
   |         | Elektroenergetyczne   |                  |                   |
   |         | S.A.                  |                  |                   |
   +---------+-----------------------+------------------+-------------------+
   | SE      | Svenska Kraftnät      | DK, DE, FI, LT,  | SE-1, SE-2, SE-3, |
   |         |                       | NO, PL           | SE-4              |
   +---------+-----------------------+------------------+-------------------+

Bidding zones
-------------

A bidding zone is the largest geographical area within which market participants are able to exchange energy without capacity allocation. There are three types of bidding zones:

1. national borders (e.g., the Netherlands - majority of bidding zones in Europe
2. larger than national borders (e.g., Germany and Luxembourg)
3. smaller zones within individual countries (e.g., Sweden)

The table below lists bidding zones in Germany and its interconnections by country and market operator [NordPool]_, [EPEXSPOT]_.

.. table:: Bidding zones and market operators in Germany and its interconnections.

   +---------+----------------+-------------------+
   | Country | Markets        | Zones             |
   +=========+================+===================+
   | AT      |                | AT                |
   +---------+----------------+-------------------+
   | CH      |                | CH                |
   +---------+----------------+-------------------+
   | CZ      |                | CZ                |
   +---------+----------------+-------------------+
   | DE      | EEX, EPEX      | DE-LU (DE-AT-LU   |
   |         |                | prior to          |
   |         |                | 01/10/2018)       |
   +---------+----------------+-------------------+
   | DK      | EEX, Nord Pool | DK-1, DK-2        |
   +---------+----------------+-------------------+
   | FR      | EEX, EPEX      | FR                |
   +---------+----------------+-------------------+
   | LU      |                | DE-LU             |
   +---------+----------------+-------------------+
   | NL      | APX            | NL                |
   +---------+----------------+-------------------+
   | PL      |                | PL                |
   +---------+----------------+-------------------+
   | SE      | EEX, Nord Pool | SE-1, SE-2, SE-3, |
   |         |                | SE-4              |
   +---------+----------------+-------------------+

Prior to 01/10/2018, Germany was part of the DE-AT-LU bidding zone, together with Austria (AT) and Luxembourg (LU), which had split into the DE-LU and AT bidding zones, as reported by European Network of Transmission Systems Operators for Electricity (:term:`ENTSO-E`) below [ENTSO-Ee]_:

   *[...] DE-AT-LU bidding zone split on the 23rd of August. BZN|DE-AT-LU will be separated into 2 new bidding zones BZN|DE-LU and BZN|AT.*

   *New bidding zones will be active from the 1st of October, however, first data submissions, like month ahead forecasts, are expected from the 1st of September.*

   *Validity end date for BZN|DE-AT-LU is the end of September 2018. [...]*

Since this project will focus on the first half of 2018, the DE-AT-LU bidding zone will be used.

Mapping bidding zones to :term:`NUTS` 3 territories is straightforward for DE, AT, CH, CZ, FR, LU, NL, and PL (bidding zone type 1 for all except DE, which is type 2) -- all :term:`NUTS` 3 territories in these countries are part of the same bidding zone.

Denmark is both conveniently separated into two zones that are easily distinguishable. These are Western Denmark (:term:`NUTS` IDs with prefixes DK03-DK05 and bidding zone DK-1) and Eastern Denmark (:term:`NUTS` IDs with prefixes DK01-DK02 and bidding zone DK-2).

There is no clear indication of the bidding zone boundaries for Sweden, so some assumptions were made. Sweden has four smaller bidding zones (type 3) with flexible borders. This was done to optimise allocation of resources and reduce the overall price of electricity [EuropeanCommission2010]_. By cross-referencing Nord Pool market data [NordPool]_, [NordPoola]_, :term:`NUTS` 3 data, and a county map of Sweden [Wikipedia2019]_, the territories are split into the bidding zones as shown in the table below. Nord Pool associates each bidding zone with a major reference city in that zone.

.. table:: Bidding zones and their territories for Sweden, approximated based on Nord Pool market data, NUTS 3 data, and a county map of Sweden.

   +---------+--------------+-----------------+------------+
   | Bidding | Reference    | Counties        | NUTS 3 IDs |
   | zone    | cities       |                 |            |
   +=========+==============+=================+============+
   | SE-1    | Luleå        | Norrbotten      | SE332      |
   +---------+--------------+-----------------+------------+
   | SE-2    | Sundsvall    | Gävleborg,      | SE313-331  |
   |         |              | Västernorrland, |            |
   |         |              | Jämtland,       |            |
   |         |              | Västerbotten    |            |
   +---------+--------------+-----------------+------------+
   | SE-3    | Stockholm    | Stockholm,      | SE110-211, |
   |         |              | Uppsala,        | SE214,     |
   |         |              | Södermanland,   | SE232-312  |
   |         |              | Östergötland,   |            |
   |         |              | Örebro,         |            |
   |         |              | Västmanland,    |            |
   |         |              | Jönköping,      |            |
   |         |              | Gotland, Västra |            |
   |         |              | Götaland,       |            |
   |         |              | Värmland,       |            |
   |         |              | Dalarna         |            |
   +---------+--------------+-----------------+------------+
   | SE-4    | Malmö        | Kronoberg,      | SE212-213, |
   |         |              | Kalmar,         | SE221-231  |
   |         |              | Blekinge,       |            |
   |         |              | Halland, Skåne  |            |
   +---------+--------------+-----------------+------------+

Approximate bidding zone polygons are available from Tomorrow's electricityMap repository [tmrowco2020]_. Combining all of these produces the following map.

.. figure:: ../images/zones.png
   :alt: Approximate bidding zones of Germany and its interconnections (in the first half of 2018), made using polygons by Tomorrow and Eurostat (© EuroGeographics for the administrative boundaries).

   Approximate bidding zones of Germany and its interconnections (in the first half of 2018), made using polygons by Tomorrow and Eurostat (© EuroGeographics for the administrative boundaries).
