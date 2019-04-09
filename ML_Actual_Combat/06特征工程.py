#-*- encoding:utf-8 -*-
# #过滤之方差筛选
# from sklearn.feature_selection import VarianceThreshold
# X = [[0,0,1],[0,1,0],[1,0,0],[0,1,0],[0,1,0],[0,1,0]]
# sel = VarianceThreshold(threshold=(0.8 * (1 - 0.8)))
# print(sel.fit_transform(X))

# #过滤之卡方检验
# from sklearn.datasets import load_iris
# from sklearn.feature_selection import SelectKBest
# from sklearn.feature_selection import chi2
# iris = load_iris()
# X,y = iris.data,iris.target
# print(X.shape)
# X_new = SelectKBest(chi2,k=2).fit_transform(X,y)
# print(X_new.shape)

# #包装法
# #选定一些算法，根据算法在数据上的表现来选择特征集合，一般选用的算法包括随机森林，支持向量机和K近邻等；
# import matplotlib.pyplot as plt
# from sklearn.svm import SVC
# from sklearn.model_selection import StratifiedKFold
# from sklearn.feature_selection import RFECV
# from sklearn.datasets import make_classification
# X,y = make_classification(n_samples=1000,n_features=25,n_informative=3,n_redundant=2,
#                           n_repeated=0,n_classes=8,n_clusters_per_class=1,random_state=0)
# svc = SVC(kernel="linear")
# rfecv = RFECV(estimator=svc,step=1,cv=StratifiedKFold(2),scoring="accuracy")
# rfecv.fit(X,y)
# print("Optimal number of features : %d" % rfecv.n_features_)
# plt.figure()
# plt.xlabel("Number of features selected")
# plt.ylabel("Cross validation score (nb of correct classifications)")
# plt.plot(range(1,len(rfecv.grid_scores_) + 1),rfecv.grid_scores_)
# plt.show()

# # 嵌入法之际遇惩罚想的特征选择
# from sklearn.svm import LinearSVC
# from sklearn.datasets import load_iris
# from sklearn.feature_selection import SelectFromModel
# iris = load_iris()
# print(iris.target)
# X,y = iris.data,iris.target
# print("原始数据特征维度：",X.shape)
# lsvc = LinearSVC(C=0.01,penalty="l1",dual=False).fit(X,y)
# model = SelectFromModel(lsvc,prefit=True)
# X_new = model.transform(X)
# print("l1惩罚处理之后的数据维度：",X_new.shape)

# # 嵌入法之基于树模型的特征选择法
# from sklearn.ensemble import ExtraTreesClassifier
# from sklearn.datasets import load_iris
# from sklearn.feature_selection import SelectFromModel
# iris = load_iris()
# print(iris.target)
# X,y = iris.data,iris.target
# print("原始数据特征维度：",X.shape)
# clf = ExtraTreesClassifier()
# clf = clf.fit(X,y)
# clf.feature_importances_
# model = SelectFromModel(clf,prefit=True)
# X_new = model.transform(X)
# print("l1惩罚处理之后的数据维度：",X_new.shape)

# # one-hot的两种方法
# #sklearn onehotencoder
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.datasets import load_iris
# iris = load_iris()
# print(iris.target)
# one_hot = OneHotEncoder().fit_transform(iris.target.reshape((-1,1))).toarray()
# print(one_hot)

# # pandas dummies 方法
# import pandas as pd
# from sklearn.datasets import load_iris
# iris = load_iris()
# print(pd.get_dummies(iris.target))

# #招聘数据的特征工程探索
# import warnings
# warnings.filterwarnings("ignore")
# import numpy as np
# import pandas as pd
# lagou_df = pd.read_csv("data/lagou_data5.csv",encoding="gbk")
# # print(lagou_df.head())
# one_hot_city = pd.get_dummies(lagou_df["city"])
# print(one_hot_city.head())

# sklearn onehot 方法
# 先要硬编码labelcoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import pandas as pd
lagou_df = pd.read_csv("data/lagou_data5.csv",encoding="gbk")
lbl = LabelEncoder()
lbl.fit(list(lagou_df["city"].values))
lagou_df["city"] = lbl.transform(list(lagou_df["city"].values))
# print(lagou_df["city"].head())

df_city = OneHotEncoder().fit_transform(lagou_df["city"].values.reshape((-1,1))).toarray()
# print(df_city[:5])

