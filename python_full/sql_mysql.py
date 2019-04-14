# import mysql.connector
# conn = mysql.connector.connect(host='127.0.0.1',port='3306',user='root',password='root')
# sql = conn.cursor()
# sql.execute("show databases;")
# for i in sql.fetchall():
#     print(i[0])
# import sqlite3
# conn = sqlite3.connect('./test.db')
# cursor = conn.cursor()
# # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# print(cursor.execute('select * from user where id = ?',(1,)).fetchall())
# cursor.close()
# conn.commit()
# conn.close()

import mysql.connector
import pprint
conn = mysql.connector.connect(host='127.0.0.1',user='root',password='root',database='studentsys')
try:
    cursor = conn.cursor()
    cursor.execute('select * from t_student where phone = %s',('15010350105',))
    # pprint.pprint(cursor.fetchall())
    for res in cursor.fetchall():
        pprint.pprint(res)
finally:
    cursor.close()
    conn.close()


