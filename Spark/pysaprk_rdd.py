from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession

conf = SparkConf().setAppName('pyspark_test').setMaster('local[2]')
sc = SparkContext(conf=conf)
data = [12,3,4,5,6]
d = sc.parallelize(data).reduce(lambda x,y:x+y)
print(d)
# sc.textFile()

spark = SparkSession(sc)
spark.createDataFrame()