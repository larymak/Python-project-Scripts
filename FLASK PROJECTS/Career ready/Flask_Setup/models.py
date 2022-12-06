
import pandas as pd
import numpy as np
import pickle
# import seaborn as sns
career = pd.read_csv('dataset9000.data', header=None)

# for skills
X = np.array(career.iloc[:,0:17])
print(X)

#for roles
Y = np.array(career.iloc[:,17])
print(Y)

col = career.shape
print(col)
# labelling the columns of the dataframe
career.columns = ["Database Fundamentals","Computer Architeture","Distributed Computing Systems","Cyber Security","Networking","Development","Programming Skills","Project Management",
"Computer Forensics Fundamentals","Technical Communication"," AI ML", "Software Engineering", "Business Analysis","Communication Skills", "Data Science", "Troubleshooting skills", "Graphic Designing","Roles"]

career.head()

# sns.heatmap(career.isnull(),cbar=False)

career.dropna(how='all',inplace=True)

career.head()


from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.3, random_state=524)
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
scores = {}
knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, Y_train)
print("X_Train",X_train)
print("Y_Train", Y_train)

Y_pred = knn.predict(X_test)
print("Y_pred", Y_pred)
scores[5] = metrics.accuracy_score(Y_test,Y_pred)
print("Accuracy:",scores[5]*100)

pickle.dump(knn, open('careerl.pkl','wb'))
print('test file created!')