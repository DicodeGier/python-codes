import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


rgb = [(255,0,255), (128,0,128)]
#colors = [tuple(t / 255 for t in x) for x in rgb]


array = np.random.random((5,5))
#print(array)
heat_map = sns.heatmap(array,cmap = rgb)
plt.show()
