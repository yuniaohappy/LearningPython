from pyspark import SparkConf,SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

conf = SparkConf().setAppName('spark_test').setMaster('local[2]')
sc = SparkContext(conf=conf)

spark = SparkSession(sc)
# dataset = spark.read.csv('D:\BaiduNetdiskDownload\iris.csv',header=False)
dataset = spark.read.format('libsvm').load('D:\spark-2.3.3-bin-hadoop2.7\data\mllib\sample_kmeans_data.txt')
kmeans = KMeans().setK(4).setSeed(1)
model = kmeans.fit(dataset)
predictions = model.transform(dataset)

# Evaluate clustering by computing Silhouette score
evaluator = ClusteringEvaluator()

silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette))

# Shows the result.
centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)

# txt = sc.textFile('D:\BaiduNetdiskDownload\iris.csv')
# iris = txt.map(lambda x:x.strip().split(',')).map(lambda x:Row(sepal_length = x[0],
#                                                              sepal_width = x[1],
#                                                              petal_length = x[2],
#                                                              petal_width = x[3],
#                                                              clzz = x[4]))
# df = spark.createDataFrame(iris)
# df.createOrReplaceTempView('iris')
# spark.sql('select sum(petal_width) from iris').show(10)

