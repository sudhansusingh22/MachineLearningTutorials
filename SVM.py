import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from matplotlib import style
style.use("ggplot")

x = [1,5,1.5,6,3,7]
y = [2,8,1.8,8,4,13]

plt.scatter(x,y)
# plt.show()

X = np.array([[1,2],
              [5,8],
              [1.5,1.8],
              [6,8],
              [3,4],
              [7,13]
              ])

y = [0,1,0,1,0,1]

clf = svm.SVC(kernel='linear',C=1.0)
clf.fit(X,y)
w = clf.coef_[0]
print(w)

a = -w[0]/w[1]
xx = np.linspace(0,14)
yy = a*xx-clf.intercept_[0]/w[1]
h = plt.plot(xx,yy,'r-', label = 'SVM Divider')
plt.scatter(X[:,0],X[:,1], c = y)
plt.legend()
plt.show()
p = clf.predict([0.4,0.9])
p1 = clf.predict([12,13])
print(p)
print(p1)