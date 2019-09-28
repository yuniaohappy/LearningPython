"""
打印九九乘法表
"""

# for x in range(1,10):
#     for y in range(1,x+1):
#         print(y ,"x",x,'=',x*y,'\t',end='')
#     print()

import psycopg2

conn = psycopg2.connect(database='datalab',user='postgres',password='postgres',port='5432')
cur = conn.cursor()
# cur.execute("CREATE TABLE student(id integer,name varchar,sex varchar);")
# cur.execute("INSERT INTO student(id,name,sex)VALUES(%s,%s,%s)",(1,'Aspirin','M'))
# cur.execute("INSERT INTO student(id,name,sex)VALUES(%s,%s,%s)",(2,'Taxol','F'))
# cur.execute("INSERT INTO student(id,name,sex)VALUES(%s,%s,%s)",(3,'Dixheral','M'))
cur.execute('select * from student')
res = cur.fetchall()
print(res)

