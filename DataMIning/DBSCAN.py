import pandas as pd
from sklearn.cluster import DBSCAN
import numpy as np


df = pd.read_csv ("Data/source_merged.csv")  # available sources 
df2=pd.read_csv("Data/demand_merged.csv")   

df=df.drop(columns=['Time'])
df=df.drop(df.columns[0], axis=1)

df2=df2.drop(columns=['Time'])
df2=df2.drop(df2.columns[0], axis=1)


df=df.fillna(df.mean()) #fill in NaN with the mean of collumn
df2=df2.fillna(df.mean())
print(df[:100])
print(df2[:100])


df=df[:40000]
df2=df2[:40000]


#df_list = df.values.tolist() #df to list

source_arr=df.to_numpy()


#df2_list = df2.values.tolist() #df2 to list
demand_arr=df2.to_numpy()


DBSCAN_source =DBSCAN(eps=2000,min_samples=25).fit(source_arr)
labels = DBSCAN_source.labels_
sources_lables = DBSCAN_source.labels_
#print(sources_lables)
# = np.array(sources_lables) == -1
outliers_index = np.where(sources_lables == -1)
print(outliers_index)
outliers_index = np.array(outliers_index).tolist()
outliers=[]
for line in outliers_index:
    for i in line:
        outliers.append(source_arr[i])

print("SOURCES OUTLIERS")

print(outliers)


DBSCAN_source =DBSCAN(eps=800,min_samples=5).fit(demand_arr)
labels = DBSCAN_source.labels_
sources_lables = DBSCAN_source.labels_
print(sources_lables)
# = np.array(sources_lables) == -1
outliers_index2 = np.where(sources_lables == -1)
print(outliers_index2)
outliers_index2 = np.array(outliers_index2).tolist()
outliers2=[]
for line in outliers_index2      :
    for i in line:
        outliers2.append(demand_arr[i])

print("DEMAND OUTLIERS")
print(outliers2)

