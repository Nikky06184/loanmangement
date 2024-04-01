# import pandas as pd

import mysql . connector

con1 = mysql.connector.connect(
    host = "localhost",
    user  = "root",
    port = 3306,
    database = "nik",
    password = "Test1234!%"

)

con2 = con1.cursor()
con2.execute("select * from company")
c1 = con2.fetchall()

for i in c1:
    print(i)

con2.close()


