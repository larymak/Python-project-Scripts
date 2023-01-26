import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

def label_encoder(x):
    if x == 'M':
        return 1
    elif x == 'E':
        return 2
    elif x == 'E+':
        return 3
    elif x == 'S':
        return 4
    
    
def process_and_predict(data):
    #process the data
    data = (np.array(data)).reshape(1, -1)
    
    #load the model
    model = joblib.load('model')
    
    #model prediction
    prediction = list(model.predict(data))[0]
    
    if prediction == 0:
        text = "Not Eligible"
    elif prediction == 1:
        text = "Eligible"
    
    return text
