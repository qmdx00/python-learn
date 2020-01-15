import tensorflow as tf


a = tf.constant([[0, 2], [1, 0]])
b = tf.constant([[1, -2], [1, 0]])
print(tf.matmul(a, b))
