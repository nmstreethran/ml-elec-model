Background
==========

Electricity system
------------------

The electricity system can be seen as having two components; the physical grid consisting of generators and transmission and distribution systems, and the electricity market consisting of a number of actors.

Electricity systems exist in different resolutions and levels of uncertainty. The figure below represents the different scales of electricity systems, mainly in terms of temporal resolution, but also uncertainty and spatial resolution. Temporally, "real-time" is referred to as the time of dispatch. It can be observed that the operational planning scale has high spatial and temporal resolution, and relatively low uncertainty. Operational planning includes dispatch planning and plant scheduling (i.e., unit commitment), which ranges from a few minutes to a week before dispatch. Maintenance planning can take a few weeks to years, as it involves upgrade and maintenance work which may require shut-down of units or assets, in turn affecting the availability of generation units and grid infrastructure. Adequacy assessments, which takes years, involve assessing the existing generation and storage capacities and planning for new installations based on demand projections, to ensure this demand will be met in the future. Finally, grid investment decisions, including planning transmission and distribution grid networks, cross-border and regional interconnections and grid capacity expansions, take many years to decades and have very high uncertainty as a result.

.. figure:: images/resolution.png
    :alt: The various scales of electricity systems in terms of their approximate temporal resolution, as well as spatial resolution and uncertainty, adapted from Glismann 2018 and Pfenninger, et al. 2014.

    The various scales of electricity systems in terms of their approximate temporal resolution, as well as spatial resolution and uncertainty, adapted from Glismann 2018 and Pfenninger, et al. 2014.

Generation technologies
-----------------------

The table below shows the characteristics of the main energy generation technologies, including their costs. These generation sources have different variabilities, fuel types, flexibilities, costs and carbon emissions. According to the EU reference scenario 2016, wind and solar energy resources, which are variable renewable energy (VRE) resources, are expected to generate a total of 35 % of EU's electricity by 2050, which is a significant increase (23 %) from 2015 levels. Conversely, generation from nuclear and solids, which are not variable and provide base load generation, are expected to decrease significantly. Unlike conventional generators, VRE are intermittent as they are dependent on atmospheric conditions, such as wind speed and cloud cover, and they vary both spatially (i.e., location-dependent) and temporally. Therefore, VRE generation cannot be controlled to meet the demand patterns and needs of the energy system, which is a challenge to electricity and energy system operators in general. The costs listed in this table are derived based on National Renewable Energy Laboratory (NREL)'s NREL-SEAC 2008 Data Set. VRE generation technologies have high capital expenditure (CAPEX) compared to conventional fossil-powered and biomass generation. Conversely, the operational expenditure (OPEX), which includes fuel and fixed operational and maintenance (O&M) costs, is low for VRE generation technologies, as they have no fuel costs unlike conventional generators.

.. table:: Characteristics of the main energy generation technologies, adapted from Erbach 2016 and Tidball, et al. 2010.

    =============== ============ ============= =============== ============== ========= ========= ===============
    **Type**\  [1]_ **Variable** **Fuel type** **Flexibility** **Low carbon** **CAPEX** **OPEX**  **LCOE**\  [2]_
    =============== ============ ============= =============== ============== ========= ========= ===============
    Coal            no           fossil        medium          no             low       high      very low
    Natural gas     no           fossil        high            no             very low  very high low
    Biomass         no           renewable     medium          yes [3]_       low       very high very high
    Nuclear         no           nuclear       low             zero-emission  medium    medium    medium
    Hydro           no           renewable     very high       zero-emission                     
    Solar           yes          renewable     very low        zero-emission  very high very low  very high
    Wind            yes          renewable     very low        zero-emission                     
    *Onshore wind*                                                            high      very low  very low
    *Offshore wind*                                                           very high low       high
    Geothermal      no           renewable     high            zero-emission  high      medium    high
    =============== ============ ============= =============== ============== ========= ========= ===============

.. [1] Costs for natural gas, biomass, solar and geothermal are that of advanced combustion turbine, biomass gasification plant, utility-scale photovoltaic and hydrothermal plant respectively.
.. [2] LCOE - levelised cost of electricity.
.. [3] Regrowth of biomass compensates emissions.

Electricity market
------------------

