Background
==========

The energy transition
---------------------

The transition towards a future low-carbon economy is driven globally by the Paris Agreement, which recognises the need for sustainable development worldwide to counter the threats of climate change. The European Union (EU) is committed to reduce greenhouse gas emissions by 2050 to 80-90 % below 1990 levels. As the energy industry is responsible for the highest share of anthropogenic greenhouse gas emissions, importance is placed on how changes in energy systems can help achieve these greenhouse gas emission reduction targets.

A number of opportunities exist for the decarbonisation of the energy industry. The International Renewable Energy Agency, in their renewable energy roadmap study, has identified renewable energy as having the highest potential in reducing energy-related carbon dioxide emissions globally, which is closely followed by energy efficiency and electrification with renewable energy. In a 2018 political agreement, the EU member states agreed upon a target of at least 32 % of the demand being met with renewables by 2030, through national targets of the individual member states. The electricity demand in the transport sector is also expected to increase due to expected petrol and diesel engine bans and subsequently the electrification of road transport.

Conventional energy resources, such as fossil fuels, biomass, hydro, geothermal, and nuclear fuels are non-variable. Fossil fuels, including coal, natural gas, and oil, as well as nuclear, are non-renewable. While nuclear, biomass, hydro, and geothermal energy are clean and/or renewable, generating power from fossil fuels or hydrocarbons involve combustion, which is a process that releases carbon dioxide and harmful by-products, such as soot. Fossil fuels are still extensively used and depended upon in industries around the world, including transport, chemicals, and power generation. As a result, the focus of the energy transition is to move away from fossil fuels to cleaner energy resources and technologies, including variable renewable energy resources such as solar and wind. According to the EU reference scenario 2016, wind and solar energy resources are expected to generate a total of 35 % of EU's electricity by 2050, which is a significant increase (23 %) from 2015 levels. Conversely, generation from nuclear and solids, which are not variable and provide base load generation, are expected to decrease significantly.

While fossil fuels can be stored, transported, combusted, and converted into more useful forms of energy when there is a demand, generation from variable renewable energy resources cannot be controlled to follow consumption patterns in the same way. Variable renewable energy resources are intermittent as they are dependent on atmospheric conditions, such as cloud cover and wind speed. They also have variations temporally (time-based) and spatially (location-based). This is a challenge to energy system operators, whose objective is to reliably and securely meet the energy needs at all times.

The energy system is also transitioning towards a decentralised system with more consumer participation and new forms of flexibilities, including sector coupling, demand-side management, energy conversion and storage, cross-border interconnection, and curtailment. This allows demand patterns to shift to better suit the generation patterns in systems with high penetration of variable renewable energy resources, such as solar and wind. This decentralised, flexible, and renewable energy system is more complex than traditional centralised systems, and require improved decision making processes for an optimal system operation. As the energy system is also becoming "smart", the system will have an increasing amount of sensors and controllers that continuously record measurements of the system. Advancements in these technologies mean that data that is fast, heterogeneous and high in volume from the energy system will be generated. This provides an opportunity to exploit data with these characteristics to gain insights on the energy system, which can then be converted to strategies that optimise the system.

Energy system modelling and decision making in various resolutions
------------------------------------------------------------------

Energy systems models are tools used to project the future energy supply of a country or region. The figure below explains the energy systems modelling process using a system analysis approach. This process starts with creating a model of the actual energy system by simplifying and conceptualising the present system. This conceptualised system with all assumptions is then mathematically solved to produce numerical results. These results can then be interpreted and conclusions can be drawn regarding the future energy system. Such conclusions form the evidence-base for decision makers, resulting in policy implications that help achieve these climate targets. This same approach can be used to explain various decision making processes for an energy system at various scales, other than policy making, as energy systems exist in different resolutions and levels of uncertainty.

.. figure:: images/system-analysis.png
    :alt: The system analysis approach applied on the energy system modelling process, adapted from Krook-Riekkola 2015.

    The system analysis approach applied on the energy system modelling process, adapted from Krook-Riekkola 2015.

