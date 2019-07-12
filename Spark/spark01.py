# from pyspark.sql import SparkSession
# spark = SparkSession().builder.appName("spark_test").config('spark.sql.warehouse.dir','./spark-warehouse').enableHiveSupport().getOrCreate()
# spark.sql('select * from ods_import.9970102000101_asdf').show()
# spark.read.orc('hdfs://http://20.200.56.229:8020/apps/hive/warehouse/ods_import.db/9970102000101_asdf').show()


from pyspark.sql import HiveContext
from pyspark import SparkConf,SparkContext

conf = SparkConf().setAppName("spark_test").setMaster('local[*]')
sc = SparkContext(conf=conf)
hive = HiveContext(sc)
hive.sql('use ods_import')
hive.sql('select * from ods_import.9970102000101_asdf').show()