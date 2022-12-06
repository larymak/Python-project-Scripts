import requests

city = input("\nEnter the city name : ")
url = "https://wttr.in/{}".format(city)
try:
    res = requests.get(url)
    print(res.text)
except:
    print("Error occure Please try again later...")