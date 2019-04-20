# from pyhive import hive
# conn = hive.connect(host='127.0.0.1',port='10000',user='hive',database='ods_import').cursor()
# print(conn.fetchall())

from impala.dbapi import connect
conn = connect(host='127.0.0.1',port=10000,database='ods_import',auth_mechanism='NOSASL',user='hive')
cur = conn.cursor()
cur.execute("select * from test")
print(cur.featchall())
