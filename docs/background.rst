Background
==========

The energy transition
---------------------

The transition towards a future low-carbon economy is driven globally by the Paris Agreement, which recognises the need for sustainable development worldwide to counter the threats of climate change. The European Union (EU) is committed to reduce greenhouse gas (GHG) emissions by 2050 to 80-90 % below 1990 levels. As the energy industry is responsible for the highest share of anthropogenic GHG emissions, importance is placed on how changes in energy systems can help achieve these GHG emission reduction targets.

A number of opportunities exist for the decarbonisation of the energy industry. The International Renewable Energy Agency, in their renewable energy roadmap study, has identified renewable energy as having the highest potential in reducing energy-related carbon dioxide emissions globally, which is closely followed by energy efficiency and electrification with renewable energy. In a 2018 political agreement, the EU member states agreed upon a target of at least 32 % of the demand being met with renewables by 2030, through national targets of the individual member states. The electricity demand in the transport sector is also expected to increase due to expected petrol and diesel engine bans and subsequently the electrification of road transport.

Conventional energy resources, such as fossil fuels, biomass, hydro, geothermal, and nuclear fuels are non-variable. Fossil fuels, including coal, natural gas, and oil, as well as nuclear, are non-renewable. While nuclear, biomass, hydro, and geothermal energy are clean and/or renewable, generating power from fossil fuels or hydrocarbons involve combustion, which is a process that releases carbon dioxide and harmful by-products, such as soot. Fossil fuels are still extensively used and depended upon in industries around the world, including transport, chemicals, and power generation. As a result, the focus of the energy transition is to move away from fossil fuels to cleaner energy resources and technologies, including variable renewable energy (VRE) resources such as solar and wind. According to the EU reference scenario 2016, wind and solar energy resources are expected to generate a total of 35 % of EU's electricity by 2050, which is a significant increase (23 %) from 2015 levels. Conversely, generation from nuclear and solids, which are not variable and provide base load generation, are expected to decrease significantly.

While fossil fuels can be stored, transported, combusted, and converted into more useful forms of energy when there is a demand, generation from VRE resources cannot be controlled to follow consumption patterns in the same way. VRE resources are intermittent as they are dependent on atmospheric conditions, such as cloud cover and wind speed. They also have variations temporally (time-based) and spatially (location-based). This is a challenge to energy system operators, whose objective is to reliably and securely meet the energy needs at all times.

The energy system is also transitioning towards a decentralised system with more consumer participation and new forms of flexibilities, including sector coupling, demand-side management, energy conversion and storage, cross-border interconnection, and curtailment. This allows demand patterns to shift to better suit the generation patterns in systems with high penetration of VRE resources, such as solar and wind. This decentralised, flexible, and renewable energy system is more complex than traditional centralised systems, and require improved decision making processes for an optimal system operation. As the energy system is also becoming "smart", the system will have an increasing amount of sensors and controllers that continuously record measurements of the system. Advancements in these technologies mean that data that is fast, heterogeneous and high in volume from the energy system will be generated. This provides an opportunity to exploit data with these characteristics to gain insights on the energy system, which can then be converted to strategies that optimise the system.

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

Existing models and tools
-------------------------

Ringkjøb, et al. reviewed a comprehensive list of energy systems models for systems with large shares of VRE generation. They have classified existing energy systems models based on the developer, software availability (i.e., open-source, commercial), software type (e.g., stand-alone, General Algebraic Modeling System (GAMS)), purpose (e.g., power system analysis, scenario-based), modelling approach (bottom-up, top-down, hybrid), methodology (e.g., optimisation, simulation), temporal resolution, modelling horizon and spatial coverage. Additionally, information regarding the available conventional and renewable generation technologies, storage options, grid, demand sectors, demand elasticity, demand response, costs, market and emissions are provided.

