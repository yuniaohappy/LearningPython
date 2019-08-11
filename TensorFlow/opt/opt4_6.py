import tensorflow as tf

w1 = tf.Variable(0,dtype=tf.float32)
global_step = tf.Variable(0,trainable=False)
MOVING_AVERAGE_DECAY = 0.99
ema = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY,global_step)
ema_op = ema.apply(tf.trainable_variables())

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run([w1,ema.average(w1)]))
    sess.run(tf.assign(w1,1))
    sess.run(ema_op)

    print(sess.run([w1, ema.average(w1)]))
    sess.run(tf.assign(global_step,100))
    sess.run(tf.assign(w1,10))
    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))

    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))

    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))

    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))

    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))

    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))

    sess.run(ema_op)
    print(sess.run([w1, ema.average(w1)]))


