from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MySQL to PySpark") \
    .config("spark.driver.extraClassPath", "path_to_mysql_connector/mysql-connector-java-X.X.X.jar") \
    .getOrCreate()

jdbc_url = "jdbc:mysql://hostname:port/database"
connection_properties = {
    "user": "localhost",
    "password": "Test1234!%",
    "driver": "com.mysql.jdbc.Driver"
}

df = spark.read.jdbc(url=jdbc_url, table="table_name", properties=connection_properties)

df.show()

spark.stop()

