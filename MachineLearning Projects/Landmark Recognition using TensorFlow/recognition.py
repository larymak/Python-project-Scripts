
import PIL
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim

model_url = 'https://tfhub.dev/google/on_device_vision/classifier/landmarks_classifier_asia_V1/1'
labels = 'landmarks_classifier_asia_V1_label_map.csv'
df = pd.read_csv(labels)
labels = dict(zip(df.id, df.name))

def image_processing(image):
    image = "taj_mahal.jpg"
    img_shape = (321, 321)
    classifier = tf.keras.Sequential(
        [hub.KerasLayer(model_url, input_shape=img_shape + (3,), output_key="predictions:logits")])
    img = PIL.Image.open(image)
    img = img.resize(img_shape)
    img1 = img
    img = np.array(img) / 255.0
    img = img[np.newaxis]
    result = classifier.predict(img)
    fresult = labels[np.argmax(result)],img1
    print("Prediction Location is ",fresult[0])
    geolocator = Nominatim(user_agent="Your_Name")
    location = geolocator.geocode(fresult[0])
    floc = location.address,location.latitude, location.longitude
    print(location.address,location.latitude, location.longitude) 


def run():

    img_file = 'taj.jpg'
    image_processing(img_file)
   
