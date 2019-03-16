# Use the following data for this assignment:

import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])

import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap


avg = df.mean(axis=1) 

std = df.std(axis=1)/np.sqrt(df.shape[1])

# looks like max on col 1992
y = 40000

norm = Normalize(vmin=-1.96, vmax=1.96)
maps = get_cmap('seismic')
cols = pd.DataFrame([])
cols['intensity'] = [norm(x) for x in (avg-y)/std]
cols['color'] = [maps(x) for x in cols['intensity']]

plt.figure(figsize=(8,6))
bplot = plt.bar(df.index, avg, yerr=std*1.96, color=cols['color']);
hline = plt.axhline(y=y, color='k', linewidth=2, linestyle='--');

plt.xticks(df.index+0.4, ('1992', '1993', '1994', '1995'));
