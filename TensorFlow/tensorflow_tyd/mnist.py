import tensorflow as tf
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
from tensorflow.examples.tutorials.mnist import input_data

matplotlib.rcParams['font.family'] = 'SimHei'

mnist = input_data.read_data_sets('data/',one_hot=True)
# print("type of mnist is %s" % (type(mnist)))
# print(mnist.train.num_examples)
# print(mnist.test.num_examples)
trainimg = mnist.train.images
trainlabel = mnist.train.labels
testimg = mnist.test.images
testlabel = mnist.test.labels

# print("trainimg类型：",type(trainimg))
# print("trainlabel类型：",type(trainlabel))
# print("testimg类型：",type(testimg))
# print("testlabel类型：",type(testlabel))

# print("trainimg形状：",trainimg.shape)
# print("trainlabel形状：",trainlabel.shape)
# print("testimg形状：",testimg.shape)
# print("testlabel形状：",testlabel.shape)
# print(trainimg[0])
# print(trainlabel[0])
# print(trainimg.shape[0])

nsample = 5
randidx = np.random.randint(trainimg.shape[0],size=nsample)
for i in randidx:
    curr_img = np.reshape(trainimg[i,:],(28,28))
    print(len(trainimg[i]))
    curr_label = np.argmax(trainlabel[i,:])
    # plt.matshow(curr_img,cmap=matplotlib.cm.binary,interpolation='nearest')
    plt.imshow(curr_img, cmap=plt.get_cmap('gray'))
    # t = "第" + str(curr_img) + "张图片标签是：" + str(curr_label)
    t = "" + str(i) + "th Training Data "  + "Label is " + str(curr_label)
    plt.title(t)
    print("第",str(i),"张图片标签是：" ,str(curr_label))
    plt.show()

batch_size = 100
batch_xs,batch_ys = mnist.train.next_batch(batch_size)
print ("type of 'batch_xs' is %s" % (type(batch_xs)))
print ("type of 'batch_ys' is %s" % (type(batch_ys)))
print ("shape of 'batch_xs' is %s" % (batch_xs.shape,))
print ("shape of 'batch_ys' is %s" % (batch_ys.shape,))











