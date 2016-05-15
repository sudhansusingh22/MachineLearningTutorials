import matplotlib.pyplot as plt
from sklearn  import datasets
from sklearn import svm, preprocessing
import numpy as np
import pandas as pd
from matplotlib import style
import warnings
warnings.filterwarnings("ignore")


style.use("ggplot")

FEATURES = ["DE Ratio",
            'Trailing P/E',
            'Price/Sales',
            'Price/Book',
            'Profit Margin',
            'Operating Margin',
            'Return on Assets',
            'Return on Equity',
            'Revenue Per Share',
            'Market Cap',
            'Enterprise Value',
            'Forward P/E',
            'PEG Ratio',
            'Enterprise Value/Revenue',
            'Enterprise Value/EBITDA',
            'Revenue',
            'Gross Profit',
            'EBITDA',
            'Net Income Avl to Common ',
            'Diluted EPS',
            'Earnings Growth',
            'Revenue Growth',
            'Total Cash',
            'Total Cash Per Share',
            'Total Debt',
            'Current Ratio',
            'Book Value Per Share',
            'Cash Flow',
            'Beta',
            'Held by Insiders',
            'Held by Institutions',
            'Shares Short (as of',
            'Short Ratio',
            'Short % of Float',
            'Shares Short (prior ']

def Build_Data_Set(features = FEATURES):
    data_df = pd.DataFrame.from_csv("key_stats.csv")
#     data_df = data_df[:100]
    X = np.array(data_df[features].values)
    y = (data_df["Status"].replace("underperform",0).replace("outperform",1).values.tolist())
    X = preprocessing.scale(X)
    return X,y

def Analysis():
    
    test_size = 1000
    
    X,y = Build_Data_Set()
    print(len(X))
    clf = svm.SVC(kernel="linear",C = 1.0)
    clf.fit(X[:-test_size],y[:-test_size])
    correct_count = 0
    for x in range(1,test_size+1):
        if clf.predict(X[-x])[0]==y[-x]:
            correct_count+=1
            
    print("Accuracy ", (float(correct_count)/float(test_size))*100.00 )
    
    
    """
    w = clf.coef_[0]
    
    a = -w[0]/w[1]
    xx = np.linspace(min(X[:,0]), max(X[:,0]))
    yy = a*xx-clf.intercept_[0]/w[1]
    h0 = plt.plot(xx,yy,"k-",label = "non weighted")
    print(len(X[:,0]))
    print(len(X[:,1]))

    plt.scatter(X[:,0],X[:,1],c=y)
    print('here')
    plt.ylabel("Trailing PE")
    plt.xlabel("DE Ration")
    plt.legend()
    plt.show()
    """
Analysis()