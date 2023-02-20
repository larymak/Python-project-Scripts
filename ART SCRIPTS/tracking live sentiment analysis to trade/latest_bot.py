import requests
import os
import json
import config
import preprocessor as p
from langdetect import detect
from csv import writer
import praw
import config, pprint
from textblob import TextBlob
import config
from threading import *
import praw
from binance.client import Client
from binance.enums import *
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import re

# I have used another file called config.py to store the credentials

#Connecting to reddit API (To get this credentials go to : https://www.reddit.com/prefs/apps login and create new app to get the credentials) 

reddit = praw.Reddit(
    client_id=config.REDDIT_ID,
    client_secret=config.REDDIT_SECRET,
    password=config.REDDIT_PASS,
    user_agent="USERAGENT",
    username=config.REDDIT_USER,
)
#Connecting to binance api
client = Client(config.BINANCE_kEY, config.BINANCE_SECRET)


#Variables for Bot

lst_reddit = []
lst_twitter=[]
dogePrices=[]
neededSentiments = 300
# in_position = False
TRADE_SYMBOL = 'BTCUSDT'
# TRADE_QUANTITY = 0.000010
#TRADE_SYMBOL = 'DOGEUSDT'
# TRADE_QUANTITY = 40
UPPER_BAND = 70
LOWER_BAND = 30

#function to perform the average to a given list
def Average(lst): 
    if len(lst) == 0:
        return len(lst)
    else:
        return sum(lst[-neededSentiments:]) / neededSentiments


#webscrapping the fear and greed form cnn
def Fearandgreed():
            cnn= "https://money.cnn.com/data/fear-and-greed/"
            req= Request(url=cnn,headers={'user-agent' :' my-app/0.0.1'})
            response =urlopen(req)
            feargreedindex={}
            html= BeautifulSoup(response)
            feargreedindex=html.find(id='needleChart')

            dataRows=feargreedindex.findAll('li')
            indexstring = dataRows[0]
            indexstring=re.findall(r'[0-9]+',str(indexstring))
            return indexstring[0]

#Connect to Reddit Stream for comments
class Reddit(Thread):
    def run(self):
        # getting the live comments from bitcoin subreddit
        for comment in reddit.subreddit("bitcoin").stream.comments():
            
            #converting the live comments into the sentiment using the textblob, the values lie in the range of (-1= negative sentiment  to 1=postive sentiment)

            redditComment = comment.body
            blob = TextBlob(redditComment)
            sent = blob.sentiment
            # if the sentiment is neutral it isn't much useful
            if sent.polarity != 0.0:
                lst_reddit.append(sent.polarity)
                avg = round(Average(lst_reddit), 2)
                print(" ********** Total Sentiment is currently: "+str(round(Average(lst_reddit), 4)) + " and there are " + str(len(lst_reddit)) + " elements in reddit")

                #Getting the candles information of past 1 minutes from binance api 
                candles = client.get_historical_klines(TRADE_SYMBOL, Client.KLINE_INTERVAL_1MINUTE, "1 Minutes ago UTC")

                if len(dogePrices) == 0:
                    dogePrices.append(float(candles[-1][1]))
                elif dogePrices[-1] != float(candles[-1][1]):
                    dogePrices.append(float(candles[-1][1]))
                print(dogePrices)

                print(" ********** Length of Prices list is: " + str(len(dogePrices)))

                # is indicator is used to measure the trend of the market if the rsi reaches the threshold value like UPPERBAND=70 or LOWERBAND=30. 
                rsi = RSIIndicator(pd.Series(dogePrices))
                df = rsi.rsi()

                
                if (df.iloc[-1] < LOWER_BAND and round(Average(lst)) > 0.2 and len(lst) > 15):
                    # if in_position:
                    #     print("***** BUY ***** but we own!")
                    # else:
                    #     print("***** BUY *****")

                    print("time to buy coin")
                elif (df.iloc[-1] > UPPER_BAND and Average(lst) < -0.2 and len(lst) > 15):
                    # if in_position:
                    #     print("we have to sell")
                    # else:
                    #     print("***** SELL ***** but we dont own!")
                    print("time to sell it")

