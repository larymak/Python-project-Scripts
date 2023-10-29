<!--Please do not remove this part-->
![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

# PDF Page Color Counter

## 🛠️ Description
This Python project provides the integration that eliminates the need for manual data entry and facilitates the quick and accurate transfer of data from Excel to Firebase. Push thousands of data from excel to firebase in mins.

**Key Feature :**

* Excel Data Parsing: We will create a feature to parse Excel spreadsheets, extracting structured data to be used in the Firebase Realtime Database. This parsing functionality will support various Excel formats, ensuring compatibility with a wide range of data sources.


## ⚙️ Languages or Frameworks Used
- **Python**: The primary programming language used for the project.
- **Flask**: Flask is a micro web framework for Python that is lightweight and easy to use.
- **Pandas**: Pandas is a popular open-source Python library used for data manipulation and analysis.

## 🌟 How to run
 - ### Install all the requirements
   - Run `pip install -r requirements.txt` to install all the requirements.
 - ### Firebase Setup for Project

   - Create a [firebase](https://firebase.google.com/) project, set up a web project and get all the `Project Configurations` from `Project Settings`.

   - Navigate to the **Authentication** section in your firebase project and enable the `Email and Password`
    authentication.

    - The `Project Configurations` will look as follows :-
    ```bash
    "apiKey": YOUR_API_KEY ,
    "authDomain": YOUR_AUTH_DOMAIN,
    "databaseURL": YOUR_DATABASEURL,
    "projectId": YOUR_PROJECT_ID,
    "storageBucket": YOUR_STORAGE_BUCKET,
    "messagingSenderId": YOUR_MESSAGING_SENDER_ID,
    "appId": YOUR_APP_ID,
    "measurementId": YOUR_MEASUREMENT_ID 
    ```
    - ### Setup Environment for the project
    - Now create a `.env` file in your project dreictory and include the following parameters as it is :-
    ```bash
    export FIREBASE_APIKEY=YOUR_API_KEY
    export FIREBASE_AUTHDOMAIN=YOUR_AUTH_DOMAIN
    export FIREBASE_DATABASEURL=YOUR_DATABASEURL
    export FIREBASE_PROJECT_ID=YOUR_PROJECT_ID
    export FIREBASE_STORAGE_BUCKET=YOUR_STORAGE_BUCKET
    export FIREBASE_MESSAGING_SENDER_ID=YOUR_MESSAGING_SENDER_ID
    export FIREBASE_APP_ID=YOUR_APP_ID
    export FIREBASE_MEASUREMENT_ID=YOUR_MEASUREMENT_ID
    ``` 

 - ### Setup a Virtual Enviroment

   - Run this command in your terminal `python -m venv myenv`.
   - Change your directory by `cd myenv/Scripts` if on windows.
   - Activate the virtual enviroment by running this command `source activate`.
   - Move out from virtual env to your **Project Directory** by `cd..` .
   - Install the packages if not present - `uvicorn`, `Flask`, `pandas`, `numpy`, `openpyxl`, `firebase`.

- ###  Now Just, Run the project
   
   -Now Run the following command - `python main.py`.
   -You will see output in your terminal indicating that the Flask app is running, usually on http://127.0.0.1:5000/
   -Open your web browser and visit the URL specified in the output to access your Flask application.


## 📺 Demo
![Screenshot 2023-10-25 133406](https://github.com/Om25091210/Count-Color-Black-Pages-PDF/assets/74484315/a84def7c-7db4-4ab5-bf0b-f8cfe5ded66b)


## 🤖 Author

Github - [OM YADAV](https://github.com/Om25091210)
LinkedIn - [OM YADAV](www.linkedin.com/in/omyadav)




