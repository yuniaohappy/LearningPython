from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('spark_test').getOrCreate()
people = spark.read.json('D:\\spark-2.3.3-bin-hadoop2.7\\examples\\src\\main\\resources\\people.json')\
    .createOrReplaceGlobalTempView('people')
print(type(people))
user = spark.read.parquet('D:\\spark-2.3.3-bin-hadoop2.7\\examples\\src\\main\\resources\\users.parquet').show()
user.select('user').show()
# people.select().show()
# spark.sql('select * from people').show()
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


