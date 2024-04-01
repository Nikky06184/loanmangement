import pandas as pd

col1 = ["age","classess","rollno"]
df1 = pd.DataFrame(columns = col1 )

age1 =[3,54,23,56,76,32]

classes1 = ["A","B","C","D","A","B"]

rollno1 = [5,2,7,9,1,3]

df1 ["age"]= age1
df1["classess"]= classes1
df1["rollno"] = rollno1
#  it is method to convert raw(data or iin py file to csv file by using df.to_csv)  to csv file
df1.to_csv("my2practicefile.csv", index=False)
print(df1.head())
print("nikky3")

