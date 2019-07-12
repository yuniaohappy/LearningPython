from sklearn.feature_extraction import DictVectorizer
X = [{'city':'北京','temperature':100},
     {'city':'上海','temperature':50},
     {'city':'深圳','temperature':30}]
dv = DictVectorizer(sparse=False)
data = dv.fit_transform(X)
print(data)
from sklearn import datasets
iris = datasets.load_iris()
