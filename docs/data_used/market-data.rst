Electricity market data
=======================

Day-ahead market prices
-----------------------

In the :term:`ENTSO-E TP`, the day-ahead prices are published for each bidding zone at every market time unit, in the relevant currency per MWh. It is published no later than an hour after gate closure. In case of implicit allocation, the gate closure time is interpreted as the output time of the matching algorithms. The data is primarily owned and provided to the :term:`ENTSO-E TP` by power exchanges or :term:`TSO`\s. This dataset is available at hourly resolution.

Electricity market operators
----------------------------

Nord Pool
~~~~~~~~~

Nord Pool publishes market data on their website [NordPool]_. However, these are not available under open licenses and the :term:`API` is only available to their customers [NordPoolb]_ [NordPoolc]_. Automatic extraction of data is also not permitted, as stated in the excerpt from their terms and conditions below [NordPoolb]_:

   *Nord Pool does not permit automatic extraction of data or other usage that reduces the performance of the website. Any such extraction or usage will lead to the user being blocked from the website without further notice.*

As a result, this project will only utilise the market data available on :term:`ENTSO-E TP` and any other sources where data are available for reuse.
