
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

label2category = {1: 'positive' , 0: 'neutral' , -1: 'negative'}
category2label = {cat:label for label , cat in label2category.items()}

def predict(corpus , categories , text_array): 

    cv = CountVectorizer(max_features = 1000 , ngram_range = (1,2) , max_df = 0.9)
    mnb = MultinomialNB()
    mnb.fit(cv.fit_transform(corpus).toarray() , categories)
    
    preds = [label2category[label] for label in mnb.predict(cv.transform(text_array).toarray())]
    
    analysis = {'positive':0 , 'neutral':0 , 'negative':0}
    for label in preds:
        analysis[label] += 1
   
    return analysis['positive'] , analysis['neutral'] , analysis['negative']



