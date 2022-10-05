import requests
from bs4 import BeautifulSoup
from plyer import notification
def get_data(url):
    data = requests.get(url)
    return data
raw_data = get_data('https://weather.com/en-IN/weather/today/l/e1bbaf5ba44a74170e3bb9f892416301c36b3b17f37e1a666c6e1213de0f5668')
bs = BeautifulSoup(raw_data.text, 'html.parser')
temperature = bs.find_all("span",  class_ = "CurrentConditions--tempValue--1RYJJ")
conditions = bs.find_all("div", class_ = "CurrentConditions--phraseValue--17s79")
city_name = bs.find_all("h1", class_ = "CurrentConditions--location--2_osB")
for i,j,k in zip(temperature,conditions,city_name):
    temp = str(i.text)
    condi = str(j.text)
    city = str(k.text)
weather_update = "Current temperature is: " + temp + "\nCurrent conditions: " + condi
city.replace(' ',',')
city = city.split(',')
notification.notify(
        title = city[0] + " weather update",
        message = weather_update,
        timeout = 5,
        app_icon = None
    )