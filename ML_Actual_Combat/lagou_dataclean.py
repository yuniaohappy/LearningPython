import numpy as np
import pandas as pd

class data_clean(object):
    def __init__(self):
        pass
    def get_data(self):
        data1 = pd.read_csv('./data/data_analysis.csv',encoding='gbk')
        data2 = pd.read_csv('./data/machine_learning.csv',encoding='gbk')
        data3 = pd.read_csv('./data/data_mining.csv',encoding='gbk')
        data4 = pd.read_csv('./data/deep_learning.csv',encoding='gbk')

        data = pd.concat((pd.concat((pd.concat((data1,data2)),data3)),data4)).reset_index(drop=True)
        # print(data.shape)
        # print(data.head)
        # print(data.info())
        # print(data['work_year'].value_counts())

        return data
    def clean_operation(self):
        data = self.get_data()
        data['address'] = data['address'].fillna("['未知']")
        for i,j in enumerate(data['address']):
            j = j.replace('[','').replace(']','')
            data['address'][i] = j

        for i,j in enumerate(data['salary']):
            j = j.replace('K','').replace('k','').replace('以上','-0')
            j1 = int(j.split('-')[0])
            j2 = int(j.split('-')[1])
            j3 = (j1 + j2)/2
            data['salary'][i] = j3 * 1000

        # print(data['address'][:4])
        # print(data['salary'][:4])
        print(data['industryLables'][:4])
        # print(data['label'][:4])
        # print(data['position_detail'][:4])
        return data

data_clean().clean_operation()

