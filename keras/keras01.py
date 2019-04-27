from keras.models import Sequential
from keras.layers import Dense
from keras.losses import categorical_crossentropy
import numpy as np

x_train = np.arange(150).reshape(50,3)
y_train = np.arange(50)

model = Sequential()
model.add(Dense(units=32,activation='relu',input_dim=3))
model.add(Dense(units=1,activation='relu'))

# model.compile(loss=keras.losses.categorical_crossentropy,
#               optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))
model.compile(loss='sparse_categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])
# model.compile(loss=categorical_crossentropy,optimizer=keras.optimizers.SGD(lr=0.01,momentum=0.9,nesterov=True))
# model.fit(x_train,y_train,epochs=50,batch_size=32)
model.train_on_batch(x_train,y_train)
# loss_and_metrcis = model.evaluate()
