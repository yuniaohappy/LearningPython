from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.context import SparkContext, SparkConf
from pyspark.sql import HiveContext
from pyspark.sql import Row
import time


conf = SparkConf().setAppName('Spark Test').setMaster('local[*]')
sc = SparkContext(conf=conf)
start = time.time()
t = sc.textFile('D:\spark-2.3.3-bin-hadoop2.7\README.md')
counts = t.flatMap(lambda line:line.split(' '))\
    .map(lambda x:(x,1))\
    .reduceByKey(lambda a,b:a+b)\
    .map(lambda x:(x[1],x[0])).sortByKey(False)\
    .map(lambda x:(x[1],x[0])).take(10)
print(time.time()-start)
# counts.foreach(lambda x:print(x))
for word in counts:print(word)

# sortby实现
# start = time.time()
# t = sc.textFile('D:\spark-2.3.3-bin-hadoop2.7\README.md')
# counts = t.flatMap(lambda line:line.split(' '))\
#     .map(lambda x:(x,1))\
#     .reduceByKey(lambda a,b:a+b)\
#     .sortBy(lambda x:x[1],False).take(10)
# print(time.time()-start)
#
# for word in counts:print(word)

# spark = SparkSession(sc).builder.appName('Spark SQL').config('spark.some.config.option', 'some-value').getOrCreate()
# df = spark.read.json('D:\李鹏工作目录\python\python_learning\json\\ambar3node.json')
# print(df.show())
# print(sc.textFile('D:\spark-2.3.3-bin-hadoop2.7\examples\src\main\\resources\people.txt').count())
# spark = SparkSession(sc).builder.getOrCreate()
# j = spark.read.json('D:\spark-2.3.3-bin-hadoop2.7\examples\src\main\\resources\people.json')
# j.createOrReplaceTempView('people')
# j.describe().show()

spark = SparkSession(sc).builder.getOrCreate()
# emp = spark.read.json('D:\spark-2.3.3-bin-hadoop2.7\examples\src\main\\resources\employees.json')
# print(type(emp.toPandas()))
# users = spark.read.parquet('D:\spark-2.3.3-bin-hadoop2.7\examples\src\main\\resources\\users.parquet')
# users.show()



# p = sc.textFile('D:\spark-2.3.3-bin-hadoop2.7\examples\src\main\\resources\people.txt')
# line = p.map(lambda line:line.strip().split(','))
# people = line.map(lambda p:Row(name = p[0],age = int(p[1])))
# df = spark.createDataFrame(people)
# df.createOrReplaceTempView('people')
# spark.sql('select * from people where age > 20').show()