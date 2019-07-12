from pyhive import hive


conn = hive.Connection(host='20.200.41.69',port=10000,username='hive',database='ods_cdi').cursor()
conn.execute('select * from cditloan_ta_loan_infodetail')
res = conn.fetchone()
print(res)
# for tab in res:
#     print(tab)


import pyhdfs
# fs = pyhdfs.HdfsClient('20.5.194.65:50070',user_name='hdfs')
# fst = fs.list_status('/apps/hive/warehouse/ods_import.db/99701160000_apdb_tb_b_asm_astpkg/')
# fst = fs.listdir('/')
# FileStatus(accessTime=0,
# blockSize=0,
# childrenNum=6,
# fileId=16392,
# group='hadoop',
# length=0,
# modificationTime=1553755334860,
# owner='yarn',
# pathSuffix='app-logs',
# permission='777',
# replication=0,
# storagePolicy=0,
# type='DIRECTORY')

# for f in fst:
#
#     # print(f.pathSuffix,f.owner,f.permission,f.replication,f.blockSize,f.type)
#     print(f)


