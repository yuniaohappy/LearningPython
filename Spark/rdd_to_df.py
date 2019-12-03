from pyspark import SparkConf,SparkContext
from pyspark.sql import SparkSession,Row
from pyspark.sql.types import StructField,StructType,StringType,FloatType


conf = SparkConf().setAppName('rdd_to_df').setMaster('local[2]')
sc = SparkContext(conf=conf)
spark = SparkSession(sc)
# 将RDD转换为DataFrame，使用ROW方式自动推断数据类型问题
# iris_row = sc.textFile('D:\BaiduNetdiskDownload\iris.txt').map(lambda line:line.split(','))\
#     .map(lambda row:Row(sepal_length=row[0],
#                         sepal_width=row[1],
#                         petal_length=row[2],
#                         petal_width=row[3],
#                         class_=row[4]))
# iris = spark.createDataFrame(iris_row)
# iris.createOrReplaceTempView('iris')
# # spark.sql('select * from iris').show()
# iris_df = spark.sql('select class_,count(*) as num from iris group by class_')
# irises = iris_df.rdd.map(lambda iris:'分类：'+iris.class_).collect()
# for i in irises:
#     print(i)

# 通过编程方式将RDD转换为DataFrame
# sepal_length,sepal_width,petal_length,petal_width,class
# iris_rdd = sc.textFile('D:\BaiduNetdiskDownload\iris.txt')\
#     .map(lambda line:line.split(','))\
#     .map(lambda r:(float(r[0]),float(r[1]),float(r[2]),float(r[3]),r[4].strip()))
# # 使用列表推导式来指定列类型
# cols = "sepal_length,sepal_width,petal_length,petal_width,class"
# iris_cols = [StructField(col,StringType(),True) for col in cols.split(',')]
# 单个列设置不同类型也是string类型
# iris_clos = [StructField('sepal_length',FloatType(),True),
#               StructField('sepal_width',FloatType(),True),
#               StructField('petal_length',FloatType(),True),
#              StructField('petal_width',FloatType(),True),
#               StructField('class',StringType(),True)]
# iris_schema = StructType(iris_cols)
# iris = spark.createDataFrame(iris_rdd,iris_schema)
# iris.createOrReplaceTempView('iris')
# res = spark.sql('select * from iris')
# res.write.parquet("D:\BaiduNetdiskDownload\iris.parquet")
# res.write.orc('D:\BaiduNetdiskDownload\iris.orc')
# res.show()

# spark.sql('select * from orc. `D:\BaiduNetdiskDownload\iris.orc`').show()

# df = spark.read.json('D:\spark-2.3.3-bin-hadoop2.7\examples\src\main\\resources\people.json')
# df.createOrReplaceTempView('people')
# spark.sql('select * from people').show()
# jsonStrings = ['{"name":"Yin","address":{"city":"Columbus","state":"Ohio"}}']
# otherPeopleRDD = sc.parallelize(jsonStrings)
# spark.read.json(otherPeopleRDD).write.jdbc()


