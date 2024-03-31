import pandas as pd
from sqlalchemy import create_engine

# Establish connection to MySQL
engine = create_engine('mysql+mysqlconnector://root:Test1234!%@localhost/nikkydb')

# Assuming df is your DataFrame
# Replace 'table_name' with the name of your table
table_name = "loannikky"

df = pd.read_csv("customer_loan_data.csv")
print(df)

# Write DataFrame to MySQL database
df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

# Close the connection
engine.dispose()

print("nikky111")