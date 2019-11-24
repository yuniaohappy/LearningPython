import pandas as pd
import os
# import parser
# from pyspark import SparkContext,SparkConf
# from pyspark.sql import SparkSession

EXCEL_PATH = 'D:\爱狄特工作目录\数据实验室2019年新增功能项目\\334个贫困县\\334个贫困县名单.xlsx'
CITYS_PATH = 'D:\爱狄特工作目录\数据实验室2019年新增功能项目\\334个贫困县\\334个贫困县2018年末数据'

df334 = pd.read_excel(EXCEL_PATH,header=[2])
# conf = SparkConf().setAppName('334_test').setMaster('local[2]')
# sc = SparkContext(conf=conf)
# spark = SparkSession(sc)

pks = os.listdir(CITYS_PATH)
df_citys_collect = pd.DataFrame()

# 截取文件名中的地市名称
def split_pre(s):
    return s.split('.')[0].split('_')[-1]

citys_df = pd.read_excel(os.path.join(CITYS_PATH,pks[0]),header=[2])
city_df = citys_df.iloc[[0],3:].T
city_df2 = citys_df.iloc[[1],3:].T

print(city_df.append(city_df2))
# print(df334.join(city_df))
# print(split_pre(pks[0]))

# 生成地市的贷款总计数据
# def citys_data():
#     for p in pks:
#         citys_df = pd.read_excel(os.path.join(CITYS_PATH,p),header=[2])
#         city_df = citys_df.iloc[[0],2:].T
#         print(df334.join(city_df))
#         # print(type(city_df))
#         # print(split_pre(pks[0]))
#     print(df_citys_collect)

# 汇总334个深度贫困县数据
def collect_citys():
    pass

# if __name__ == '__main__':
#     citys_data()





