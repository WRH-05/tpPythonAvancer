# tp3_ex03_1.py
# Demander la saisie d'une matrice
import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print("Enter the matrix values separated by space followed by newline:")
matrix = np.array([input().strip().split() for _ in range(rows)], int)
print(matrix)
