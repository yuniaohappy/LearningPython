import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = []
y_data = []
for i in range(1000):
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1*0.1 + 0.3 + np.random.normal(0.0,0.03)
    x_data.append(x1)
    y_data.append(y1)

# plt.scatter(x_data,y_data)
# plt.show()
W = tf.Variable(tf.random_uniform([1],-1.0,1.0),name='W')
b = tf.Variable(tf.zeros([1]),name='b')
y = W * x_data + b

loss = tf.reduce_mean(tf.square(y - y_data),name='loss')
optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(loss,name='train')
init = tf.global_variables_initializer()
save = tf.train.Saver()
with tf.Session() as sess:
    sess.run(init)
    print("W =", sess.run(W), "b =", sess.run(b), "loss =", sess.run(loss))
    tf.summary.FileWriter("./tf_log", sess.graph)
    for i in range(100):
        resault = sess.run(train)
        # writer.add_summary(resault)
        print("W =", sess.run(W), "b =", sess.run(b), "loss =", sess.run(loss))

    save.save(sess,"./save_model/LinerR_model.ckpt")


    # plt.scatter(x_data,y_data,c='r')
    # plt.plot(x_data,sess.run(W) * x_data + sess.run(b))
    # plt.show()


    # writer = tf.train.SummaryWriter("./tf_log",sess.graph)