The actors in the electricity market include generators, retailers, large and small consumers, transmission system operators (TSOs), distribution network operators (DNOs), balance responsible parties (BRPs), aggregators, regulators, and market operators.

There are two types of electricity markets; the retail market and the wholesale market. The retail market involves the retailers buying electricity from generators and selling it to consumers. The wholesale market involves generators, retailers and (large) consumers, who buy and sell electricity. Energy-only transactions in the wholesale market have different temporal resolutions and take place before dispatch, shown in green in the figure below. Balancing markets, shown in pink in the figure, which involve both energy and services, operate both before and after dispatch. The energy-only markets are operated by the market operator or power exchanges, while the balancing market is operated by the system operator. The day-ahead and intra-day markets can be considered short-term electricity markets, as the former takes place 24 hours in advance of dispatch, while the latter takes place continuously after the day-ahead market, up to minutes before dispatch.

.. figure:: images/market-resolution.png
    :alt: The various electricity markets in terms of operator and temporal resolution, before and after dispatch, adapted from KU Leuven Energy Institute 2015 and Pinson 2018.

    The various electricity markets in terms of operator and temporal resolution, before and after dispatch, adapted from KU Leuven Energy Institute 2015 and Pinson 2018.

In short-term electricity market auctions, such as the day-ahead market auction, generating companies have the incentive to bid as low as possible, as the supply bids are ranked in ascending order of price. Conversely, on the demand side, consumers have the incentive to bid as high as possible, as the demand bids are ranked in descending order of price. These two curves form a so called merit order, and the intersection between these two curves is the equilibrium point. The price at this equilibrium point is the market clearing price, which is what all accepted bids will receive, regardless of their initial bid. All supply and demand bids to the left of the equilibrium point will be accepted, and those to the right are rejected.

In the case of generating companies, the OPEX of their generators determine the price at which it is bid. For conventional power plants, this OPEX includes fuel costs and carbon costs (except nuclear power plants). For solar and wind power plants, the OPEX is close to zero, as they do not require fuel to run. The revenue received by generating companies in the day-ahead market for each power plant contributes towards their CAPEX. Since conventional power plants have relatively low CAPEX, and fuel costs are high, the main decision generating companies have to make in short-term electricity markets is whether it is economical to run these power plants. For solar and wind power plants, which have relatively high CAPEX, companies are interested in getting as many bids accepted and as much of the electricity generated sold as possible.

References
----------

1. Erbach, G., "`Understanding electricity markets in the EU <http://www.europarl.europa.eu/thinktank/en/document.html?reference=EPRS_BRI%282016%29593519>`__," European Union, Briefing, November 2016.
2. Glismann, S., "Modelling from a TSO Perspective - TenneT NL," 6 September 2018.
3. Pfenninger, S., Hawkes, A., and Keirstead, J., "`Energy systems modeling for twenty-first century energy challenges <https://doi.org/10.1016/j.rser.2014.02.003>`__," Renewable and Sustainable Energy Reviews, vol. 33, pp. 74–86, May 2014.
4. "`Energy modelling - EU Reference Scenario 2016 <https://data.europa.eu/euodp/data/dataset/energy-modelling>`__."
5. Joskow, P. L., "`Comparing the Costs of Intermittent and Dispatchable Electricity Generating Technologies <https://doi.org/10.1257/aer.101.3.238>`__," American Economic Review, vol. 101, no. 3, pp. 238–241, May 2011.
6. Tidball, R., Bluestein, J., Rodriguez, N., Knoke, S., and Macknick, J., "`Cost and Performance Assumptions for Modeling Electricity Generation Technologies <https://www.nrel.gov/docs/fy11osti/48595>`__," National Renewable Energy Laboratory, Subcontract Report NREL/SR-6A20-48595, 2010.
7. Pinson, P., "Renewables in Electricity Markets."
8. "`The current electricity market design in Europe <https://set.kuleuven.be/ei/factsheets>`__," KU Leuven Energy Institute, Heverlee, Belgium, January 2015.
9. "`Overview of European Electricity Markets <https://ec.europa.eu/energy/sites/ener/files/documents/overview_of_european_electricity_markets.pdf>`__," European Union, Brussels, Belgium, February 2016.
