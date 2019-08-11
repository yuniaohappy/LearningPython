import tensorflow as tf

LEANING_RATE_BASE = 0.5
LEANING_RATE_DECAY = 0.99
LEANING_RATE_STEP = 1

global_step = tf.Variable(0,trainable=False)
# 指数衰减学习率
leaning_rate = tf.train.exponential_decay(LEANING_RATE_BASE,global_step,LEANING_RATE_STEP,LEANING_RATE_DECAY,staircase=True)

w = tf.Variable(tf.constant(5,dtype=tf.float32))
loss = tf.square(w + 1)
train = tf.train.GradientDescentOptimizer(leaning_rate).minimize(loss,global_step=global_step)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    for i in range(40):
        sess.run(train)
        w1 = sess.run(w)
        loss1 = sess.run(loss)
        print("Steps {} w is {} loss is {}".format(i,w1,loss1))
