# Introduction
This is a  machine learning project that determines fake news through the url of the news.

# Project Structre
This project has four major parts :

* fake_news_detection.py - This contains code fot our Machine Learning model to classify the model
* app.py - This contains Flask APIs that receives news url through GUI or API calls, extracts the article from the url, feeds it to the model and returns the prediction.
* templates - This folder contains the HTML template to allow user to enter url and displays whether the news is fake or real.
* static - This folder contains the CSS file.

# Running the project on local machine

Ensure that you are in the project home directory.

Run app.py using below command to start Flask API
python app.py
By default, flask will run on port 5000.

Navigate to URL http://127.0.0.1:5000
