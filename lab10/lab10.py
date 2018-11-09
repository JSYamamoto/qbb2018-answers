#!/usr/bin/env python3

"""
conda activate py3
"""

import sys
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy import stats
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data= pd.read_csv('hema_data.txt',sep="\t",index_col='gene')
df=pd.DataFrame(data)
df_array=np.array(df)

#print (df["CFU"])
print (df.iloc[[0]])
cmap=sns.diverging_palette(220,20,sep=20,as_cmap=True)

ax=sns.clustermap(df, cmap=cmap)
#fig.tight_layout()
# plt.show()
ax.savefig("Heatmap.png")
# plt.close(ax)
 
 
kmeans=KMeans(n_clusters=6)
kmeans.fit(df)
y_kmeans=kmeans.predict(df)

plt.figure()
plt.title("k_means")
plt.scatter(df["CFU"], df['poly'], c=y_kmeans,s=5,cmap='viridis')
plt.ylabel("poly expression")
plt.xlabel("CFU expression")
plt.savefig("test_kmeans.png")
plt.close()