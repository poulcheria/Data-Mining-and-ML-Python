from sqlite3 import Timestamp
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import numpy as np

# fix random seed for reproducibility
tf.random.set_seed(7)


df=pd.read_csv("C://Users//poulcheria//Desktop//DataMining//Data//source_merged.csv")
df=df.drop(columns=['Unnamed: 0','Time','Solar','Wind','Geothermal','Biomass','Biogas','Small hydro','Batteries','Imports','Other','Large Hydro',])

#print(df)

coal=df.iloc[:,0]
Nuclear=df.iloc[:,1]
Natural_Gas=df.iloc[:,2]
"""""
coal_val=[coal[i] for i in range (315351)]
Nuclear_val=[Nuclear[i] for i in range (315351)]
Natural_Gas_val=[Natural_Gas[i] for i in range (315351)]

plt.plot(coal_val,label='coal')
plt.plot(Nuclear_val,label='Nuclear')
plt.plot(Natural_Gas_val,label='Natural Gas')

plt.xlabel("Time")
plt.ylabel("None renewable resources")

#plt.show()
"""

coal = df.values
coal = coal.astype('float32')

# normalize the dataset
scaler = MinMaxScaler(feature_range=(0, 1))
coal = scaler.fit_transform(coal)


# split into train and test sets
train_size = int(len(coal) * 0.50)
test_size = len(coal) - train_size
train, test = coal[0:train_size,:], coal[train_size:len(coal),:]
print(len(train), len(test))
# convert an array of values into a dataset matrix

def create_dataset(dataset, look_back=1): 
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a=dataset[i:(i+look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return np.array(dataX), np.array(dataY)



look_back=1
coal_trainX, coal_trainY=create_dataset(train,look_back)
coal_testX, coal_testY=create_dataset(test,look_back)

trainX = np.reshape(coal_trainX, (coal_trainX.shape[0], 1, coal_trainX.shape[1]))
testX = np.reshape(coal_testX, (coal_testX.shape[0], 1, coal_testX.shape[1]))

print(trainX)
print(testX)
print(coal_trainY)
	

# create and fit the LSTM networkS
model = Sequential()
model.add(LSTM(32, input_shape=(1,look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, coal_trainY, epochs=300, batch_size=100, verbose=2)



# make predictions
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)

#print(trainPredict)
#print(testPredict)

plt.plot(trainPredict,label='trainPredict')
plt.plot(testPredict,label='testPredict')

plt.show()