bearer_token = config.BEARER_TOKEN

#Connect to Twitter Stream for comments and open the twitter developera account to get credentials i.e bearer_token

# we only make changes to the set rules and get rules method 
class Twitter(Thread):
    def run(self):
                
        def bearer_oauth(r):
            """
            Method required by bearer token authentication.
            """

            r.headers["Authorization"] = f"Bearer {bearer_token}"
            r.headers["User-Agent"] = "v2FilteredStreamPython"
            return r


        def get_rules():
            response = requests.get(
                "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
            )
            if response.status_code != 200:
                raise Exception(
                    "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
                )
            print(json.dumps(response.json()))
            return response.json()


        def delete_all_rules(rules):
            if rules is None or "data" not in rules:
                return None

            ids = list(map(lambda rule: rule["id"], rules["data"]))
            payload = {"delete": {"ids": ids}}
            response = requests.post(
                "https://api.twitter.com/2/tweets/search/stream/rules",
                auth=bearer_oauth,
                json=payload
            )
            if response.status_code != 200:
                raise Exception(
                    "Cannot delete rules (HTTP {}): {}".format(
                        response.status_code, response.text
                    )
                )
            print(json.dumps(response.json()))

        # in the set rules i am setting the bitcoin as a particular hastag from which the tweets are streamed
        def set_rules(delete):
            # You can adjust the rules if needed
            sample_rules = [
                {"value": "bitcoin", "tag": "bitcoin"},
                # {"value": "cat has:images -grumpy", "tag": "cat pictures"},
            ]
            payload = {"add": sample_rules}
            response = requests.post(
                "https://api.twitter.com/2/tweets/search/stream/rules",
                auth=bearer_oauth,
                json=payload,
            )
            if response.status_code != 201:
                raise Exception(
                    "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
                )
            print(json.dumps(response.json()))


        def get_stream(set):
            response = requests.get(
                "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
            )
            print(response.status_code)
            if response.status_code != 200:
                raise Exception(
                    "Cannot get stream (HTTP {}): {}".format(
                        response.status_code, response.text
                    )
                )
            # here the twitter api default code ends from here we need to make the changes and build the logic
            for response_line in response.iter_lines():
                if response_line:
                    json_response = json.loads(response_line)
                    tweet = json_response['data']['text']
                    tweet = p.clean(tweet)
                    tweet = tweet.replace(':','')
                    blob = TextBlob(tweet)
                    sent = blob.sentiment

                    if sent.polarity != 0.0:
                        lst_twitter.append(sent.polarity)
                        avg = round(Average(lst_twitter), 2)
                        print(" ********** Total Sentiment is currently: "+str(round(Average(lst_twitter), 4)) + " and there are " + str(len(lst_twitter)) + " elements in twitter")

                        if (round(Average(lst_twitter)) > 0.2 and len(lst_twitter) > neededSentiments and Fearandgreed()<40):
                            # if in_position:
                            #     print("***** BUY ***** but we own!")
                            # else:
                            #     print("***** BUY *****")
                            print("time to buy coin")
                        elif (round(Average(lst_twitter)) < -0.2 and len(lst_twitter) > neededSentiments and Fearandgreed()>60):
                            # if in_position:
                            #     print("we have to sell")
                            # else:
                            #     print("***** SELL ***** but we dont own!")
                            print("time to sell it")


        def main():
            
            rules = get_rules()
            delete = delete_all_rules(rules)
            set = set_rules(delete)
            get_stream(set)
            bearer_token = config.BEARER_TOKEN
            # headers = create_headers(bearer_token)
            # rules = get_rules(headers, bearer_token)
            # delete = delete_all_rules(headers, bearer_token, rules)
            # set = set_rules(headers, delete, bearer_token)
            # get_stream(headers, set, bearer_token)

        main()


 
if __name__ == "__main__":
    red=Reddit()
    # twi=Twitter()

    red.start()
    # twi.start()

    