import numpy as np
import pandas as pd
import PIL
import tensorflow as tf
import pyparsing
import tensorflow_hub as hub

model_url = "https://tfhub.dev/google/on_device_vision/classifier/landmarks_classifier_asia_V1/1"
labels = "landmarks_classifier_asia_V1_label_map.csv"
img_shape = (321,321)
classifer = tf.keras.Sequential([hub.KerasLayer(model_url,input_shape=img_shape)])


