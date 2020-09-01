Electricity system data
=======================

See `Data sources <data_used/data-sources.html#entso-e-transparency-platform-data>`__ for more information regarding data from the :term:`ENTSO-E TP` used in this project.

The bidding zones in Germany and its interconnections, mapped to their corresponding Energy Identification Codes (:term:`EIC`\s) [ENTSO-Ed]_ as shown in the table below, are used when querying using the pandas client.

.. IMPORTANT::
   Note that ``DE-LU`` only works for timestamps starting 01/10/2018 [ENTSO-Ee]_. Use ``DE-AT-LU`` for timestamps prior to this date. Since this project is focussing on the first half of 2018, ``DE-AT-LU`` is used.

.. table:: Bidding zones in Germany and its interconnections, and their corresponding EICs.

   +---------------+-------------+----------------------+
   | Zone name     | Bidding     | EIC                  |
   |               | zone        |                      |
   +===============+=============+======================+
   | Austria       | AT          | ``10YAT-APG------L`` |
   +---------------+-------------+----------------------+
   | Switzerland   | CH          | ``10YCH-SWISSGRIDZ`` |
   +---------------+-------------+----------------------+
   | Czech         | CZ          | ``10YCZ-CEPS-----N`` |
   | Republic      |             |                      |
   +---------------+-------------+----------------------+
   | Germany       |             | ``10Y1001A1001A83F`` |
   +---------------+-------------+----------------------+
   | Germany       |             | ``10YDE-VE-------2`` |
   | (50Hertz      |             |                      |
   | Transmission) |             |                      |
   +---------------+-------------+----------------------+
   | Germany       |             | ``10YDE-RWENET---I`` |
   | (Amprion)     |             |                      |
   +---------------+-------------+----------------------+
   | Germany       |             | ``10YDE-EON------1`` |
   | (TenneT TSO)  |             |                      |
   +---------------+-------------+----------------------+
   | Germany       |             | ``10YDE-ENBW-----N`` |
   | (TransnetBW)  |             |                      |
   +---------------+-------------+----------------------+
   | Germany,      | DE-AT-LU    | ``10Y1001A1001A63L`` |
   | Austria, and  |             |                      |
   | Luxembourg    |             |                      |
   +---------------+-------------+----------------------+
   | Germany and   | DE-LU       | ``10Y1001A1001A82H`` |
   | Luxembourg    |             |                      |
   +---------------+-------------+----------------------+
   | Luxembourg    |             | ``10YLU-CEGEDEL-NQ`` |
   +---------------+-------------+----------------------+
   | Denmark       |             | ``10Y1001A1001A65H`` |
   +---------------+-------------+----------------------+
   | Denmark       |             | ``10Y1001A1001A796`` |
   | (Energinet)   |             |                      |
   +---------------+-------------+----------------------+
   | Western       | DK-1        | ``10YDK-1--------W`` |
   | Denmark       |             |                      |
   +---------------+-------------+----------------------+
   | Eastern       | DK-2        | ``10YDK-2--------M`` |
   | Denmark       |             |                      |
   +---------------+-------------+----------------------+
   | France        | FR          | ``10YFR-RTE------C`` |
   +---------------+-------------+----------------------+
   | Netherlands   | NL          | ``10YNL----------L`` |
   +---------------+-------------+----------------------+
   | Poland        | PL          | ``10YPL-AREA-----S`` |
   +---------------+-------------+----------------------+
   | Sweden        |             | ``10YSE-1--------K`` |
   +---------------+-------------+----------------------+
   | Luleå, Sweden | SE-1        | ``10Y1001A1001A44P`` |
   +---------------+-------------+----------------------+
   | Sundsvall,    | SE-2        | ``10Y1001A1001A45N`` |
   | Sweden        |             |                      |
   +---------------+-------------+----------------------+
   | Stockholm,    | SE-3        | ``10Y1001A1001A46L`` |
   | Sweden        |             |                      |
   +---------------+-------------+----------------------+
   | Malmö, Sweden | SE-4        | ``10Y1001A1001A47J`` |
   +---------------+-------------+----------------------+

Generation
----------

:term:`ENTSO-E TP` aggregates data by following electricity production types [ENTSO-Eb]_:

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

- 15 minutes: AT, DE, LU, NL
- 1 hour: CH, CZ, DK, NO, PL, SE

Each data point represents the average of all available instantaneous net generation output values on each market time unit. The values are estimated if unknown. The actual outputs of small-scale generating units may be estimated if there are no real-time measurements from these units. The data are published on :term:`ENTSO-E TP` no later than one hour after the operational period.

The installed capacity per production unit dataset contains information about production units (existing and planned) with an installed generation capacity of at least 100 MW, which includes the following:

- unit name
- code
- installed net generation capacity (MW)
- voltage connection level (kV)
- bidding zone (denoted using :term:`EIC`\s)
- production type (e.g., fossil gas, wind offshore)

This information is published annually on :term:`ENTSO-E TP` at the start of the year and is valid for the three following years.

Load
----

This dataset represents the actual total load in MW per bidding zone per market time unit. These are available at different resolutions depending on the country, which is summarised in below.

Temporal resolution of electricity load dataset by country:

- 15 minutes: DE, LU, NL
- 1 hour: AT, CH, CZ, DK, NO, PL, SE

The total load is defined as equal to the sum of power generated by plants on both :term:`TSO` and :term:`DNO` networks, from which the following are deduced:

- the balance (export-import) of exchanges on interconnections between neighbouring bidding zones
- the power absorbed by energy storage resources

The load is calculated using the average of real-time load values per bidding zone per market time unit.

.. code:: md

   Actual total load (including losses without stored energy)
   = Net generation – Exports + Imports – Absorbed energy

For these calculations, the net generation is preferred. However, gross generation may be used if it is available with the better precision. The :term:`TSO`\s responsible for each area decide whether to use gross or net generation, but they are required to keep their choice consistent per bidding zone. Absorbed energy is also provided as separate information with the aggregated generation output of the hydro pumped storage. The physical flow on the tie line is measured as agreed by neighbouring :term:`TSO`\s or bidding zones, where applicable. This dataset is published on :term:`ENTSO-E TP` no later than one hour after the end of the operating period.

.. rubric:: Footnotes

.. [#f4] https://transparency.entsoe.eu/usrm/user/createPublicUser
