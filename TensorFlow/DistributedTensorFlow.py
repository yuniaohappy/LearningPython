#-*- coding:utf-8 -*-
import argparse
import sys

import tensorflow as tf

FLAGS = None

"""
python DistributedTensorFlow.py --ps_hosts=192.168.0.111:2223 --worker_hosts=192.168.0.112:2223,192.168.0.113:2223 --job_name=ps --task_index=0
"""

def main(_):
    ps_hosts = FLAGS.ps_hosts.split(",")
    worker_hosts = FLAGS.worker_hosts.split(",")

    # 从PS节点和Worker创建集群
    cluster = tf.train.ClusterSpec({"ps": ps_hosts, "worker": worker_hosts})

    # 从本地创建和启动一个服务
    server = tf.train.Server(cluster,
                             job_name=FLAGS.job_name,
                             task_index=FLAGS.task_index)

    if FLAGS.job_name == "ps":
        server.join()
    elif FLAGS.job_name == "worker":
        # Assigns ops to the local worker by default.
        with tf.device(tf.train.replica_device_setter(worker_device="/job:ps/task:%d" % FLAGS.task_index)):
            x = tf.Variable(tf.ones([2, 2]))
            y = tf.Variable(tf.ones([2, 2]))

        with tf.device(tf.train.replica_device_setter(worker_device="/job:worker/task:%d" % FLAGS.task_index)):
            z = tf.matmul(x, y) + x

        with tf.Session("grpc://192.168.0.197:2223") as sess:
            sess.run(tf.global_variables_initializer())
            v = sess.run(z)
            print(v)

        # Build model...
        # with tf.name_scope("input"):
        #     x = tf.placeholder(tf.float32, [None, 784], name='x-input')
        #     y_ = tf.placeholder(tf.int64, [None], name='y-input')
        # loss = ...
        # global_step = tf.contrib.framework.get_or_create_global_step()

        # train_op = tf.train.AdagradOptimizer(0.01).minimize(
        #     loss, global_step=global_step)

        # The StopAtStepHook handles stopping after running given steps.
    # hooks = [tf.train.StopAtStepHook(last_step=1000000)]

    # The MonitoredTrainingSession takes care of session initialization,
    # restoring from a checkpoint, saving to a checkpoint, and closing when done
    # or an error occurs.
    # with tf.train.MonitoredTrainingSession(master=server.target,
    #                                        is_chief=(FLAGS.task_index == 0),
    #                                        checkpoint_dir="/tmp/train_logs",
    #                                        hooks=hooks) as mon_sess:
    #     while not mon_sess.should_stop():
    #         # Run a training step asynchronously.
    #         # See `tf.train.SyncReplicasOptimizer` for additional details on how to
    #         # perform *synchronous* training.
    #         # mon_sess.run handles AbortedError in case of preempted PS.
    #         mon_sess.run(z)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.register("type", "bool", lambda v: v.lower() == "true")
    # Flags for defining the tf.train.ClusterSpec
    parser.add_argument(
        "--ps_hosts",
        type=str,
        default="",
        help="Comma-separated list of hostname:port pairs"
    )
    parser.add_argument(
        "--worker_hosts",
        type=str,
        default="",
        help="Comma-separated list of hostname:port pairs"
    )
    parser.add_argument(
        "--job_name",
        type=str,
        default="",
        help="One of 'ps', 'worker'"
    )
    # Flags for defining the tf.train.Server
    parser.add_argument(
        "--task_index",
        type=int,
        default=0,
        help="Index of task within the job"
    )

    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
