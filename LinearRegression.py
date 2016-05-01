# Ref
#https://pythonprogramming.net/machine-learning-tutorial-python-introduction/

import pandas as pd
import quandl
import math, datetime
from datetime import datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import  matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot'
          )
# df = quandl.get("GOOG/NASDAQ_GOOGL")
df = quandl.get("WIKI/GOOGL")
# print(df.head())
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT'] = (df['Adj. High']-df['Adj. Close'])/df['Adj. Close']*100
df['PCT_Change'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100
df = df[['Adj. Close','HL_PCT','PCT_Change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-999999, inplace=True)
forecast_out = int(math.ceil(0.01*len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)

X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['label'])


X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size = 0.2)
# clf = LinearRegression()
# clf = svm.SVR(kernel = "poly")
# clf.fit(X_train, y_train)
# 
# # save the classifier to pickle
# with open('lr.pickle','wb') as f:
#     pickle.dump(clf,f)
    
pickle_in = open('lr.pickle','rb')
clf = pickle.load(pickle_in)    
accuracy = clf.score(X_test,y_test)

forecast_set = clf.predict(X_lately)
# print (forecast_set, accuracy, forecast_out)

df['forecast'] = np.nan
# last_date = df.iloc[-1].name
# print(type(last_date))
# last_unix = last_date#.timestamp()
# oneday = 86400
# next_unix = last_unix+pd.DateOffset(1)
# for i in forecast_set:
#     next_date = datetime.fromtimestamp(next_unix)
#     next_unix+= oneday
#     df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]                                              
df['Adj. Close'].plot()
df['forecast'].plot()
plt.legend(loc = 4)
plt.xlabel('Data')
plt.ylabel('Price')
plt.show()

# print(accuracy)
# print(len(X),len(y))

