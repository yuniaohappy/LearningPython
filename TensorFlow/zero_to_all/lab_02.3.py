import tensorflow as tf

W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

h = W * x + b
loss = tf.reduce_sum(tf.square(h - y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(loss)

x_data = [1,2,3,4]
y_data = [0,-1,-2,-3]

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for steps in range(1000):
    sess.run(train,feed_dict={x:x_data, y:y_data})

curr_W,curr_b,curr_loss = sess.run([W, b, loss], feed_dict={x:x_data, y:y_data})
print("W: %s, b: %s, loss: %s " % (curr_W,curr_b,curr_loss))