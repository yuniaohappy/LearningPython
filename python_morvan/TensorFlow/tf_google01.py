import tensorflow as tf

w1 = tf.Variable([[0.2, 0.1, 0.4], [0.3, -0.5, 0.2]])
w2 = tf.Variable([[0.6], [0.1], [-0.2]])
x = tf.constant([[0.7, 0.9]])
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

with tf.Session() as sess:
    sess.run(w1.initializer)
    sess.run(w2.initializer)
    writer = tf.summary.FileWriter("D:\\Python\\TensorBoard\\2018-09-16", sess.graph)
    print(sess.run(y))
