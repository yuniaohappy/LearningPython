import tensorflow as tf
import mnist_forward
import mnist_backward
import time
import os
from tensorflow.examples.tutorials.mnist import input_data

TEST_INTERVAL_SECS = 5

def test(mnist):
    with tf.Graph().as_default() as g:
        x = tf.placeholder(tf.float32, [None, mnist_forward.INPUT_NODE])
        y_ = tf.placeholder(tf.float32, [None, mnist_forward.OUT_NODE])
        y = mnist_forward.forward(x, None)

        ema = tf.train.ExponentialMovingAverage(mnist_backward.MOVING_AVERAGE_DECAY)
        ema_restore = ema.variables_to_restore()
        saver = tf.train.Saver(ema_restore)

        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


        with tf.Session() as sess:
            ckpt = tf.train.get_checkpoint_state(mnist_backward.MODEL_SAVE_PATH)
            if ckpt and ckpt.model_checkpoint_path:
                saver.restore(sess,ckpt.model_checkpoint_path)
                global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                print('model_checkpoint_path:',ckpt.model_checkpoint_path)
                accuracy_score = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
                for i in range(int(global_step),mnist_backward.STEPS):
                    if i % 1000 == 0:
                        print("After %s training step(s),test accuracy = %g" % (i, accuracy_score))
                        saver.save(sess, os.path.join(mnist_backward.MODEL_SAVE_PATH, mnist_backward.MODEL_NAME),global_step=i)
            else:
                print('No checkpoint file found!!!')
                return
        time.sleep(TEST_INTERVAL_SECS)

def main():
    mnist = input_data.read_data_sets('./data/',one_hot=True)
    test(mnist)

if __name__ == '__main__':
    main()


