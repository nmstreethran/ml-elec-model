# import libraries
import geopandas
import matplotlib.pyplot as plt
import pandas as pd

# root url for NO and SE bidding zone polygons from tmrowco
url = 'https://raw.githubusercontent.com/tmrowco/electricitymap-contrib/master/web/third_party_maps/'

# list of zones
urlList = ['NO-NO1', 'NO-NO2', 'NO-NO3', 'NO-NO4', 'NO-NO5',
    'SE-SE1', 'SE-SE2', 'SE-SE3', 'SE-SE4']

# create an empty list and dictionary to store geo dataframes
dfList = []
urlDict = {}

# read geojson files for each zone and store them in the list
for zone in urlList:
    urlDict[zone] = geopandas.read_file(url + zone + '.json')
    dfList.append(urlDict[zone])

# concatenate the geo dataframes
rdf = geopandas.GeoDataFrame(pd.concat(dfList, ignore_index=True),
    crs=dfList[0].crs)
print(rdf)

# plot the zones
rdf.plot()
plt.show()
