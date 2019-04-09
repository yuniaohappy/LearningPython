import tensorflow as tf
import numpy as np

W = tf.Variable(tf.random_uniform([1],-1.0,1.0),name='W')
b = tf.Variable(tf.zeros([1]),name='b')
save = tf.train.Saver()
with tf.Session() as sess:
    save.restore(sess,'./save_model/LinerR_model.ckpt')
    x = input("请输入数字：")
    res = sess.run(W) * int(x) + sess.run(b)
    # print(type(res[0]))
    rou = np.around(res,2)
    print("模型结果：",rou.__str__())
    print("实际结果：" ,str(0.1 * int(x) + 0.3))
