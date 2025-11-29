# tp3_ex03_3.py
# Demander la saisie d'une matrice
import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = np.fromstring(input(), sep=",").reshape(rows, cols)
print(matrix)