Among the models listed by Ringkjøb, et al. are The Integrated MARKAL-EFOM System (TIMES) and MARKet ALlocation (MARKAL). The MARKAL and TIMES family of models, developed by the Energy Technology Systems Analysis Program (ETSAP) of the International Energy Agency (IEA), are bottom-up models that can generate economic models providing technology-rich basis for representing energy dynamics over a multi-period time horizon for local, national, multi-regional and global energy systems. Bottom-up models, also known as techno-economic or process-oriented models, have "relatively high degree of technological detail used to assess future energy demand and supply" and "use a business economics approach for the economic evaluation of the technologies simulated". ETSAP reports that the MARKAL and TIMES models are being used by over 150 teams in 50 countries. Although widely used, these models focus on long time horizons and only perform a simplified supply and demand analysis for the electricity market and lack the detail to properly represent short-term fluctuations of VRE, making them unsuitable for operational planning. Additionally, TIMES was only recently (in January 2020) released under an open source GNU General Public License, but still requires the proprietary GAMS language, solvers, and VEDA set of tools.

The methods used for forecasting in industry are commercial tools developed and maintained by energy consultancies, provide paid support to their customers. These models perform forecasting mainly using statistical and stochastic methods. Due to these tools being closed-source, no documentation or detailed information regarding these models are available publicly.

Transmission system operators (TSOs) make use of internal and commercial modelling tools when it comes to forecasting VRE generation and demand. Example of commercial tools used for VRE forecasting by TSOs in Great Britain include AWS Truepower, GH Forecaster (Garrad Hassan, now DNV-GL), PowerSight Wind Forecasting System (3Tier), Forecasting Tool (Element Energy) and Load Profile Modelling (Grid Scientific).

AWS Truepower has a range of software for the operation of renewable energy projects, which includes
access to time series measurements of wind and meteorological data at any time, a dashboard with
visualisation of data, the ability to download data files, statistics and plot graphs, and support from the company’s consulting team.

DNV-GL’s short-term energy forecasting service is provided to wind and solar power plant operators. It is comprised of several forecasters, which has the ability to predict hourly wind and solar conditions up to 15 days in advance and update as quickly as every five minutes. The raw data can be provided in the plant operator’s choice of format. The service also includes interactive visualisation of data, both forecasts and historical measurements, and monthly reports and summaries.

Element Energy is a specialist consultancy that has a load forecasting tool for identifying trends in future demand, generation and storage, as well as customer behaviour and technology deployment. Their forecasting model is of high resolution and is bottom-up. Apart from TSOs, DSOs are also able to use this model for scenario-based cost-benefit analysis, as the grid flexibilities and smart grid services, including demand response and electric vehicle charging, are modelled in detail.

Grid Scientific is a consultancy offering services related to information and communication technology and smart grids. No information regarding their Load Profile Modelling tool was available.

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

The actors in the electricity market include generators, retailers, large and small consumers, TSOs, distribution network operators (DNOs), balance responsible parties (BRPs), aggregators, regulators, and market operators.

There are two types of electricity markets; the retail market and the wholesale market. The retail market involves the retailers buying electricity from generators and selling it to consumers. The wholesale market involves generators, retailers and (large) consumers, who buy and sell electricity. Energy-only transactions in the wholesale market have different temporal resolutions and take place before dispatch, shown in green in the figure below. Balancing markets, shown in pink in the figure, which involve both energy and services, operate both before and after dispatch. The energy-only markets are operated by the market operator or power exchanges, while the balancing market is operated by the system operator. The day-ahead and intra-day markets can be considered short-term electricity markets, as the former takes place 24 hours in advance of dispatch, while the latter takes place continuously after the day-ahead market, up to minutes before dispatch.

.. figure:: images/market-resolution.png
    :alt: The various electricity markets in terms of operator and temporal resolution, before and after dispatch, adapted from KU Leuven Energy Institute 2015 and Pinson 2018.

    The various electricity markets in terms of operator and temporal resolution, before and after dispatch, adapted from KU Leuven Energy Institute 2015 and Pinson 2018.

In short-term electricity market auctions, such as the day-ahead market auction, generating companies have the incentive to bid as low as possible, as the supply bids are ranked in ascending order of price. Conversely, on the demand side, consumers have the incentive to bid as high as possible, as the demand bids are ranked in descending order of price. These two curves form a so called merit order, and the intersection between these two curves is the equilibrium point. The price at this equilibrium point is the market clearing price, which is what all accepted bids will receive, regardless of their initial bid. All supply and demand bids to the left of the equilibrium point will be accepted, and those to the right are rejected.

