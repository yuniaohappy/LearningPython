import tensorflow as tf

w = tf.Variable(tf.constant(3,dtype=tf.float32))
loss = tf.square(w + 1)

train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(40):
        sess.run(train)
        w1 = sess.run(w)
        loss1 = sess.run(loss)
        print("w: ",w1," loss: ",loss1)