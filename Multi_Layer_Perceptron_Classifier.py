import pandas as pd
dataset = pd.read_csv('Social_Network_Ads.csv')
x = dataset.iloc[:, [1, 2, 3]]
y = dataset.iloc[:, -1]
# print(dataset,"\n")
# print(x,"\n")
# print(y,"\n")
X=x.values
Y=y.values
# print(X,"\n")
# print(Y,"\n")

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:,0] = le.fit_transform(X[:,0])

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 1)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='sgd', alpha=1e-5, hidden_layer_sizes=(15, ))
Y_pred = clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)
print(Y_pred,"\n")

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(Y_test, Y_pred)
ac = accuracy_score(Y_test, Y_pred)
print(cm,"\n")
print(ac,"\n")
