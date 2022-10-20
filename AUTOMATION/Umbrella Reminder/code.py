import schedule
import smtplib
import requests
from bs4 import BeautifulSoup
  
  
def umbrellaReminder():
    city = "Hyderabad"
      
    # creating url and requests instance
    url = "https://www.google.com/search?q=" + "weather" + city
    html = requests.get(url).content
      
    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temperature = soup.find('div',
                            attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    time_sky = soup.find('div', 
                         attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
      
    # formatting data
    sky = time_sky.split('\n')[1]
  
    if sky == "Rainy" or sky == "Rain And Snow" or sky == "Showers" or sky == "Haze" or sky == "Cloudy":
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
          
        # start TLS for security
        smtp_object.starttls()
          
        # Authentication
        smtp_object.login("YOUR EMAIL", "PASSWORD")
        subject = "GeeksforGeeks Umbrella Reminder"
        body = f"Take an umbrella before leaving the house.\
        Weather condition for today is {sky} and temperature is\
        {temperature} in {city}."
        msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nGeeksforGeeks".encode(
            'utf-8')
          
        # sending the mail
        smtp_object.sendmail("FROM EMAIL",
                             "TO EMAIL", msg)
          
        # terminating the session
        smtp_object.quit()
        print("Email Sent!")
  
  
# Every day at 06:00AM time umbrellaReminder() is called.
schedule.every().day.at("06:00").do(umbrellaReminder)
  
while True:
    schedule.run_pending()
