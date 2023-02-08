from pyspark.sql import SparkSession
spark = SparkSession.builder \
     .master("local") \
     .appName("Esempio Spark") \
     .config("spark.opzione.esempio", "valore-opzione") \
     .getOrCreate()
     
# codice da eseguire

spark.stop()
