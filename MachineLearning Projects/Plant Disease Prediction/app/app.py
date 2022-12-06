from flask import Flask, render_template, request
from requests import get   #pip install flask
app = Flask(__name__)


import os
import numpy as np
import tensorflow as tf

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
config = ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.2
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

# Keras
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from werkzeug.utils import secure_filename

MODEL_PATH ='model_inception.h5'
# Load your trained model
model = load_model(MODEL_PATH)

def model_predict(img_path, model):
    print(img_path)
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x=x/255
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)
    preds=np.argmax(preds, axis=1)
    if preds==0:
        preds="Healthy"
    elif preds==1:
        preds="Powdery"
    elif preds==2:
        preds="Rust"
    
    return preds


# route
@app.route('/', methods=["GET", "POST"])
def index():
    # a=svd.predict(1, 302, 3)
    return render_template('index.html')

@app.route('/analyze', methods=["GET", "POST"])
async def analyze():
    if request.method == 'POST':
        f = request.files['imagefile']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        preds = model_predict(file_path, model)
        result=preds
        return render_template('res.html', result=result)
    return render_template('res.html', result="Sorry!! we're not able to find any relevent result for your image, please check the image and retry!!")
if __name__ == "__main__":
    app.run(debug=True)