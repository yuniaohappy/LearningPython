import tensorflow as tf

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

# z = x + y
z = tf.add(x, y)
with tf.Session() as sess:
    z = z*3
    print(sess.run(z,feed_dict={x:[3.0,5.0],y:4.0}))

# node1 = tf.constant(3.0, dtype=tf.float32,name="node1")
# node2 = tf.constant(4.0,dtype=tf.float32,name="node2")
#
# node3 = tf.add(node1, node2)
# print(node3)
#
# sess = tf.Session()
# print(sess.run([node1, node2]))
# print(sess.run(node3))
