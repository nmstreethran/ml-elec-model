#%%
from scipy import spatial
import pandas as pd

#%%
tso = pd.read_csv('data/power/installed/TransnetBW.csv', encoding='utf-8')
postcodes = pd.read_csv('data/geography/postcodes/postcodesDE.csv', encoding='utf-8')
wind = pd.read_csv('data/meteorology/wind/stations.csv', encoding='utf-8')

#%%
postcodes = postcodes.drop_duplicates(['postal_code'])

#%%
tso_merged = pd.merge(tso, postcodes, on=['postal_code'], how='left')




# airports = [(10,10),(20,20),(30,30),(40,40)]
# tree = spatial.KDTree(airports)
# tree.query([(21,21)])

# x, y = np.mgrid[0:5, 2:8]

# tree = spatial.KDTree(list(zip(x.ravel(), y.ravel())))
# pts = np.array([[0, 0], [2.1, 2.9]])

# tree.query(pts)
# (array([ 2.        ,  0.14142136]), array([ 0, 13]))

# tree.query(pts[0])

# %%
