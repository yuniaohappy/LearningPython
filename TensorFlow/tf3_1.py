import tensorflow as tf
import numpy as np
SEED = 23455
STEPS = 30000
LEARN_RATE = 0.001

rns = np.random.RandomState(SEED)
x_ = rns.rand(32,2)
y_ = [[int(x0 + x1 < 1)] for x0,x1 in x_]
print(x_)
print(y_)

X = tf.placeholder(tf.float32,shape=(None,2))
Y = tf.placeholder(tf.float32,shape=(None,1))

w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

a = tf.matmul(X,w1)
y = tf.matmul(a,w2)
# Y = W * X + b

loss = tf.reduce_mean(tf.square(y - y_))
train = tf.train.GradientDescentOptimizer(LEARN_RATE).minimize(loss)
# train = tf.train.MomentumOptimizer(LEARN_RATE,0.9).minimize(loss)
# train = tf.train.AdamOptimizer(LEARN_RATE).minimize(loss)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(STEPS):
        # start = (i * 8) % 32
        # end = start + 8
        sess.run(train, feed_dict={X:x_,Y:y_})
        if i % 50 == 0:
            total_loss = sess.run(loss,feed_dict={X:x_,Y:y_})
            # total_train = sess.run(train,feed_dict={X:x_,Y:y_})
            print("损失函数为：" ,total_loss)
    print("w1:" ,sess.run(w1))
    print("w2",sess.run(w2))