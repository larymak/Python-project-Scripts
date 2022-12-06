# Sending Email

## Description
This snippet of code will send emails from your account to one or multiple accounts.

## Requirements

`$ pip install emails`

`$ pip install secure-smtplib`

## Steps To Execution
- First of all you need to Enable Less Secure app access from your sending email account. [(Click Here for reference !!)](https://youtu.be/Ee7PDsbfOUI)
- Fork this repo and navigate to Sending-Email folder
- Open code.py in any text/code editor
- Write necessary modification in code like your mail-id , password , reciever's mail id , send file name etc..
- Run this code.py `$ python code.py`
- Check if reciever got the mails or not !!!

## Extra
- Note that you can send emails to multiple accounts by adding [email1,email2.email3,..,emailN] to (TO:) section in code.
- I have aaded HTML using add_alternative, so it will work for sending emails using html formats.
- I have also added add_attachments so that you can send files with email
- Those who don't want any functionality, fill free to comment out that portion of code.
