import tensorflow as tf

x_train = [1,2,3]
y_train = [1,2,3]
# y = W*x + b
W = tf.Variable(tf.random_normal([1]),name="weight")
b = tf.Variable(tf.random_normal([1]),name="biase")

# y = tf.matmul(W,x_train) + b
y = W * x_train + b
loss = tf.reduce_mean(tf.square(y - y_train))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for steps in range(2000):
        if steps % 20 == 0:
            print(steps,sess.run(loss),"\t",sess.run(W),"\t",sess.run(b))

