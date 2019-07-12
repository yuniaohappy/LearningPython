from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.utils import shuffle
import sklearn.feature_extraction
import sklearn.feature_selection
iris = load_iris()

print(iris.keys())
# print(iris.DESCR)
# print(iris['data'].shape)
# print(iris['target'].shape)
# print(iris['target_names'])
# print(iris['feature_names'])
# print(iris['target'][0])

X,y,X_test,y_test = iris['data'][:120],iris['target'][:120],iris['data'][120:],iris['target'][120:]
# print(X.shape)
# print(X_test.shape)
# lr = LinearRegression()
# print(lr.fit(X,y))
# print(lr.predict(X_test))


svc = SVC()
print(svc.fit(X,y))
print('==================')
print(svc.predict(X_test))
print('%%%%%%%%%%%%%%%%%%%')
print(y_test)
print(svc.score(X_test,y_test))


