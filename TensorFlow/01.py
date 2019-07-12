import tensorflow as tf
from sklearn import datasets

iris = datasets.load_iris()
# print(iris)
# a = tf.constant([[1,2,3],
#                  [4,5,6]])
# b = tf.constant([[7,8,9],
#                  [10,11,12]])
a = tf.constant([1,2,3,4,5,6])
b = tf.constant([7,8,9,10,11,12])
res = a + b
with tf.Session() as sess:
    print(sess.run(res))