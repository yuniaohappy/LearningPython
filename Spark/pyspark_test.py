from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('spark_test').getOrCreate()
spark.read.json('D:\\spark-2.3.3-bin-hadoop2.7\\examples\\src\\main\\resources\\people.json').show()

# from pyspark import SparkConf, SparkContext
# conf = SparkConf().setMaster("local[*]").setAppName("First_App")
# sc = SparkContext(conf=conf)
#
# data = sc.parallelize(range(10))
# ans = data.reduce(lambda x, y: x + y)
# print (ans)
#
# lines = sc.textFile("D:\spark-2.3.3-bin-hadoop2.7\README.md")
# print (lines.count())
# print (lines.first())


