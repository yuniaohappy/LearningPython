import tensorflow as tf
import numpy as np
from keras.layers import activations
tf.nn.relu

SEED = 25535
STEPS = 10000
RATE = 0.001
rng = np.random.RandomState(SEED)

x_ = rng.rand(50,2)
y_ = [[int((m + n) < 1)] for m,n in x_]
print(x_)
print(y_)

x = tf.placeholder(tf.float32,shape=(None,2))
y = tf.placeholder(tf.float32,shape=(None,1))
w = tf.Variable(tf.random_normal([2,3],dtype=tf.float32))
b = tf.Variable(tf.random_normal([3,1],dtype=tf.float32))
a = tf.matmul(x,w)
Y = tf.matmul(a,b)
loss = tf.reduce_mean(tf.square(Y-y_))
train = tf.train.GradientDescentOptimizer(RATE).minimize(loss)
train = tf.train.MomentumOptimizer(RATE,momentum=0.9).minimize(loss)
train = tf.train.AdamOptimizer(RATE).minimize(loss)
init = tf.global_variables_initializer()
dx = {x: x_, y: y_}
with tf.Session() as sess:
    sess.run(init)
    sess.run(train,feed_dict=dx)
    for i in range(STEPS):
        if i % 50 == 0:
            # print("Y:",sess.run(Y,feed_dict=dx))
            print("loss is :",sess.run(loss,feed_dict=dx))
    print("w:",sess.run(w))
    print("b:",sess.run(b))

