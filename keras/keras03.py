from keras.layers import Dense,Dropout,LSTM
from keras.models import Model,Sequential
import numpy as np
import matplotlib.pyplot as plt

x_train = np.random.random((1000,100))
y_train = np.random.randint(2,size=(1000,1))

model = Sequential()
model.add(Dense(32,input_dim=100,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])
history = model.fit(x_train,y_train,epochs=200,batch_size=32)
# print(history.__dict__)
plt.plot(history.epoch,history.history['acc'])
# plt.hist(history.epoch,history.history['acc'])
# print(history.history['acc'])
# print(history.epoch)
plt.show()