The figure below represents the different scales of energy systems, mainly in terms of temporal resolution, but also uncertainty and spatial resolution. Temporally, "real-time" is referred to as the time of dispatch. It can be observed that the operational planning scale has high spatial and temporal resolution, and relatively low uncertainty. Operational planning includes dispatch planning and plant scheduling , which ranges from a few minutes to a week before dispatch. Maintenance planning can take a few weeks to years, as it involves upgrade and maintenance work which may require shut-down of units or assets, in turn affecting the availability of generation units and grid infrastructure. Adequacy assessments, which takes years, involve assessing the existing generation and storage capacities and planning for new installations based on demand projections, to ensure this demand will be met in the future. Finally, grid investment decisions, including planning transmission and distribution grid networks, cross-border and regional interconnections, and grid capacity expansions, take many years to decades and have very high uncertainty as a result.

.. figure:: images/resolution.png
    :alt: The various scales of energy systems in terms of their approximate temporal resolution, as well as spatial resolution and uncertainty, adapted from Glismann 2018 and Pfenninger, et al. 2014.

    The various scales of energy systems in terms of their approximate temporal resolution, as well as spatial resolution and uncertainty, adapted from Glismann 2018 and Pfenninger, et al. 2014.

The electricity system
----------------------

The electricity system can be seen as having two components; the physical grid consisting of generators and transmission and distribution systems, and the electricity market consisting of a number of actors.

The table below shows the characteristics of the main energy generation technologies, including their costs. These generation sources have different variabilities, fuel types, flexibilities, costs and carbon emissions. The costs listed in this table are derived based on National Renewable Energy Laboratory (NREL)'s NREL-SEAC 2008 Data Set. VRE generation technologies have high capital expenditure (CAPEX) compared to conventional fossil-powered and biomass generation. Conversely, the operational expenditure (OPEX), which includes fuel and fixed operational and maintenance (O&M) costs, is low for VRE generation technologies, as they have no fuel costs unlike conventional generators.

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

The actors in the electricity market include generators, retailers, large and small consumers, transmission system operators (TSOs), distribution network operators (DNOs), balance responsible parties (BRPs), aggregators, regulators, and market operators.

There are two types of electricity markets; the retail market and the wholesale market. The retail market involves the retailers buying electricity from generators and selling it to consumers. The wholesale market involves generators, retailers and (large) consumers, who buy and sell electricity. Energy-only transactions in the wholesale market have different temporal resolutions and take place before dispatch, shown in green in the figure below. Balancing markets, shown in pink in the figure, which involve both energy and services, operate both before and after dispatch. The energy-only markets are operated by the market operator or power exchanges, while the balancing market is operated by the system operator. The day-ahead and intra-day markets can be considered short-term electricity markets, as the former takes place 24 hours in advance of dispatch, while the latter takes place continuously after the day-ahead market, up to minutes before dispatch.

.. figure:: images/market-resolution.png
    :alt: The various electricity markets in terms of operator and temporal resolution, before and after dispatch, adapted from KU Leuven Energy Institute 2015 and Pinson 2018.

    The various electricity markets in terms of operator and temporal resolution, before and after dispatch, adapted from KU Leuven Energy Institute 2015 and Pinson 2018.

In short-term electricity market auctions, such as the day-ahead market auction, generating companies have the incentive to bid as low as possible, as the supply bids are ranked in ascending order of price. Conversely, on the demand side, consumers have the incentive to bid as high as possible, as the demand bids are ranked in descending order of price. These two curves form a so called merit order, and the intersection between these two curves is the equilibrium point. The price at this equilibrium point is the market clearing price, which is what all accepted bids will receive, regardless of their initial bid. All supply and demand bids to the left of the equilibrium point will be accepted, and those to the right are rejected.

In the case of generating companies, the OPEX of their generators determine the price at which it is bid. For conventional power plants, this OPEX includes fuel costs and carbon costs (except nuclear power plants). For solar and wind power plants, the OPEX is close to zero, as they do not require fuel to run. The revenue received by generating companies in the day-ahead market for each power plant contributes towards their CAPEX. Since conventional power plants have relatively low CAPEX, and fuel costs are high, the main decision generating companies have to make in short-term electricity markets is whether it is economical to run these power plants. For solar and wind power plants, which have relatively high CAPEX, companies are interested in getting as many bids accepted and as much of the electricity generated sold as possible.

Project objective
-----------------

