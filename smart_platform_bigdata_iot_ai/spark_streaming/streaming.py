from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "traffic_topic") \
    .load()

df = df.selectExpr("CAST(value AS STRING)")

query = df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()