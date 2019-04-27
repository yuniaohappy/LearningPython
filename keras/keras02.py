from keras.datasets import mnist
from keras.layers import Dense,Dropout
from keras.models import Sequential

((x_train,y_train),(x_test,y_test)) = mnist.load_data()
x_train = x_train.reshape(60000,784)