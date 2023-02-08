from pyspark.sql import SparkSession
spark = SparkSession.builder \
        .master('local') \
        .appName('EsempioSpark')\
        .getOrCreate()

df=spark.read.jason('contob')


spark.stop()
