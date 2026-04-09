import pandas as pd 
s = ([10, 20, 30, 40, 50])
print(pd.Series(s))
data = {
  "Name": ["Avnish", "Raman", "Vinayak"],
  "Marks": [86, 90, 95]
 }
df = pd.DataFrame(data)
print(df)

data =  {
    "Student": ["Avnish", "Raman", "Vinayak"],
    "Marks" : [87, 90, 96],
    "Age" : [18,19,20],
                  
  }
df = pd.DataFrame(data)
print(df.head(2))
print(df.tail(1))
print(df.columns)
print(df.describe())

