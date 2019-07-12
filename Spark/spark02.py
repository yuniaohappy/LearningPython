from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.context import SparkContext, SparkConf

conf = SparkConf().setAppName('Spark Test').setMaster('local[*]')
sc = SparkContext(conf)

spark = SparkSession(sc).builder.appName('Spark SQL').config('spark.some.config.option', 'some-value').getOrCreate()
df = spark.read.json('D:\李鹏工作目录\python\python_learning\json\\ambar3node.json')
print(df.show())
