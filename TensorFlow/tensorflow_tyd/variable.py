import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# w = tf.Variable([[0.5,1.0]])
# x = tf.Variable([[2.0],[1.0]])
# y = tf.matmul(w,x)
# init = tf.global_variables_initializer()
# with tf.Session() as sess:
#     sess.run(init)
#     a = sess.run(y)
#     print(y.eval())

# tf.zeros((3,4),tf.int32)
# tensor = [[1,2,3],[3,4,5]]
# tf.zeros_like(tensor)
# tf.ones([3,4],tf.int32)
# tf.ones_like(tensor)
# tensor = tf.constant([1, 2, 3, 4, 5, 6, 7])
# # tensor = tf.constant(-1.0, shape=[2, 3])
# li = tf.linspace(10.0, 12.0, 5, name="linspace")
# ran = tf.range(3, 18, 3)
# with tf.Session() as sess:
#     x = sess.run(li)
#     y = sess.run(ran)
#     plt.plot(x,y)
#     plt.show()

# norm = tf.random_normal([2,3],mean=-1,stddev=4)
# c = tf.constant([[1,2],[3,4],[5,6]])
# shuff = tf.random_shuffle(c)
# with tf.Session() as sess:
#     print(sess.run(norm))
#     print(sess.run(c))
#     print(sess.run(shuff))

# stat = tf.Variable(0)
# new_value = tf.add(stat,tf.constant(5))
# update = tf.assign(stat,new_value)
# init = tf.global_variables_initializer()
# with tf.Session() as sess:
#     sess.run(init)
#     print(sess.run(stat))
#     for _ in range(3):
#         # print(sess.run(new_value))
#         sess.run(update)
#         print(sess.run(stat))

# w = tf.Variable([[0.5,1.0]])
# x = tf.Variable([[2.0],[1.0]])
# y = tf.matmul(w,x)
# init = tf.global_variables_initializer()
# saver = tf.train.Saver()
# with tf.Session() as sess:
#     sess.run(init)
#     save_path = saver.save(sess,"./tf_test_model/")
#     print(save_path)

# a = np.zeros([3,3])
# n = tf.convert_to_tensor(a)
# with tf.Session() as sess:
#     print(sess.run(n))

# input1 = tf.placeholder(tf.float32)
# input2 = tf.placeholder(tf.float32)
# y = tf.matmul(input1,input2)
#
# with tf.Session() as sess:
#     print(sess.run([y],feed_dict={input1:tf.convert_to_tensor([7.]),input2:tf.convert_to_tensor([2.])}))

# input1 = tf.placeholder(tf.float32)
# input2 = tf.placeholder(tf.float32)
# y = tf.add(input1,input2)
#
# with tf.Session() as sess:
#     print(sess.run([y],feed_dict={input1:[7.],input2:[2.]}))




