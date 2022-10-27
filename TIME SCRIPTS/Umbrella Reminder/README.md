# Umbrella Reminder

## Description
This snippet of code will Scrape weather data using Python to get umbrella reminder on email

## Requirements

`$ pip install bs4`

`$ pip install requests `

`$ pip install smtplib`

`$ pip install schedule `



## Steps To Execution
- First of all you need to Enable Less Secure app access from your sending email account. [(Click Here for reference !!)](https://youtu.be/Ee7PDsbfOUI)
- Fork this repo and navigate to Umbrella-Reminder folder
- Open code.py in any text/code editor
- Write necessary modification in code like your time ,city, mail-id , password ...
- Run this code.py `$ python code.py`

Note: When you execute this program it will throw you a smtplib.SMTPAuthenticationError and also sends you a Critical Security alert to your email because, 
In a nutshell, Google is not allowing you to log in via smtplib because it has flagged this sort of login as “less secure”, so what you have to do is go to 
this link while you’re logged in to your google account, and allow the access:

