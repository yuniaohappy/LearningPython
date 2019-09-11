import tensorflow_datasets as tfds
import tensorflow as tf
tf.data.Dataset

tf.enable_eager_execution()
tfds_list = tfds.list_builders()
# for i in tfds_list:
#     print(i)
tf_train,tf_test = tfds.load(name='mnist',split=['train','test'])
print(tf_train)
