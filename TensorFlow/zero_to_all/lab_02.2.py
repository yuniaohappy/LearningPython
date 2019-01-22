import tensorflow as tf

W = tf.Variable(tf.random_normal([1]),name="weight")
b = tf.Variable(tf.random_normal([1]),name="bias")

X = tf.placeholder(tf.float32,shape=[None])
Y = tf.placeholder(tf.float32,shape=[None])

hypothesis = W * X + b

loss = tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)

train = optimizer.minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for steps in range(1000):
        if steps % 10 == 0:
            loss_val,W_val,b_val,train_val = sess.run([loss,W,b,train],feed_dict={X:[1,2,3],Y:[1,2,3]})
            # print(steps, loss_val, W_val, b_val, train_val)

            print(sess.run(hypothesis, feed_dict={X: [5]}))
            print(sess.run(hypothesis, feed_dict={X: [2.5]}))
