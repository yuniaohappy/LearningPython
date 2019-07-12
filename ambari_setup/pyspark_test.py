from pyspark.sql import SparkSession
from pyspark import SparkConf,SparkContext
from pyspark.sql import HiveContext
from pyspark.mllib.regression import LinearRegressionModel

spark = SparkSession.builder.appName('spark_test').enableHiveSupport().getOrCreate()
# sc = spark.SparkContext
people = spark.read.json('D:\spark-2.3.3-bin-hadoop2.7\examples\src\main\\resources\people.json')
people.select('age').filter('age > 20').show()


# print(spark.sql("select * from ods_import.9970102000101_asdf"))


# hive = spark.read.jdbc('jdbc:hive2://20.200.56.229:10000/ods_import',table='9970102000101_asdf')

# print(hive.count())

# df = spark.read.json('D:\spark-2.3.3-bin-hadoop2.7\examples\src\main\\resources\people.json')
# print(df.show())
# print(df.describe())
# print(df.count())
# df.printSchema



