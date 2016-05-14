import numpy as np
from sklearn import preprocessing, cross_validation,neighbors
import pandas as pd
from math import sqrt
from collections import Counter
import random


def k_nearest_neighbors(data,predict,k=3):
    if len(data)>=k:
        print('Wrong value of k')
    distance = []
    for group in data:
        for features in data[group]:
            ed = np.linalg.norm(np.array(features)-np.array(predict))
            distance.append([ed,group])
    votes = [i[1] for i in sorted(distance)[:k]]
#     print(Counter(votes).most_common(1))
    votes_results = Counter(votes).most_common(1)[0][0]
    confidence = float(Counter(votes).most_common(1)[0][1])/float(k)
    return votes_results,confidence


df = pd.read_csv('breast-cancer-wisconsin.data')
# print(df)
df.replace('?',-99999,inplace=True)
df.drop(['id'],1,inplace=True)
full_data = df.astype(float).values.tolist()
random.shuffle(full_data)

test_size = 0.2

train_set = {2:[],4:[]}

test_set = {2:[],4:[]}
train_data = full_data[:-int(test_size*len(full_data))]
test_data = full_data[-int(test_size*len(full_data)):]

for i in train_data:
    train_set[i[-1]].append(i[:-1])        #class col
for i in test_data:
    test_set[i[-1]].append(i[:-1])        #class col
    
    
correct = 0.0
total = 0.0

for group in test_set:
    for data in test_set[group]:
        vote,confidence = k_nearest_neighbors(train_set,data, k=5)
        if (group == vote):
            correct = correct+1
        else:
            print(confidence)
        total+=1
print(total)
print(correct)
print('Accuracy: ', correct/total)
        
# can drop NA also instead

X = np.array(df.drop(['class'],1))
y = np.array(df['class'])

X_train,X_test,y_train, y_test = cross_validation.train_test_split(X,y, test_size = 0.2)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test,y_test)

# print(accuracy)

example_measures = np.array([4,2,1,1,1,4,3,2,1])
# print(example_measures)
example_measures = example_measures.reshape(1,-1)
# print(example_measures)
prediction = clf.predict(example_measures)
# print(prediction)

plot1 = [1,2]
plot2 = [3,6]

ed = sqrt((plot1[0]-plot2[0])**2 + (plot1[1]-plot2[1])**2)
# print(ed)

dataset = {'k':[[1,2],[2,3],[3,2]],'r':[[5,6],[6,6],[7,8]]}

new_feature = [5,8]


results = k_nearest_neighbors(dataset, new_feature, k=3)
# print(results)