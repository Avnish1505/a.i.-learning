import pandas as pd
data = {
    'Name': ['Avnish', 'Ashutosh', 'Amit'],
    'Age': [25, 30, 28],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}
df = pd.DataFrame(data)
print(df.loc[2])