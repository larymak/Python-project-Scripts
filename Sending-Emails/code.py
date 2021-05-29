###### Notice ######

# before sending email you have to enable your less secure apps access in your sending mail (xyz@gmail.com)

import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "xyz@gmail.com"                         # your email-id goes here
EMAIL_PASSWORD = "xyz"                                  # your password goes here

msg = EmailMessage()
msg['Subject'] = 'this is subject'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS

msg.set_content('Content area')

msg.add_alternative("""\
<html>
<body>
    <h1>Your HTML CONTENT GOES HERE </h1>                                
</body>
</html>
""", subtype='html')

with open('testing.txt', 'rb') as f:                       # your filename will go here
    file_data = f.read()
    file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
    print("Email Sent Successfully ..")