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
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 0)
from sklearn.preprocessing import MinMaxScaler, StandardScaler
sc = MinMaxScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'euclidean')
classifier.fit(X_train,Y_train)
Y_pred = classifier.predict(X_test)
Y_pred
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(Y_test, Y_pred)
ac = accuracy_score(Y_test, Y_pred)
print(cm,"\n")
print(ac,"\n")







