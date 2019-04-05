from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
import tensorflow as tf

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
#b = tf.Variable(tf.zeros([10]))
#y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])
#cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
#train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
sess = tf.InteractiveSession()
# for _ in range(1000):
#   batch_xs, batch_ys = mnist.train.next_batch(100)
#   sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
# correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
# accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
#
# writer = tf.summary.FileWriter(r"D:\Python\TensorBoard\mnist_softmax", tf.get_default_graph())
# writer.close()

def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
#现在我们可以实现第一层卷积。它由一个卷积接一个最大池化构成。卷积在每5x5的patch中算出32个特征。它的权重张量形状为[5, 5, 1, 32]。前两个维度是patch大小，第三个维度是图片颜色输入通道的数量（灰度图片为1，彩色图片为3），最后一个是输出通道的数量。我们还将为每个输出通道添加一个偏置量。
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])
#为了将层应用于图中，我们首先reshape x形成4d张量，第二和第三维对应于图片的宽度和高度，最后的尺寸对应于颜色通道的数量。
x_image = tf.reshape(x, [-1, 28, 28, 1])
#然后我们将x_image与权重张量进行卷积，添加偏置量，应用于ReLU函数，最后再加入最大池化。该max_pool_2x2方法将图像大小减小到14x14。
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)
#为了构建一个深层次的网络，我们堆叠几层这种类型的模块。第二层将为每个5x5patch提取64特征。
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

#现在图像尺寸已经缩小到7x7，我们添加了一个具有1024个神经元的全连接层，以便对整个图像进行处理。我们从池化层将张量reshape成一些向量，然后乘以权重矩阵，添加偏置量并应用于ReLU。
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

#为了避免过拟合，我们在输出层之前加入dropout 。我们创建一个占位符表示在神经元dropuot时保持不变的概率。这样可以让我们在训练过程中应用dropout，并在测试过程中将其关闭。TensorFlow的tf.nn.dropoutop除了可以屏蔽神经元的输出外，还可以自动处理神经元输出scale，所以用dropout的时候可以不用考虑任何额外scale。
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
#输出层:最后，我们添加一层，就像上面提到的softmax回归层一样。
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

#这个模型到底有多好？为了训练和评估它，我们使用与之前简单SoftMax神经网络模型几乎相同的一套代码。
# 差异在于：
# 我们将用更复杂的ADAM优化器替换梯度最快下降优化器。
# 我们将在feed_dict中加入额外的参数keep_prob，以便控制dropout。
# 我们将在训练过程中每隔100次添加日志记录。
# 随后运行这段代码，但是它会执行20,000次训练迭代，并且可能需要一段时间（可能长达半小时），这取决于您的处理器。
cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
sess.run(tf.global_variables_initializer())
for i in range(2000):
    batch = mnist.train.next_batch(50)
    if i%100 == 0:
        train_accuracy = accuracy.eval(feed_dict={
                x:batch[0], y_: batch[1], keep_prob: 1.0})
        print("step %d, training accuracy %g"%(i, train_accuracy))
    train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

print("test accuracy %g"%accuracy.eval(feed_dict={
    x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))