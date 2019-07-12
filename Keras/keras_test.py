from keras.models import Model,Sequential
from keras.layers import Dense
import numpy as np
import tensorflow as tf

x = np.arange(150).reshape(50,3)
y = np.arange(50)

model = Sequential()
model.add(Dense(3,input_shape=(50,3),batch_size=10))
model.add(Dense(1,activation='relu'))
model.compile(optimizer='sgd',loss='mse')
history = model.fit(x,y)
print(history)
