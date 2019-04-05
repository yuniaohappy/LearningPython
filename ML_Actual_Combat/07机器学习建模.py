# -*- encoding=utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

from sklearn import ensemble
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error

# boston = datasets.load_boston()
# X,y = shuffle(boston.data,boston.target,random_state=13)
# X = X .astype(np.float32)
# offset = int(X.shape[0] * 0.9)
# X_train,y_train = X[:offset],y[:offset]
# X_test,y_test = X[offset:],y[offset:]
#
# params = {"n_estimators":500,"max_depth":4,
#           "min_samples_split":2,"learning_rate":0.01,
#           "loss":"ls"}
# clf = ensemble.GradientBoostingRegressor(**params)
# clf.fit(X_train,y_train)
# mse = mean_squared_error(y_test,clf.predict(X_test))
# print("MSE：%.4f" % mse)
#
# test_score = np.zeros((params["n_estimators"],),dtype=np.float64)
# for i,y_pred in enumerate(clf.staged_predict(X_test)):
#     test_score[i] = clf.loss_(y_test,y_pred)
# plt.figure(figsize=(12,6))
# plt.subplot(1,2,1)
# plt.title("Deviance")
# plt.plot(np.arange(params["n_estimators"]) + 1,clf.train_score_,"b-",label="Training Set Deviance")
# plt.plot(np.arange(params["n_estimators"]) + 1,test_score,"r-",label="Test Set Deviance")
# plt.legend(loc="upper right")
# plt.xlabel("Boosting Iterations")
# plt.ylabel("Deviance")
#
# feature_importance = clf.feature_importances_
# feature_importance = 100.0 * (feature_importance / feature_importance.max())
# sorted_idx = np.argsort(feature_importance)
# pos = np.arange(sorted_idx.shape[0]) + 0.5
# plt.subplot(1,2,2)
# plt.barh(pos,feature_importance[sorted_idx],align="center")
# plt.yticks(pos,boston.feature_names[sorted_idx])
# plt.xlabel("Relative Importance")
# plt.title("Variable Importance")
# plt.show()

# import xgboost as xgb
# data = np.random.rand(100000,10)
# label = np.random.randint(2,size=100000)
# dtrain = xgb.DMatrix(data,label=label,missing= -999.0)
#
# data2 = np.random.rand(5000,10)
# label2 = np.random.randint(2,size=5000)
# dtest = xgb.DMatrix(data2,label=label2,missing= -999.0)
# params = {"bst:max_depth":2,"bst:eta":1,"silent":1,"objective":"binary:logistic"}
# params["nthread"] = 4
# params["eval_metric"] = "auc"
# evallist = [(dtrain,"train"),(dtest,"eval")]
# num_round = 50
# # bst = xgb.train(params,dtrain,num_round,evallist)
# bst = xgb.train(params, dtrain, num_round, evallist, early_stopping_rounds=10)
# print(bst)

# ### lightGBM
# import lightgbm as lgb
#
# data = np.random.rand(100000, 10)
# label = np.random.randint(2, size=100000)
# train_data = lgb.Dataset(data, label=label)
#
# data2 = np.random.rand(5000, 10)
# label2 = np.random.randint(2, size=5000)
# test_data = lgb.Dataset(data2, label=label2)
#
# param = {'num_leaves':31, 'num_trees':100, 'objective':'binary', 'metrics': 'binary_error'}
# num_round = 10
# bst = lgb.train(param, train_data, num_round, valid_sets=[test_data])

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/lagou_featured.csv",encoding="gbk")
print(df.shape)
pd.options.display.max_columns = 999
# print(df.head())
# plt.hist(df["salary"])
# plt.show()
X = df.drop(["salary"],axis=1).values
y = df["salary"].values.reshape((-1,1))
print(X.shape,y.shape)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
print(X_train.shape,X_train.shape,y_test.shape,y_test.shape)

# from sklearn.ensemble import GradientBoostingRegressor
# model = GradientBoostingRegressor(n_estimators = 100, max_depth = 5)
# model.fit(X_train, y_train)
# from sklearn.metrics import mean_squared_error
# y_pred = model.predict(X_test)
# print(np.sqrt(mean_squared_error(y_test, y_pred)))
# print(y_pred[:10])

