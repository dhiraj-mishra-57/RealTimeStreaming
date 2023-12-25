from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PostgreSQLExample").config("spark.jars", r"C:\Users\dhira\Downloads\postgresql-42.7.1.jar").getOrCreate()

properties = {
    "driver": "org.postgresql.Driver",
    "url": "jdbc:postgresql://localhost:5432/postgres",
    "user": "postgres",
    "password": "mysecretpassword",
    "dbtable": "customer"
}

df = spark.read.format("jdbc").options(**properties).load()