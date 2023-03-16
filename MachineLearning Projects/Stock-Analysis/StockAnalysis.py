import yfinance as yf
import pandas as pd
import datetime
from datetime import date
from pandas_datareader import data as pdr
import pandas as pd
import matplotlib.pyplot as plt

stocknum=10
option=1
tickerlist = []
while True:
  try:
    option = int(input("You have 2 options 1: Do you want to analyse top stocks in S&P index 2: Specific Stocks, 1/2 ?"))
    
    if option==1:
        stocknum=int(input("How many stocks you want to analyse? give a number"))
        toptickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
        tickerlist= toptickers.head(stocknum).Symbol.to_list()
        print(tickerlist)
    elif option==2:
        inputstr = input("Enter comma separated ticker symbols of interested stocks ")
        print("Input string: ", inputstr)

        # conver to the list
        tickerlist = inputstr.upper().split (",")
        print("list: ", list)
    else:
        raise ValueError
    break
  except ValueError:
      print("Please input valid integer only...")  
      continue

data = pd.DataFrame(columns=tickerlist)

for ticker in tickerlist:
    y = yf.Ticker(ticker)
    if(y==0):
        print("No data found for ",ticker)
        break
try:    
    today=date.today()
    yesterday=today + datetime.timedelta(days=-1)
    lastmonth=today + datetime.timedelta(days=-30)
    lastyear=today + datetime.timedelta(days=-365)
    df2=yf.download(tickerlist,today,today+datetime.timedelta(days=1), auto_adjust=True)['Close']
    df3=yf.download(tickerlist,yesterday,yesterday+datetime.timedelta(days=1), auto_adjust=True)['Close']
    df4=yf.download(tickerlist,lastmonth,lastmonth+datetime.timedelta(days=1), auto_adjust=True)['Close']
    df5=yf.download(tickerlist,lastyear,lastyear+datetime.timedelta(days=1), auto_adjust=True)['Close']
    data=data.append(df2)
    data=data.append(df3)
    data=data.append(df4)
    data=data.append(df5)
    data.plot()

    print(data.head())
except ValueError:
      print("Error occured while processing. Please try again.") 



  

