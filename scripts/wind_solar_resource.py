# %%
# import libraries
import pandas as pd
import os
import errno
import requests
# import glob
import zipfile
import io
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# define data range and station
start = "20100101"
end = "20191231"
station = "13901"

# download url
url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/10_minutes/wind/historical/10minutenwerte_wind_" + station + "_" + start + "_" + end + "_hist.zip"

# download path
path = "data/met/de/wind/10min"

# create download directory
try:
    os.makedirs(path)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print ("\nBE CAREFUL! Directory %s already exists." % path)

# extract zip file
try:
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(path)
    # exception if no zip file exists
except zipfile.BadZipFile:
    print ("This dataset does not exist")

# read file as pandas dataframe
file = "produkt_zehn_min_ff_" + start + "_" + end + "_" + station + ".txt"
wind = pd.read_csv(path + file, sep=";")

# tanslate column titles to English
wind = wind.set_axis([
    "station_id", "timestamp", "QLoNC", "mean_wind_speed",
    "mean_wind_direction", "end_of_record"],
    axis="columns", inplace=False)

# convert timestamp to datetime
wind["timestamp"] = pd.to_datetime(wind["timestamp"], format="%Y%m%d%H%M")

# handle missing values
# if speed is -999, replace with value above

# #Declare the array containing the series you want to plot. 
# #For example:
# time_series_array = np.sin(np.linspace(-np.pi, np.pi, 400)) + np.random.rand((400))
# n_steps           = 15 #number of rolling steps for the mean/std.

# #Compute curves of interest:
# time_series_df = pd.DataFrame(time_series_array)
# smooth_path    = time_series_df.rolling(n_steps).mean()
# path_deviation = 2 * time_series_df.rolling(n_steps).std()

# under_line     = (smooth_path-path_deviation)[0]
# over_line      = (smooth_path+path_deviation)[0]

# #Plotting:
# plt.plot(smooth_path, linewidth=2) #mean curve.
# plt.fill_between(path_deviation.index, under_line, over_line, color="b", alpha=.1) #std curves.