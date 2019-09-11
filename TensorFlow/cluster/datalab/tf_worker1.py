import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tf_cluster import Cluster

train_X = np.linspace(-1,1,100)
train_Y = 2 * train_X + np.random.randn(*train_X.shape) * 0.3


cluster = Cluster('localhost:2001','localhost:2002,localhost:2003','worker',0)
server = cluster.get_cluster()


# 创建网络结构
with tf.device(tf.train.replica_device_setter(worker_device='/job:ps/task:{0}'.format(cluster.task_index),
                                              cluster=cluster.cluster_spec)):
    X = tf.placeholder('float')
    Y = tf.placeholder('float')

    W = tf.Variable(tf.random_normal([1]),name='weight')
    b = tf.Variable(tf.zeros([1]),name='bias')

    global_step = tf.train.get_or_create_global_step()


    z = tf.multiply(X,W) + b
    tf.summary.histogram('z',z)
    cost = tf.reduce_mean(tf.square(Y - z))
    tf.summary.scalar('loss_function',cost)
    learning_rate = 0.01
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost,global_step=global_step)
    saver = tf.train.Saver(max_to_keep=1)
    merged_summary_op = tf.summary.merge_all()
    init = tf.global_variables_initializer()

    # 创建Supervisor 管理session
training_epochs = 2200
display_step = 2

sv = tf.train.Supervisor(is_chief=(cluster.task_index==0),
                         logdir='./log/super_worker1',
                         init_op=init,
                         summary_op=None,
                         saver=saver,
                         global_step=global_step,
                         save_model_secs=5)
with sv.managed_session(server.target) as sess:
    print('sess is OK')
    print(global_step.eval(session=sess),int(training_epochs*len(train_X)/1000))
    for step in range(global_step.eval(session=sess),int(training_epochs*len(train_X)/1000)):

        for x,y in zip(train_X,train_Y):
            _,epoch = sess.run([optimizer,global_step],
                               feed_dict={X:x,Y:y})
            summary_str = sess.run(merged_summary_op,feed_dict={X:x,Y:y})
            sv.summary_computed(sess,summary_str,global_step=epoch)
            if epoch % display_step == 0:
                loss = sess.run(cost,feed_dict={X:train_X,Y:train_Y})
                print('Step',step,"Epoch",epoch+1,'cost=',loss,'W=',sess.run(W),'b=',sess.run(b))
                # if not (loss == 'NA'):
        sv.saver.save(sess, './log/minist_with_summaries_worker1/' + 'sv.cpk', global_step=step)
    print("Training Finished!!!")
    # sv.saver.save(sess,'./log/minist_with_summaries_worker1/'+'sv.cpk',global_step=epoch)
sv.stop()


