import pandas as pd
import numpy as np

# Define the number of records
num_records = 100

# Create dummy data for loan dataset
loan_data = pd.DataFrame({
    'Loan_ID': ['LOAN' + str(i).zfill(3) for i in range(1, num_records + 1)],
    'Applicant_Age': np.random.randint(20, 70, num_records),
    'Loan_Amount': np.random.randint(5000, 50000, num_records),
    'Loan_Term_Months': np.random.randint(12, 60, num_records),
    'Credit_Score': np.random.randint(300, 850, num_records),
    'Employment_Years': np.random.randint(1, 30, num_records),
    'Income': np.random.randint(20000, 100000, num_records),
    'Loan_Status': np.random.choice(['Approved', 'Rejected'], num_records)
})

print(loan_data.head(20))
print(loan_data.shape)
print(loan_data["Applicant_Age]")
print(loan_data.head(10))


# Save the DataFrame to a CSV file
loan_data.to_csv('loan_data.csv', index=False)

# print("Loan dataset saved to 'loan_data.csv'")
