import pandas as pd


col = ["name",'age','salary']
#
#
df= pd.DataFrame(columns=col)
# print(df)

nam1 = ["nisha","manish","kartik","alok","kriti","avinash","mahesh","Tripati","kamal","laxmai"]

age1 = [23,53,21,24,56,77,50,34,32,33]

salary1 = [56000,30000,20000,70000,89000,25000,20000,30000,65000,340000]
#
#
df["name"]=nam1
df["age"]=age1
df["salary"]=salary1

print("nikky1 ",df)

df.to_csv("customer_loan_data.csv",index=False)


print("niikky2")



