import numpy as np 
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import streamlit as st
data = pd.read_csv('books.csv',error_bad_lines = False)

rating = data[data["ratings_count"] > 1000000] #1cr
df = rating.sort_values(by='average_rating', ascending=False)

author = data.groupby(by="authors")
author = author["title"].count().reset_index().sort_values(by="title", ascending=False).set_index("authors")
author = author.head(10)

rated = data.sort_values(by='ratings_count', ascending=False).head(10)
rated = rated.set_index("title")
# rated

df2 = data.copy()
df2.loc[ (df2['average_rating'] >= 0) & (df2['average_rating'] <= 1), 'rating_between'] = "between 0 and 1"
df2.loc[ (df2['average_rating'] > 1) & (df2['average_rating'] <= 2), 'rating_between'] = "between 1 and 2"
df2.loc[ (df2['average_rating'] > 2) & (df2['average_rating'] <= 3), 'rating_between'] = "between 2 and 3"
df2.loc[ (df2['average_rating'] > 3) & (df2['average_rating'] <= 4), 'rating_between'] = "between 3 and 4"
df2.loc[ (df2['average_rating'] > 4) & (df2['average_rating'] <= 5), 'rating_between'] = "between 4 and 5"

rating_df = pd.get_dummies(df2['rating_between'])
language_df = pd.get_dummies(df2['language_code'])
features = pd.concat([rating_df, language_df, df2['average_rating'],  df2['ratings_count']], axis=1)

from sklearn.preprocessing import MinMaxScaler
min_max_scaler = MinMaxScaler()
features = min_max_scaler.fit_transform(features)
model = neighbors.NearestNeighbors(n_neighbors=6, algorithm='ball_tree')
model.fit(features)
dist, idlist = model.kneighbors(features)

def book_recommend(bookname):
    books=[]
    book_id = df2[df2["title"] == bookname].index
    #print(book_id)
    book_id = book_id[0]
    for newid in idlist[book_id]:
        books.append(df2.loc[newid].title)
    return books
# BookNames = book_recommend('Harry Potter and the Half-Blood Prince (Harry Potter  #6)')
# BookNames


def book():
    bookname = st.text_input("Enter book")
    bookr = book_recommend(bookname)
    st.table(bookr)
book()