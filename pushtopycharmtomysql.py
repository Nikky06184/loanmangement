import pandas as pd
from  sqlalchemy import create_engine

engine = create_engine ("mysql+mysqlconnector://root:Test1234!%@localhost/nik")


table_name = "company1"

df1 = pd.read_csv("my2practicefile.csv")

print(df1)

df1.to_sql(name = table_name,con = engine ,if_exists="replace",index =False)

engine.dispose()

print("welcomenikky")





