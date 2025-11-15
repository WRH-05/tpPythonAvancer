# tp3_ex03_3.py
# 3ème méthode
import pandas as pd

rows = int(input("Enter the number of rows: "))
print("Enter the matrix values separated by ; followed by newline:")
data = [input().split(';') for _ in range(rows)]
df = pd.DataFrame(data)
print(df)