import numpy as np
import pandas as pd
import sklearn
dataset = pd.read_csv('Social_Network_Ads.csv')
x = dataset.iloc[:, [1, 2, 3]]
y = dataset.iloc[:, -1]
print(dataset,"\n")
print(x,"\n")
print(y,"\n")
X=x.values
Y=y.values
print(X,"\n")
print(Y,"\n")

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:,0] = le.fit_transform(X[:,0])

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.5, random_state = 0)

from sklearn.naive_bayes import BernoulliNB
clf = BernoulliNB()
Y_pred = clf.fit(X_train, Y_train).predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(Y_test, Y_pred)
ac = accuracy_score(Y_test, Y_pred)
print(cm,"\n")
print(ac,"\n")
