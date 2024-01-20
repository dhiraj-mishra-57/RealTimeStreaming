from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkStreaming").\
    config("spark.jars", r"C:\Users\dhira\Downloads\postgresql-42.7.1.jar").\
    getOrCreate()

properties = {
                "driver": "org.postgresql.Driver",
                "url": "jdbc:postgresql://localhost:5432/postgres",
                "user": "postgres",
                "password": "mysecretpassword",
                "dbtable": "customer"
                }

# df = spark.read.format("jdbc").options(**properties).load()

# df = spark.readStream.format("socket").option("host","localhost").\
#     option("port",5432).\
#     option("table","customer").\
#     option("user","postgres").option("password","mysecretpassword").load().awaitTermination()

# df = spark.readStream.format("socket").options(**properties).load()
# print(df.isStreaming())
print(df.printSchema())