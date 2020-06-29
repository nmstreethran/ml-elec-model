Data sources
============

Electricity system data
-----------------------

European Network of Transmission Systems Operators for Electricity (:term:`ENTSO-E`):

- Transparency Platform (:term:`ENTSO-E TP`):
   - https://transparency.entsoe.eu/
- List of data available for free re-use:
   - https://transparency.entsoe.eu/content/static_content/download?path=/Static%20content/terms%20and%20conditions/191025_List_of_Data_available_for_reuse_v2_cln.pdf
- Regional security coordinators:
   - https://www.entsoe.eu/major-projects/rscis/
- Power statistics:
   - https://www.entsoe.eu/data/power-stats/
- Energy identification codes (:term:`EIC`\s):
   - https://www.entsoe.eu/data/energy-identification-codes-eic/
- Guides:
   - https://transparency.entsoe.eu/content/static_content/download?path=/Static%20content/web%20api/RestfulAPI_IG.pdf
   - https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html
   - https://transparency.entsoe.eu/content/static_content/Static%20content/knowledge%20base/knowledge%20base.html
- User registration:
   - https://transparency.entsoe.eu/usrm/user/createPublicUser
- Terms and conditions:
   - https://transparency.entsoe.eu/content/static_content/Static%20content/terms%20and%20conditions/terms%20and%20conditions.html

Tools:

- :term:`ENTSO-E` Python client:
   - https://github.com/EnergieID/entsoe-py

Power plants
------------

Germany
~~~~~~~

Bundesnetzagentur:

- https://www.bundesnetzagentur.de/EN/Areas/Energy/Companies/SecurityOfSupply/GeneratingCapacity/PowerPlantList/PubliPowerPlantList_node.html

Netztransparenz - Erneuerbare-Energien-Gesetz (EEG, which roughly translates to Renewable Energy Sources Act) plant data:

- https://www.netztransparenz.de/EEG/Anlagenstammdaten

Geographical data
-----------------

Eurostat NUTS data:

- https://ec.europa.eu/eurostat/web/nuts/background

Polygons approximately representing bidding zones in Norway and Sweden are from `Tomorrow's electricityMap <https://github.com/tmrowco/electricitymap-contrib>`__:

- https://github.com/tmrowco/electricitymap-contrib/tree/master/web/third_party_maps

These sources have been used by Tomorrow:

- Norway:
   - http://driftsdata.statnett.no/Web/map/snpscustom
   - https://www.nve.no/map-services/
   - https://www.nve.no/karttjenester/
   - License:
      - https://data.norge.no/nlod/en/2.0/
- Sweden:
   - https://www.natomraden.se/

Maps:

- https://en.wikipedia.org/w/index.php?title=Counties_of_Norway&oldid=890663009
- https://en.wikipedia.org/w/index.php?title=Counties_of_Sweden&oldid=882806371

Press releases and reports:

- https://ec.europa.eu/commission/presscorner/detail/en/IP_10_425
- https://www.nordpoolspot.com/globalassets/download-center/day-ahead/elspot-area-change-log.pdf
- https://www.ofgem.gov.uk/sites/default/files/docs/2014/10/fta_bidding_zone_configuration_literature_review_1.pdf

Meteorological data
-------------------

Germany
~~~~~~~

Deutscher Wetterdienst (:term:`DWD`); Germany's meteorological service:

- Climate Data Center (:term:`DWD CDC`):
   - https://www.dwd.de/EN/climate_environment/cdc/cdc_node.html
- Terms and conditions:
   - https://opendata.dwd.de/climate_environment/CDC/Terms_of_use.txt

Tools:

- :term:`DWD` Python client:
   - https://github.com/panodata/dwdweather2

Denmark
~~~~~~~

Danish Meteorological Institute:

- http://research.dmi.dk/data/

The Netherlands
~~~~~~~~~~~~~~~

Royal Netherlands Meteorological Institute:

- https://data.knmi.nl/datasets

Norway
~~~~~~

Norwegian Meteorological Institute:

- https://www.met.no/en/free-meteorological-data

Sweden
~~~~~~

Swedish Meteorological and Hydrological Institute:

- https://www.smhi.se/en/services/professional-services/data-and-statistics
- https://www.smhi.se/en/services/open-data/search-smhi-s-open-data-1.81004
- https://www.smhi.se/data/utforskaren-oppna-data/
- https://opendata.smhi.se/apidocs/
- Meteorological observations:
   - https://opendata.smhi.se/apidocs/metobs/index.html
   - Open data :term:`API`:
      - https://opendata-download-metobs.smhi.se/api
      - https://opendata.smhi.se/apidocs/metobs/common.html
      - https://opendata.smhi.se/apidocs/metobs/schemas.html
      - https://opendata.smhi.se/apidocs/metobs/codeexamples.html
- Meteorological forecasts:
   - https://opendata.smhi.se/apidocs/metfcst/index.html
   - https://opendata-download-metfcst.smhi.se/
- Meteorological analysis:
   - Weather:
      - https://opendata.smhi.se/apidocs/metanalys/index.html
   - Sunshine:
      - https://opendata.smhi.se/apidocs/strang/index.html
- License:
   - https://www.smhi.se/data/oppna-data/information-om-oppna-data/villkor-for-anvandning-1.30622
- Policy:
   - https://www.smhi.se/omsmhi/policys/datapolicy/mer-och-mer-oppna-data-1.8138

Electricity market data
-----------------------

Nord Pool:

- https://www.nordpoolgroup.com/Market-data1/#/nordic/table
- https://www.nordpoolgroup.com/historical-market-data/
- Membership list:
   - https://www.nordpoolgroup.com/trading/join-our-markets/membership/
- Terms and conditions for use:
   - https://www.nordpoolgroup.com/About-us/Terms-and-conditions-for-use/

EEX:

- https://www.eex.com/en/market-data/power
- https://www.eex-transparency.com/power/

:term:`ENTSO-E TP`:

- https://transparency.entsoe.eu/transmission-domain/r2/dayAheadPrices/show

Press releases and reports:

- https://ec.europa.eu/energy/sites/ener/files/documents/overview_of_european_electricity_markets.pdf
- https://www.europarl.europa.eu/thinktank/en/document.html?reference=EPRS_BRI%282016%29593519
