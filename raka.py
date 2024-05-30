# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("PySpark DataFrame Sampleyyy") \
    .getOrCreate()

# Create a sample DataFrame
data = [("John", "Doe", 30),
        ("Jane", "Doe", 25),
        ("Tom", "Smith", 35),
        ("Alice", "Brown", 28)]

columns = ["first_name", "last_name", "age"]

df = spark.createDataFrame(data, columns)

# Display the DataFrame
print("Original DataFrame:")
print(df.show())
#