In the case of generating companies, the OPEX of their generators determine the price at which it is bid. For conventional power plants, this OPEX includes fuel costs and carbon costs (except nuclear power plants). For solar and wind power plants, the OPEX is close to zero, as they do not require fuel to run. The revenue received by generating companies in the day-ahead market for each power plant contributes towards their CAPEX. Since conventional power plants have relatively low CAPEX, and fuel costs are high, the main decision generating companies have to make in short-term electricity markets is whether it is economical to run these power plants. For solar and wind power plants, which have relatively high CAPEX, companies are interested in getting as many bids accepted and as much of the electricity generated sold as possible.

Project objective
-----------------

The focus of this project will be on the operational planning resolution of the electricity system in Europe. This is due to the potential of renewable energy and electrification using renewable energy in decarbonising the energy and transport industries, as well as to better analyse and include short-term fluctuations of renewable energy generation in energy models. VRE resources are also mainly used to generate electricity directly, i.e., wind and solar are converted into electrical energy from kinetic and light or heat energy respectively. This also provides the opportunity to utilise high resolution electricity system data and machine learning methods for forecasting and optimisation of the electricity system. The ultimate aim of this short-term decision making model is to help participants in short-term electricity (i.e., day-ahead) markets to develop operational and bidding strategies to maximise their revenue under uncertainty of VRE generation. Inputs used by the machine learning model for the day-ahead forecasts include, but are not limited to, recent historical measurements of electricity generation, demand, and market prices.

There is a need for open-source energy systems models, as most widely-used models are coded in GAMS, which has a proprietary license. According to the Open Energy Modelling (Openmod) Initiative, an active community advocating the use of open energy modelling in Europe, developing an energy system model is a lengthy process. With new technologies and intermittent renewables replacing conventional energy sources, these models play an important role in simulating such systems and developing new models would be a challenge. Being open-source allows for scientific collaboration, which makes this process more efficient, as there would be overlapping areas in the research and development of energy systems models. Although open-source models generate less rewards due to, for example, not being patented, the models would be subject to full scientific scrutiny, which results in the output being of higher quality in the long run and makes the model accessible to the wider scientific community. Therefore, this model will be fully open source, well-documented, and utilise open data to ensure full transparency and reproducibility.

References
----------

