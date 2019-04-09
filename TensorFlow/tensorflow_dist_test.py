import tensorflow as tf

ps_hosts = ["192.168.0.111:2222","192.168.0.112:2222"]
worker_hosts = ["192.168.0.111:2223","192.168.0.112:2223", "192.168.0.113:2223"]
cluster = tf.train.ClusterSpec({"ps":ps_hosts, "worker":worker_hosts})

x = tf.Variable()
y = tf.Variable()