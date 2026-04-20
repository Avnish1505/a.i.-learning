import pandas as pd 
data = {
    "name" : ["a", "b","c","d"],
    "age" : [25, 30, 35, 40],
    "Salary" : [50000, 60000, 70000, 80000]
    }
df = pd.DataFrame(data)
print("Original Data:")
print(df)
# 1. check missing values
print("\nMissing Values:")
print(df.isnull().sum())
#2. fill missing values with mean
df["age"] = df["age"].fillna(df["age"].mean())
df["Salary"] = df["Salary"].fillna(0)
#3. drop rows with missing values 
df_cleaned = df.dropna()
print("\ncleaned data:")
print(df_cleaned)