cat_features = ["city","industry","education","position_name","size","stage","work_year"]
for col in cat_features:
    temp = pd.get_dummies(lagou_df[col])
    lagou_df = pd.concat([lagou_df,temp],axis=1)
    lagou_df = lagou_df.drop([col],axis=1)

print(lagou_df.shape)
pd.options.display.max_columns = 999
lagou_df = lagou_df.drop(["advantage","label"],axis=1)
# print(lagou_df.head())

import pandas as pd
import warnings
warnings.filterwarnings("ignore")
lagou_df2 = pd.read_csv("data/lagou_data5.csv",encoding="gbk")
lagou_df2 = lagou_df2[["position_detail","salary"]]

for i,j in enumerate(lagou_df2["position_detail"]):
    if "python" in j:
        lagou_df2["position_detail"][i] = j.replace("python","Python")

lagou_df2["Python"] = pd.Series()
for i,j in enumerate(lagou_df2["position_detail"]):
    if "Python" in j:
        lagou_df2["Python"][i] = 1
    else:
        lagou_df2["Python"][i] = 0
# print(lagou_df2["Python"][:20])

lagou_df2["R"] = pd.Series()
for i,j in enumerate(lagou_df2["position_detail"]):
    if "R" in j:
        lagou_df2["R"][i] = 1
    else:
        lagou_df2["R"][i] = 0
print(lagou_df2["R"].value_counts())

for i,j in enumerate(lagou_df2["position_detail"]):
    if "sql" in j:
        lagou_df2["position_detail"][i] = j.replace("sql","SQL")
lagou_df2["SQL"] = pd.Series()
for i,j in enumerate(lagou_df2["position_detail"]):
    if "SQL" in j:
        lagou_df2["SQL"][i] = 1
    else:
        lagou_df2["SQL"][i] = 0
print(lagou_df2["SQL"].value_counts())

lagou_df2["Excel"] = pd.Series()
for i,j in enumerate(lagou_df2["position_detail"]):
    if "Excel" in j:
        lagou_df2["Excel"][i] = 1
    else:
        lagou_df2["Excel"][i] = 0
print("Excel: ",lagou_df2["Excel"].value_counts())

for i,j in enumerate(lagou_df2["position_detail"]):
    if "linux" in j:
        lagou_df2["position_detail"][i] = j.replace("linux","Linux")
lagou_df2["Linux"] = pd.Series()
for i,j in enumerate(lagou_df2["position_detail"]):
    if "Linux" in j:
        lagou_df2["Linux"][i] = 1
    else:
        lagou_df2["Linux"][i] = 0
print(lagou_df2["Linux"].value_counts())

lagou_df2["C++"] = pd.Series()
for i,j in enumerate(lagou_df2["position_detail"]):
    if "C++" in j:
        lagou_df2["C++"][i] = 1
    else:
        lagou_df2["C++"][i] = 0
print(lagou_df2["C++"].value_counts())

for i,j in enumerate(lagou_df2["position_detail"]):
    if "spark" in j:
        lagou_df2["position_detail"][i] = j.replace("spark","Spark")
lagou_df2['Spark'] = pd.Series()
for i, j in enumerate(lagou_df2['position_detail']):
    if 'Spark' in j:
        lagou_df2['Spark'][i] = 1
    else:
        lagou_df2['Spark'][i] = 0
print(lagou_df2['Spark'].value_counts())

for i, j in enumerate(lagou_df2['position_detail']):
    if 'tensorflow' in j:
        lagou_df2['position_detail'][i] = j.replace('tensorflow', 'Tensorflow')
    if 'TensorFlow' in j:
        lagou_df2['position_detail'][i] = j.replace('TensorFlow', 'Tensorflow')
lagou_df2['Tensorflow'] = pd.Series()
for i, j in enumerate(lagou_df2['position_detail']):
    if 'Tensorflow' in j:
        lagou_df2['Tensorflow'][i] = 1
    else:
        lagou_df2['Tensorflow'][i] = 0
print(lagou_df2['Tensorflow'].value_counts())

lagou_df = lagou_df.drop(["position_detail","salary"],axis=1)
print(lagou_df.head())

lagou = pd.concat((lagou_df2,lagou_df),axis=1).reset_index(drop=True)
print(lagou.head())
lagou.to_csv("data/lagou_featured.csv",encoding="gbk")




