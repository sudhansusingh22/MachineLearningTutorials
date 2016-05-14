import numpy as np
from sklearn import preprocessing, cross_validation,neighbors
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data')
# print(df)
df.replace('?',-99999,inplace=True)
df.drop(['id'],1,inplace=True)
# can drop NA also instead

X = np.array(df.drop(['class'],1))
y = np.array(df['class'])

X_train,X_test,y_train, y_test = cross_validation.train_test_split(X,y, test_size = 0.2)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test,y_test)

print(accuracy)

example_measures = np.array([4,2,1,1,1,4,3,2,1])
print(example_measures)
example_measures = example_measures.reshape(1,-1)
print(example_measures)
prediction = clf.predict(example_measures)
print(prediction)