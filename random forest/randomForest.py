#!/usr/bin/python

    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.ensemble  import RandomForestClassifier

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




clf =  RandomForestClassifier(n_estimators=100)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
accuracy = clf.score(features_test,labels_test)
print(accuracy)

