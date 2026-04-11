import pandas as pd 
data = {
    "name": ["a", "b", "c", "d"],
    "marks": [86, 90, 80, 78],
    "age": [20, 21, 19, 22]
    }
df = pd.DataFrame(data)
print(df["marks"])
print(df[["name", "age"]])
print(df.loc[0])
print(df.iloc[1])
print(df.loc[1, "age"])

