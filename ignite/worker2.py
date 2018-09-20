from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import os 

def main(unused_argv):
  os.environ['TF_CONFIG'] = '{"cluster":{"worker":["localhost:1111", "localhost:1112"],"chief":["localhost:1113"]}, "task":{"type":"worker","index":1}}'
  to_import_contrib_ops = tf.contrib.resampler
  tf.contrib.distribute.run_standard_tensorflow_server().join()


if __name__ == "__main__":
  tf.app.run()
