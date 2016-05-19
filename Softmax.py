"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    print(np.exp(x))
    return np.exp(x)/np.sum(np.exp(x),axis = 0)
    pass  # TODO: Compute and return softmax(x)



print(softmax(scores))

a = 1000000000
for i in xrange(1000000):
    a+= 1e-6
print(a - 1000000000)

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()