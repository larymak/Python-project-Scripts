#Importing the libraries
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

#Importing the cleaned file containing the text and label
news = pd.read_csv('news.csv')
X = news['text']
y = news['label']




#Splitting the data into train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Creating a pipeline that first creates bag of words(after applying stopwords) & then applies Multinomial Naive Bayes model
pipeline = Pipeline([('tfidf', TfidfVectorizer(stop_words='english')),
                    ('nbmodel', MultinomialNB())])

#Training our data
pipeline.fit(X_train, y_train)

#Predicting the label for the test data
pred = pipeline.predict(X_test)

#Checking the performance of our model
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))

#Serialising the file
with open('model.pickle', 'wb') as handle:
    pickle.dump(pipeline, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    