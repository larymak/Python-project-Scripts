
## Get Started

Tweepy: 
Tweepy is the python client for the official Twitter API. Install it using following pip command:

```bash
            pip install tweepy
```

TextBlob: textblob is the python library for processing textual data. Install it using following pip command:

```bash
            pip install textblob
```

Install some NLTK corpora using following command:

```bash
            python -m textblob.download_corpora
```
## Authentication: 
In order to fetch tweets through Twitter API, one needs to register an App through their twitter account. Follow these steps for the same:

1. Open developer.twitter.com/apps and click the button: ‘Create New App’
2. Fill the application details. You can leave the callback url field empty.
3. Once the app is created, you will be redirected to the app page.
4. Open the ‘Keys and Access Tokens’ tab.
5. Copy ‘Consumer Key’, ‘Consumer Secret’, ‘Access token’ and ‘Access Token Secret’.