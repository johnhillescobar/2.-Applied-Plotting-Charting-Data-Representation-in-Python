import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

np.random.seed(12345)

df_invert = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])

# calculate mean m and margin of error yerr for each of the rows in the data frame
# PS. yerr =the margin of error
df = df_invert.T
mean_df = df.mean()
yerr_df = 1.96* (df.std()/np.sqrt(len(df)))

y_axis_value = 35315

prob_map = {}
for year in [1992, 1993, 1994, 1995]:
    mean_value = mean_df[year]
    yerr = yerr_df[year]
    lower_limit = mean_value - yerr
    upper_limit = mean_value + yerr
    if y_axis_value < lower_limit:
        prob = 1
    elif y_axis_value > upper_limit:
        prob = 0
    else:
        prob = min(abs(mean_value-y_axis_value)/yerr, 1)
    prob_map[year] = prob

df_prob_map = pd.Series(prob_map)

prob_range =  df_prob_map.values #np.array([1, 0.5, 0])
colors = cm.RdBu(prob_range/float(max(prob_range)))
plot = plt.scatter(prob_range, prob_range, c=prob_range, cmap='RdBu')
plt.clf()
plt.colorbar(plot)
plt.bar(df_prob_map.index, mean_df.values, color=colors)
plt.xticks(df_prob_map.index, [str(i) for i in df_prob_map.index])


line, = plt.plot(plt.xlim(), [y_axis_value, y_axis_value], 'k-', color=(0,0,1,.5), lw=3, label="_not in legend")

plt.gca().set_title('Mean of given sample with color map of probabilist occurance considering confidence intervals')
plt.show()
