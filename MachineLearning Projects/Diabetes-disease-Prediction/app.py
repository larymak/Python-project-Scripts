from wsgiref import simple_server
from flask import Flask, request, app,render_template
from flask import Response
from flask_cors import CORS
import pickle
import bz2
import datetime
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
# from pymongo import MongoClient
# from pymongo.server_api import ServerApi


app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

scalarobject=bz2.BZ2File("Model/standardScalar.pkl", "rb")
scaler=pickle.load(scalarobject)
modelforpred = bz2.BZ2File("Model/modelForPrediction.pkl", "rb")
model = pickle.load(modelforpred)
## Route for homepage

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

## Route for patient Registration
@app.route('/add-patients',methods=['GET','POST'])
def reg():
    return render_template('patient-registration.html')


## Route for Single data point prediction
@app.route('/diabetes',methods=['GET','POST'])
def predict_datapoint():
    result=""
    current_datetime = datetime.datetime.now()
    f_datetime = current_datetime.strftime('%d-%m-%Y  %I:%M %p')

    if request.method=='POST':
        name=request.form.get("name")
        Age = int(request.form.get('Age'))
        gender = request.form.get('gender')
        if gender=='Male':
            Pregnancies=0
            pregnancy='No'
        if gender =='Female':
            Pregnancies=int(request.form.get("Pregnancies"))
            pregnancy=request.form.get("pregnancy")

        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        
        #classification
        if Glucose > 200 and Insulin < 10:
            classification = 'Type 1 Diabetes'
        elif Glucose > 126 and Insulin >= 10:
            classification = 'Type 2 Diabetes'
        elif Glucose > 92:
            classification = 'Gestational Diabetes'
        else:
            classification = 'Unclassified Diabetes'

        new_data=scaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        predict=model.predict(new_data)
       
        if predict[0] ==1 :
            result = 'Diabetic'
        else:
            result ='Non-Diabetic'
            
        return render_template('diabetes.html',result=result,name=name,Age=Age,BMI=BMI,Pregnancies=Pregnancies,Glucose=Glucose,BloodPressure=BloodPressure,Insulin=Insulin,DiabetesPedigreeFunction=DiabetesPedigreeFunction,SkinThickness=SkinThickness,gender=gender,Pregnancy=pregnancy,datetime=f_datetime,type=classification)

    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")
    app.debug(True)