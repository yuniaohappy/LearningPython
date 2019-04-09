import numpy as np
from sklearn.datasets import fetch_mldata
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from sklearn.datasets.mldata import fetch_mldata

mnist = fetch_mldata('MNIST original',data_home='./data/')
# print(mnist.target)
# print(mnist.data[38000])
X,y = mnist['data'],mnist['target']
im = X[36000].reshape(28,28)
plt.imshow(im,cmap=matplotlib.cm.binary,interpolation='nearest')
# plt.axis('off')
plt.show()
print(y[36000])
# mnist = fetch_mldata('mnist')
# mnist