1. "`Paris Agreement <https://unfccc.int/process-and-meetings/the-paris-agreement/the-paris-agreement>`__." United Nations Framework Convention on Climate Change, 2015.
2. "`Energy roadmap 2050 <https://doi.org/10.2833/10759>`__," Publications Office of the European Union, Luxembourg, 2012.
3. "`Global Energy Transformation: A Roadmap to 2050 <https://www.irena.org/publications/2018/Apr/Global-Energy-Transition-A-Roadmap-to-2050>`__," International Renewable Energy Agency, 2018.
4. "`Renewable energy - Energy - European Commission <https://ec.europa.eu/energy/topics/renewable-energy_en>`__."
5. "`World Energy Outlook 2017 <https://www.iea.org/weo2017>`__," International Energy Agency, Paris, France, 2017.
6. Lund, H., Østergaard, P. A., Connolly, D, and Mathiesen, B. V., "`Smart energy and smart energy systems <https://doi.org/10.1016/j.energy.2017.05.123>`__," Energy, vol. 137, pp. 556–565, October 2017.
7. "`Towards a consumer-centric system <https://www.elia.be/~/media/files/Elia/StakeholderDay/Elia-Vision-paper-2018_Front-Spreads-Back.pdf>`__," Elia Group, Brussels, Belgium, 2018.
8. Erbach, G., "`Understanding electricity markets in the EU <https://www.europarl.europa.eu/thinktank/en/document.html?reference=EPRS_BRI%282016%29593519>`__," European Union, Briefing, November 2016.
9. Glismann, S., "Modelling from a TSO Perspective - TenneT NL," 6 September 2018.
10. Pfenninger, S., Hawkes, A., and Keirstead, J., "`Energy systems modeling for twenty-first century energy challenges <https://doi.org/10.1016/j.rser.2014.02.003>`__," Renewable and Sustainable Energy Reviews, vol. 33, pp. 74–86, May 2014.
11. "`Energy modelling - EU Reference Scenario 2016 <https://data.europa.eu/euodp/data/dataset/energy-modelling>`__."
12. Joskow, P. L., "`Comparing the Costs of Intermittent and Dispatchable Electricity Generating Technologies <https://doi.org/10.1257/aer.101.3.238>`__," American Economic Review, vol. 101, no. 3, pp. 238–241, May 2011.
13. Tidball, R., Bluestein, J., Rodriguez, N., Knoke, S., and Macknick, J., "`Cost and Performance Assumptions for Modeling Electricity Generation Technologies <https://www.osti.gov/biblio/993653/>`__," National Renewable Energy Laboratory, Subcontract Report NREL/SR-6A20-48595, 2010.
14. Pinson, P., "`Renewables in Electricity Markets <https://pierrepinson.com/index.php/teaching/>`__."
15. "`The current electricity market design in Europe <https://set.kuleuven.be/ei/factsheets>`__," KU Leuven Energy Institute, Heverlee, Belgium, January 2015.
16. "`Overview of European Electricity Markets <https://ec.europa.eu/energy/data-analysis/energy-modelling/metis_en>`__," European Union, Brussels, Belgium, February 2016.
17. Herbst, A., Toro, F., Reitze, F., and Jochem, E., "`Introduction to Energy Systems Modelling <https://doi.org/10.1007/BF03399363>`__," Swiss Journal of Economics and Statistics, vol. 148, no. 2, pp. 111–135, April 2012.
18. Krook-Riekkola, A., "`National Energy System Modelling for Supporting Energy and Climate Policy Decision-making: The Case of Sweden <http://ltu.diva-portal.org/smash/record.jsf?pid=diva2:990599>`__," Chalmers University of Technology, Göteborg, Sweden, 2015.
19. "`Managing big data for smart grids and smart meters <https://www.ibmbigdatahub.com/whitepaper/managing-big-data-smart-grids-and-smart-meters>`__," IBM Corporation, Somers, NY, USA, 2012.
20. Ringkjøb, H.-K., Haugan, P. M. and Solbrekke, I. M., '`A review of modelling tools for energy and electricity systems with large shares of variable renewables <https://doi.org/10.1016/j.rser.2018.08.002>`__', Renewable and Sustainable Energy Reviews, vol. 96, pp. 440–459, 1st Nov. 2018.
21. Hay, S. and Ferguson, A., '`A Review of Power System Modelling Platforms and Capabilities <https://www.theiet.org/sectors/energy/resources/modelling-reports/papers.cfm>`__, The Institution of Engineering and Technology, Mar. 2015.
22. `Software Archive - UL | Renewables <https://aws-dewi.ul.com/software/>`__.
23. `Short-term forecasting - DNV-GL <https://www.dnvgl.com/services/forecaster-introduction-3848>`__.
24. `Project Case Studies | Element Energy <http://www.element-energy.co.uk/sectors/energy-networks/project-case-studies/>`__.
25. `About Us | Grid Scientific <http://gridscientific.com/about-us/>`__.
26. `IEA-ETSAP | Optimization Modeling Documentation <https://iea-etsap.org/index.php/documentation>`__.
27. `IEA-ETSAP | Energy Systems Analysis Tools <https://iea-etsap.org/index.php/etsap-tools>`__.
28. `etsap-TIMES/TIMES_model - GitHub <https://github.com/etsap-TIMES/TIMES_model>`__.
29. `Openmod - Open Energy Modelling Initiative <http://www.openmod-initiative.org>`__.
30. Tesoriere, A., and Balletta, L., '`A dynamic model of open source vs proprietary R&D <https://doi.org/10.1016/j.euroecorev.2017.02.009>`__', European Economic Review, vol. 94, pp. 221–239, 2017.
