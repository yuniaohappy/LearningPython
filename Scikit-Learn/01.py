import sklearn.datasets as ds
import sklearn.preprocessing as pre
import matplotlib.pyplot as plt
import numpy as np
import scipy

bs = ds.load_boston()
X,y = bs.data,bs.target
print(y.shape)
print(y.mean())
bin = pre.Binarizer(22.532806324110677)
new_target = bin.fit_transform(bs.target)
print(new_target[0,:5])

# print((bs.target[:5] > bs.target.mean()).astype(int))
# new_target = pre.binarize(bs.target,threshold=y.mean())
# print(type(new_target))
# print(new_target[:5])

# x_1 = X[:,:3]
# matrix = scipy.sparse.eye(1000,)
# print(pre.scale(matrix,with_mean=False))
# print(matrix.todense())

# my_scaler = pre.MinMaxScaler(feature_range=(1,2))
# print(my_scaler.fit(x_1))
# print(my_scaler.transform(x_1).max(axis=0))

# my_scaler = pre.StandardScaler()
# print(my_scaler.fit(X[:,:3]))
# print(my_scaler.transform(X[:,:3]).mean(axis=0))

# X_2 = pre.scale(X[:,:3])
# print(X_2.mean(axis=0))
# print(X_2.std(axis=0))

# plt.hist(X[:,:].mean(axis=0))
# plt.plot(X[:,:].std(axis=0))
# print(X[:20,4:5])
# plt.plot(X[:,4:5])
# plt.show()

# mea = X[:10,:3].mean(axis=0)
# st = X[:,:3].std()
# print(st)
# print(mea)
# print(X[:,:3])

# print(bs.DESCR)
# print(type(bs))
# housing = ds.fetch_california_housing()
# print(housing.DESCR)
# print(type(housing))
# # bs.get('AGE')
# ds.make_regression()
# X,y = bs.data,bs.target
# print(type(y[0]))
# print(ds.get_data_home())

import sklearn.preprocessing


