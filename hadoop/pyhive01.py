from pyhive import hive
conn = hive.Connection(host='127.0.0.1',port=10000,username='hdfs',database='ods_import')
cur = conn.cursor()
cur.execute("select * from test")
print(cur.fetchall().count())
