from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('spark_test').getOrCreate()
spark.read.json('D:\\spark-2.3.3-bin-hadoop2.7\\examples\\src\\main\\resources\\people.json').show()