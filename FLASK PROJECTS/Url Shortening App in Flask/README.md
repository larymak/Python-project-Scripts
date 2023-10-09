<!--Please do not remove this part-->
![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

# URL Shortening Application in Flask

## 🛠️ Description
This project is about developing a url shortening application in **Flask** and **MongoDB**. User will paste their long URLs in this application and will get a shortened url, which will redirect to the same long url once used in a browser.

## ⚙️ Languages or Frameworks Used
 - Flask, MongoDB
 - HTML, CSS, Bootstrap


## 🌟 How to run
 - ### Install all the requirements
    Run `pip install -r requirements.txt` to install all the requirements.
 - ### MongoDB Setup for Project

   - Download monogdb from the [official website](https://www.mongodb.com/try/download/community) and setup in your local system for testing.
   - Once it is setup locally, try creating documents and collections in mongodb to familiarize yourself with it.
   - You can also download the `MongoDB Compass`, which is the GUI version of Mongo Shell.
   - Once all the local testing is done, you can create a free cloud version of MongoDB in [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register) and get the following credentials from the dashboard of atlas:
 ```bash
export MONGO_URI=YOUR_MONGO_URI
export MONGO_USERNAME=YOUR_MONGO_USERNAME
export MONGO_PASSWORD=YOUR_MONGO_PASSWORD
``` 
     

- ### Setup Environment for the project
   - Now create a `.env` file in your project dreictory and include the following parameters as it is :-
```bash
export ENVIRONMENT=local | production (choose on the basis of local or production environment)
export APP_SECRET=YOUR_APP_SECRET
export APP_URL=YOUR_APP_URL (the short url)
export MONGO_URI=YOUR_MONGO_URI
export MONGO_USERNAME=YOUR_MONGO_USERNAME
export MONGO_PASSWORD=YOUR_MONGO_PASSWORD
export DB_NAME=YOUR_DATABASE_NAME
``` 

- ###  Now Just, Run the project
  - To the run the project, go to the `bash` terminal of VSCode or any other code editor and run `./start_server.sh`.
  - You don't have to care about setting `.env` then yourself then.


## 📺 Demo
- Main screen of the application.
![image](https://github.com/MBSA-INFINITY/Python-project-Scripts/assets/85332648/94825306-1803-4e48-95d1-4f65bd94fcc1)
- Paste you long URL in the input.
![image](https://github.com/MBSA-INFINITY/Python-project-Scripts/assets/85332648/a5dd5bf5-b311-4d72-b84f-ebf197e30009)
- Click on Shorten and copy the `short url` to clipboard
![image](https://github.com/MBSA-INFINITY/Python-project-Scripts/assets/85332648/4eeb3d39-ddfe-48b0-9c2c-23ffe01036cd)



## 🤖 Author

Github - [MBSA-INFINITY](https://github.com/MBSA-INFINITY)
LinkedIn - [MBSAIADITYA](https://www.linkedin.com/in/mbsaiaditya/)
Portfolio - [MBSA](https://mbsaiaditya.in/)




