
import pandas as pd
import numpy as np

info =np.array(['H', 'e', 'l', 'l', 'o'])
a = pd.Series(info)
print(a)

print("-" * 60)
info = {1 :'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(f"info :{info}")

a = pd.Series(info)
print(a)
