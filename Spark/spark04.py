from pyspark.sql import SparkSession
from pyspark import SparkContext,SparkConf
from pyspark.sql import Row
from pyspark.sql.types import StructField,StructType,StringType,IntegerType

# spark = SparkSession.builder.appName('test_pyspark').getOrCreate()
# df = spark.read.json('D:\spark-2.3.3-bin-hadoop2.7\examples\src\main\\resources\people.json')
# people.select('name').show()
# df.show()
# people.printSchema()
# people.select(people['name'],people['age'] + 1).show()
# people.filter(people.age > 21).show()
# df.filter(people.age > 21).show()
# df.groupBy('age').count().show()
# df.createOrReplaceTempView('people')
# spark.sql('select * from people where age > 21').show()
# df.createGlobalTempView('people')
# spark.sql('select * from global_temp.people').show()
conf = SparkConf().setAppName('test_people').setMaster('local[2]')
sc = SparkContext(conf=conf)
spark = SparkSession(sc)
spark.read.text
# 使用反射推断模式
lines = sc.textFile('D:\spark-2.3.3-bin-hadoop2.7\examples\src\main\\resources\people.txt')
# people_row = lines.map(lambda line:line.split(',')).map(lambda row:Row(name=row[0],age=int(row[1])))
# people_schma = spark.createDataFrame(people_row)
# people_df = people_schma.createOrReplaceTempView('people')
# spark.sql('select * from people').show()

# 以编程方式指定模式
people = lines.map(lambda line:line.split(',')).map(lambda x:(x[0].strip(),int(x[1].strip())))
schmastring = 'name age'
# fields = [StructField(col,StringType(),True) for col in schmastring.split()]
fields = [StructField('name',StringType(),True),StructField('age',IntegerType(),True)]
schma = StructType(fields)
schmapeople = spark.createDataFrame(people,schma)
schmapeople.createOrReplaceTempView('people')
spark.sql('select * from people').show()

