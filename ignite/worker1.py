import tensorflow as tf
from tensorflow.contrib.kafka import KafkaDataset

cluster = tf.train.ClusterSpec({"worker": ["localhost:1111", "localhost:1112"], "chief": ["localhost:1113"]})
server = tf.train.Server(cluster, job_name="worker", task_index=0)
server.join()