from sklearn.model_selection import KFold
import xgboost as xgb
from sklearn.metrics import mean_squared_error
import time

kf = KFold(n_splits=5, random_state=123, shuffle=True)


def evalerror(preds, dtrain):
    labels = dtrain.get_label()
    return 'mse', mean_squared_error(np.exp(preds), np.exp(labels))


y = np.log(y)
valid_preds = np.zeros((330, 5))

time_start = time.time()

for i, (train_ind, valid_ind) in enumerate(kf.split(X)):
    print('Fold', i + 1, 'out of', 5)
    X_train, y_train = X[train_ind], y[train_ind]
    X_valid, y_valid = X[valid_ind], y[valid_ind]
    xgb_params = {
        'eta': 0.01,
        'max_depth': 6,
        'subsample': 0.9,
        'colsample_bytree': 0.9,
        'objective': 'reg:linear',
        'eval_metric': 'rmse',
        'seed': 99,
        'silent': True
    }

    d_train = xgb.DMatrix(X_train, y_train)
    d_valid = xgb.DMatrix(X_valid, y_valid)

    watchlist = [(d_train, 'train'), (d_valid, 'valid')]
    model = xgb.train(
        xgb_params,
        d_train,
        2000,
        watchlist,
        verbose_eval=100,
        #         feval=evalerror,
        early_stopping_rounds=1000
    )
#     valid_preds[:, i] = np.exp(model.predict(d_valid))

# valid_pred = valid_preds.means(axis=1)
# print('outline score：{}'.format(np.sqrt(mean_squared_error(y_pred, valid_pred)*0.5)))
# print('cv training time {} seconds'.format(time.time() - time_start))
#
# import xgboost as xgb
# xg_train = xgb.DMatrix(X, y)
#
# params = {
#         'eta': 0.01,
#         'max_depth': 6,
#         'subsample': 0.9,
#         'colsample_bytree': 0.9,
#         'objective': 'reg:linear',
#         'eval_metric': 'rmse',
#         'seed': 99,
#         'silent': True
#     }
# cv = xgb.cv(params, xg_train, 1000, nfold=5,
#             early_stopping_rounds=800, verbose_eval=100)

X = df.drop(['salary'], axis=1).values
y = np.log(df['salary'].values.reshape((-1, 1))).ravel()
print(type(X), type(y))

import lightgbm as lgb
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error

def evalerror(preds, dtrain):
    labels = dtrain.get_label()
    return 'mse', mean_squared_error(np.exp(preds), np.exp(labels))

params = {
    'learning_rate': 0.01,
    'boosting_type': 'gbdt',
    'objective': 'regression',
    'metric': 'mse',
    'sub_feature': 0.7,
    'num_leaves': 17,
    'colsample_bytree': 0.7,
    'feature_fraction': 0.7,
    'min_data': 100,
    'min_hessian': 1,
    'verbose': -1,
}

print('begin cv 5-fold training...')
scores = []
start_time = time.time()

kf = KFold(n_splits=5, shuffle=True, random_state=27)
for i, (train_index, valid_index) in enumerate(kf.split(X)):
    print('Fold', i+1, 'out of', 5)
    X_train, y_train = X[train_index], y[train_index]
    X_valid, y_valid = X[valid_index], y[valid_index]
    lgb_train = lgb.Dataset(X_train, y_train)
    lgb_valid = lgb.Dataset(X_valid, y_valid)
    model = lgb.train(params,
                lgb_train,
                num_boost_round=2000,
                valid_sets=lgb_valid,
                verbose_eval=200,
#                feval=evalerror,
               early_stopping_rounds=1000)
#     feat_importance = pd.Series(model.feature_importance(), index=X.columns).sort_values(ascending=False)
#     test_preds[:, i] = model.predict(lgb_valid)
# print('outline score：{}'.format(np.sqrt(mean_squared_error(y_pred, valid_pred)*0.5)))
print('cv training time {} seconds'.format(time.time() - time_start))

