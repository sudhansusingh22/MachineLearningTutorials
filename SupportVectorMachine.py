# Ref
# pythonprogramming.net

import matplotlib.pyplot as plt
import numpy
from sklearn import datasets, svm

digits = datasets.load_digits()
print(digits.target)

clf = svm.SVC(gamma = 0.001, C=100)


x,y = digits.data[:-1], digits.target[:-1] 

clf.fit(x,y)
print('Prediction', clf.predict(digits.data[-1]))
plt.imshow(digits.images[-1], cmap = plt.gray(),interpolation="nearest")
plt.show()

