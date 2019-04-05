import tensorflow as tf

tf.app.flags.DEFINE_string("ps_hosts", "localhost:2222","ps hosts")
tf.app.flags.DEFINE_string("worker_hosts", "localhost:2223,localhost:2224","worker  hosts")
tf.app.flags.DEFINE_string("job_name", "worker", "'ps' or 'worker")
tf.app.flags.DEFINE_integer("task_index", 0, "ps and worker task index")

FLAGS = tf.app.flags.FLAGS

def main(_):
    ps_hosts = FLAGS.ps_hosts.split(",")
    worker_hosts = FLAGS.worker_hosts.split(",")
    cluster = tf.train.ClusterSpec({"ps": ps_hosts, "worker": worker_hosts})
    server = tf.train.Server(cluster,FLAGS.job_name,FLAGS.task_index)
    server.join()

if __name__ == "__main__":
    tf.app.run()

