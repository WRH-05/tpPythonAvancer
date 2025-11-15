# tp3_ex03_2.py
# 2ème méthode
import pandas as pd

rows = int(input("Enter the number of rows: "))
print("Enter the matrix values separated by comma followed by newline:")
data = [input().split(',') for _ in range(rows)]
df = pd.DataFrame(data)
print(df)
