import mysql.connector
conn = mysql.connector.connect(host='127.0.0.1',port='3306',user='root',password='root')
sql = conn.cursor()
sql.execute("show databases;")
for i in sql.fetchall():
    print(i[0])

