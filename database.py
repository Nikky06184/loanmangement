import pandas as pd
import mysql . connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  port =3306,
  database = "nik",
  # database = "nikkydb",
  password="Test1234!%"
)
print("n")
mycursor = mydb.cursor()
# mycursor.execute("select * from emp ")
mycursor.execute("select * from company1 ")
results = mycursor .fetchall()

# Print the results
for row in results:
    print(row)

# Close cursor and database connection
mycursor.close()
mydb.close()
print("n111")




