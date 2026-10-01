import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'department': ['HR', 'IT', 'Finance', 'Marketing'],
    'age': [25, 30, 35, 40],
    'salary': [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)

df['provident_fund'] = df['salary'] * 0.12  # Calculate provident fund as 12% of salary
df['housing_allowance'] = df['salary'] * 0.2  # Calculate housing allowance as 20% of salary
df['income_tax'] = df['salary'] * 0.15  # Calculate income tax as 15% of salary
df['net_salary'] = df['salary'] - df['income_tax'] - df['housing_allowance'] - df['provident_fund']  # Calculate net salary after deductions

print(df)