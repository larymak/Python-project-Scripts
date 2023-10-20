<!--Please do not remove this part-->
![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

# BillSwift: Inventory Billing Management System

## 🛠️ Description
BillSwift is a comprehensive billing solution that empowers merchants to effortlessly create, generate, and manage bills, track inventory and products, and optimize their billing processes. With BillSwift, you can bid farewell to tedious paperwork and embrace a more efficient way of running your business.
### 🌟 Key Features:
- Intuitive Bill Creation: Easily create professional invoices allowing you to add your branding and personal touch.
- Inventory Management: Keep track of your products and manage stock levels.
- Bill Tracking: Monitor the status of your bills, know which ones are paid and pending, and never miss a payment again.

## ⚙️ Languages or Frameworks Used
 - Flask
 - Firebase (for Authentication)
 - MongoDB (for data storage)

## 🌟 How to run
 - ### Install all the requirements
    Run `pip install -r requirements.txt` to install all the requirements.
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
- ### MongoDB Setup for Project

   - Download monogdb from the [official website](https://www.mongodb.com/try/download/community) and setup in your local system for testing.
   - Once it is setup locally, try creating documents and collections in mongodb to familiarize yourself with it.
   - You can also download the `MongoDB Compass`, which is the GUI version of Mongo Shell.
   - Once all the local testing is done, you can create a free cloud version of MongoDB in [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register) and get the following credentials from the dashboard of atlas:
 ```bash
MONGO_URI=YOUR_MONGO_URI
MONGO_USERNAME=YOUR_MONGO_USERNAME
MONGO_PASSWORD=YOUR_MONGO_PASSWORD
```
- ### Setup Environment for the project
   - Now create a `.env` file in your project dreictory and include the following parameters as it is :-
```bash
export ENVIRONMENT=local/production
export APP_SECRET=YOUR_APP_SECRET
export MONGO_URI=YOUR_MONGO_URI
export MONGO_USERNAME=YOUR_MONGO_USERNAME
export MONGO_PASSWORD=YOUR_MONGO_PASSWORD
export DB_NAME=YOUR_MONGODB_DATABASE_NAME
export FIREBASE_APIKEY=YOUR_API_KEY
export FIREBASE_AUTHDOMAIN=YOUR_AUTH_DOMAIN
export FIREBASE_DATABASEURL=YOUR_DATABASEURL
export FIREBASE_PROJECT_ID=YOUR_PROJECT_ID
export FIREBASE_STORAGE_BUCKET=YOUR_STORAGE_BUCKET
export FIREBASE_MESSAGING_SENDER_ID=YOUR_MESSAGING_SENDER_ID
export FIREBASE_APP_ID=YOUR_APP_ID
export FIREBASE_MEASUREMENT_ID=YOUR_MEASUREMENT_ID
``` 
-  ###  Now Just, Run the project
    - To the run the project, go to the `bash` terminal of VSCode or any other code editor and run `./start_server.sh`.
    - The server would start running on `http://127.0.0.1:{port_number}`.(generally http://127.0.0.1:5000)
    
 - ### Login/Signup as a user
   Since, you are a new user, singup in the application and then login. Then, Start Exploring the project!
  > Note: **You will recieve a email verification mail from firebase upon singup and then only you can proceed**


## 📺 Demo
- Login/Singup Screen.
  
![image](https://github.com/MBSA-INFINITY/Python-project-Scripts/assets/85332648/1a9738b0-106e-4b49-84e4-29713e260fed)
![image](https://github.com/MBSA-INFINITY/Python-project-Scripts/assets/85332648/cccb7c3a-9436-4db3-b535-6a7678c2273d)

- Main screen of the application (Bill generation)
![image](https://github.com/MBSA-INFINITY/Python-project-Scripts/assets/85332648/88acfd54-8f9a-4f2a-a6f2-d4f5464733c1)

- Product Screen/ Adding products
  
![image](https://github.com/MBSA-INFINITY/Python-project-Scripts/assets/85332648/ebcdd3fd-89fb-427b-b458-2adc6fd3a39a)
![image](https://github.com/MBSA-INFINITY/Python-project-Scripts/assets/85332648/d9aaf039-04dd-42b9-b326-c8080cd879cb)

> Note: **This is where you can manage the inventory of a product by editing it.**

- All Bills Page
  
![image](https://github.com/MBSA-INFINITY/Python-project-Scripts/assets/85332648/53a60ec6-aa3d-44d8-960e-cc885ac31b60)

- Bill generation in PDF Format.
  
![image](https://github.com/MBSA-INFINITY/Python-project-Scripts/assets/85332648/7a498083-75d6-40c4-a928-065933841269)







## 🤖 Author
Github - [MBSA-INFINITY](https://github.com/MBSA-INFINITY)
LinkedIn - [MBSAIADITYA](https://www.linkedin.com/in/mbsaiaditya/)
Portfolio - [MBSA](https://mbsaiaditya.in/)
Instagram - [MBSAIADITYA](https://instagram.com/mbsaiaditya)
