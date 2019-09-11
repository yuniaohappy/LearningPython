import tensorflow as tf

class Cluster():
    def __init__(self,ps_hosts,worker_hosts,job_name,task_index,):
        self.ps_hosts = ps_hosts
        self.worker_hosts = worker_hosts
        self.job_name = job_name
        self.task_index = task_index

    def get_cluster(self):
        ps = self.ps_hosts.split(',')
        worker = self.worker_hosts.split(',')
        self.cluster_spec = tf.train.ClusterSpec({'ps':ps,'worker':worker})
        server = tf.train.Server({'ps':ps,'worker':worker},
                                 job_name=self.job_name,
                                 task_index=self.task_index)
        if self.job_name == 'ps':
            server.join()
        return server