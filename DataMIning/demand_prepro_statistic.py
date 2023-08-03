from cProfile import label
from turtle import width
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


names=range(0,1095)

name = [str(x) for x in names]
df_demand_list=[]

mean_list_cd=[]
mean_list_da=[]
mean_list_ha=[]

for i in range(1095):
    df=pd.read_csv("C://Users//poulcheria//Desktop//DataMining//Data//demand//"+name[i]+".csv")
    df=df.fillna(df.mean()) #fill in NaN with the mean of collumn
    df_demand_list.append(df)
    

final_df=pd.concat(df_demand_list)

#final_df.to_csv("C://Users//poulcheria//Desktop//DataMining//Data//demand_merged.csv")
#print(final_df)

df_2019=final_df[0:105485]
df_2020=final_df[105485:210970]
df_2021=final_df[210970:3163456]
describe_df2019=df_2019.describe()
print(describe_df2019)
describe_df2020=df_2020.describe()
print(describe_df2020)
describe_df2021=df_2021.describe()
print(describe_df2021)

mean_list=describe_df2019.iloc[1].to_list()
std_list=describe_df2019.iloc[2].to_list()
min_list=describe_df2019.iloc[3].to_list()
perc25_list=describe_df2019.iloc[4].to_list()
perc50_list=describe_df2019.iloc[5].to_list()
perc75_list=describe_df2019.iloc[6].to_list()
max_list=describe_df2019.iloc[7].to_list()




values1=[mean_list[i] for i in range (2)]
values2=[std_list[i] for i in range (2)]
values3=[min_list[i] for i in range (2)]
values4=[perc25_list[i] for i in range (2)]
values5=[perc50_list[i] for i in range (2)]
values6=[perc75_list[i] for i in range (2)]
values7=[max_list[i] for i in range (2)]

mean_list2=describe_df2020.iloc[1].to_list()
std_list2=describe_df2020.iloc[2].to_list()
min_list2=describe_df2020.iloc[3].to_list()
perc25_list2=describe_df2020.iloc[4].to_list()
perc50_list2=describe_df2020.iloc[5].to_list()
perc75_list2=describe_df2020.iloc[6].to_list()
max_list2=describe_df2020.iloc[7].to_list()




val1=[mean_list2[i] for i in range (2)]
val2=[std_list2[i] for i in range (2)]
val3=[min_list2[i] for i in range (2)]
val4=[perc25_list2[i] for i in range (2)]
val5=[perc50_list2[i] for i in range (2)]
val6=[perc75_list2[i] for i in range (2)]
val7=[max_list2[i] for i in range (2)]

mean_list3=describe_df2021.iloc[1].to_list()
std_list3=describe_df2021.iloc[2].to_list()
min_list3=describe_df2021.iloc[3].to_list()
perc25_list3=describe_df2021.iloc[4].to_list()
perc50_list3=describe_df2021.iloc[5].to_list()
perc75_list3=describe_df2021.iloc[6].to_list()
max_list3=describe_df2021.iloc[7].to_list()





vals1=[mean_list3[i] for i in range (2)]
vals2=[std_list3[i] for i in range (2)]
vals3=[min_list3[i] for i in range (2)]
vals4=[perc25_list3[i] for i in range (2)]
vals5=[perc50_list3[i] for i in range (2)]
vals6=[perc75_list3[i] for i in range (2)]
vals7=[max_list3[i] for i in range (2)]


plt.plot(values1 ,label="2019")
plt.plot(val1,label="2020")
plt.plot(vals1,label="2021")
plt.xlabel("Time")
plt.ylabel("Mean")
plt.show()

plt.plot(values2,label='2019')
plt.plot(val2,label='2020')
plt.plot(vals2,label='2021')
plt.xlabel("Time")
plt.ylabel("Std")
plt.show()

plt.plot(values3,label='2019')
plt.plot(val3,label='2020')
plt.plot(vals3,label='2021')
plt.xlabel("Time")
plt.ylabel("Min")
plt.show()

plt.plot(values4,label='2019')
plt.plot(val4,label='2020')
plt.plot(vals4,label='2021')
plt.xlabel("Time")
plt.ylabel("25%")
plt.show()

plt.plot(values5,label='2019')
plt.plot(val5,label='2020')
plt.plot(vals5,label='2021')
plt.xlabel("Time")
plt.ylabel("50%")
plt.show()

plt.plot(values6,label='2019')
plt.plot(val6,label='2020')
plt.plot(vals6,label='2021')
plt.xlabel("Time")
plt.ylabel("75%")
plt.show()

plt.plot(values7,label='2019')
plt.plot(val7,label='2020')
plt.plot(vals7,label='2021')
plt.xlabel("Time")
plt.ylabel("Max")
plt.show()

