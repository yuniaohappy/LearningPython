import sklearn.datasets as ds
import numpy as np

bs = ds.load_boston()
# print(bs.DESCR)
# print(type(bs))
# housing = ds.fetch_california_housing()
# print(housing.DESCR)
# print(type(housing))
# # bs.get('AGE')
ds.make_regression()
X,y = bs.data,bs.target
# print(type(y[0]))
# print(ds.get_data_home())