The focus of this project will be on the operational planning resolution of the electricity system. This is due to the potential of renewable energy and electrification using renewable energy in decarbonising the energy and transport industries, as well as to better analyse and include short-term fluctuations of renewable energy generation in energy models. Variable renewable energy resources are also mainly used to generate electricity directly, i.e., wind and solar are converted into electrical energy from kinetic and light or heat energy respectively. This also provides the opportunity to utilise high resolution electricity system data and machine learning methods for forecasting and optimisation of the electricity system. The ultimate aim of this short-term decision making model is to help participants in short-term electricity (i.e., day-ahead) markets to develop operational and bidding strategies to maximise their revenue under uncertainty of variable renewable energy generation. Inputs used by the machine learning model for the day-ahead forecasts include, but are not limited to, recent historical measurements of electricity generation, demand, and market prices.

References
----------

1. "`Paris Agreement <https://unfccc.int/process-and-meetings/the-paris-agreement/the-paris-agreement>`__." United Nations Framework Convention on Climate Change, 2015.
2. "`Energy roadmap 2050 <https://doi.org/10.2833/10759>`__," Publications Office of the European Union, Luxembourg, 2012.
3. "`Global Energy Transformation: A Roadmap to 2050 <http://www.irena.org/publications/2018/Apr/Global-Energy-Transition-A-Roadmap-to-2050>`__," International Renewable Energy Agency, 2018.
4. "`Renewable energy - Energy - European Commission <https://ec.europa.eu/energy/en/topics/renewable-energy>`__."
5. "`World Energy Outlook 2017 <https://www.iea.org/weo2017/>`__," International Energy Agency, Paris, France, 2017.
6. Lund, H., Østergaard, P. A., Connolly, D, and Mathiesen, B. V., "`Smart energy and smart energy systems <https://doi.org/10.1016/j.energy.2017.05.123>`__," Energy, vol. 137, pp. 556–565, October 2017.
7. "`Towards a consumer-centric system <http://www.elia.be/~/media/files/Elia/StakeholderDay/Elia-Vision-paper-2018_Front-Spreads-Back.pdf>`__," Elia Group, Brussels, Belgium, 2018.
8. Erbach, G., "`Understanding electricity markets in the EU <https://www.europarl.europa.eu/thinktank/en/document.html?reference=EPRS_BRI%282016%29593519>`__," European Union, Briefing, November 2016.
9. Glismann, S., "Modelling from a TSO Perspective - TenneT NL," 6 September 2018.
10. Pfenninger, S., Hawkes, A., and Keirstead, J., "`Energy systems modeling for twenty-first century energy challenges <https://doi.org/10.1016/j.rser.2014.02.003>`__," Renewable and Sustainable Energy Reviews, vol. 33, pp. 74–86, May 2014.
11. "`Energy modelling - EU Reference Scenario 2016 <https://data.europa.eu/euodp/data/dataset/energy-modelling>`__."
12. Joskow, P. L., "`Comparing the Costs of Intermittent and Dispatchable Electricity Generating Technologies <https://doi.org/10.1257/aer.101.3.238>`__," American Economic Review, vol. 101, no. 3, pp. 238–241, May 2011.
13. Tidball, R., Bluestein, J., Rodriguez, N., Knoke, S., and Macknick, J., "`Cost and Performance Assumptions for Modeling Electricity Generation Technologies <https://www.osti.gov/biblio/993653/>`__," National Renewable Energy Laboratory, Subcontract Report NREL/SR-6A20-48595, 2010.
14. Pinson, P., "Renewables in Electricity Markets."
15. "`The current electricity market design in Europe <https://set.kuleuven.be/ei/factsheets>`__," KU Leuven Energy Institute, Heverlee, Belgium, January 2015.
16. "`Overview of European Electricity Markets <https://ec.europa.eu/energy/data-analysis/energy-modelling/metis_en>`__," European Union, Brussels, Belgium, February 2016.
17. Herbst, A., Toro, F., Reitze, F., and Jochem, E., "`Introduction to Energy Systems Modelling <https://doi.org/10.1007/BF03399363>`__," Swiss Journal of Economics and Statistics, vol. 148, no. 2, pp. 111–135, April 2012.
18. Krook-Riekkola, A., "`National Energy System Modelling for Supporting Energy and Climate Policy Decision-making: The Case of Sweden <http://urn.kb.se/resolve?urn=urn:nbn:se:ltu:diva-17594>`__," Chalmers University of Technology, Göteborg, Sweden, 2015.
19. "`Managing big data for smart grids and smart meters <http://www.ibmbigdatahub.com/whitepaper/managing-big-data-smart-grids-and-smart-meters>`__," IBM Corporation, Somers, NY, USA, 2012.
