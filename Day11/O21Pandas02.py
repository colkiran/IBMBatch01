
import pandas as pd

x = ['C', 'C++', 'Python', 'numpy', 'Pandas']
print(f"x :{x}")

df = pd.DataFrame(x)
print(f"dataframe :{df}")

print("-" * 60)

data = {'id':[100, 200, 300], 'Department':['Bsc', 'Btech', 'Mtech']}
df = pd.DataFrame(data)
print(f"df :{df}")

print("-" * 60)
data = {'one': pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f']), 'two': pd.Series([1,2, 3, 4, 5, 6, 7, 8], index= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])}
print(f"data: {data}")
