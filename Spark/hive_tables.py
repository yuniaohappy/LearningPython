from pyspark.sql import SparkSession,HiveContext
import pyspark

# from os.path import abspath

# spark = SparkSession\
#     .builder\
#     .enableHiveSupport()\
#     .appName('hive_tables')\
#     .config('spark-warehouse')\
#     .master('local[2]')\
#     .getOrCreate()
spark = SparkSession.builder.appName('spark_jdbc').master('local[2]').getOrCreate()
# hive = HiveContext(spark)
# hive.setConf()
# spark.sql('create table if not exists  src (key INT ,value STRING) using hive')
# spark.sql("load data local inpath 'kv1.txt' into table src")
# spark.sql('select * from src').show()

# jdbc = spark.read.jdbc('jdbc:postgresql://localhost:5432/spark?currentSchema=spark',
#           'iris',
#           properties={'user':'postgres','password':'postgresql','driver':'org.postgresql.Driver'})
#
# jdbc.show()

iris = spark.read.orc('E:\BaiduNetdiskDownload\iris.orc')
iris.show()
# iris.write\
#     .jdbc('jdbc:postgresql://localhost:5432/spark?currentSchema=spark',
#           'iris',
#           mode='overwrite',
#           properties={'user':'postgres','password':'postgresql','driver':'org.postgresql.Driver'})

iris.write.jdbc('jdbc:mysql://localhost:3306/spark',
                'iris',
                'overwrite',
                properties={'user':'root',
                            'password':'root',
                            'driver':'com.mysql.jdbc.Driver'})
