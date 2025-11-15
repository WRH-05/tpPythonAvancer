# tp3_exo1.py
import numpy as np

# question 1
A = np.eye(4,4,0)
print(f'A=',A)
A = np.eye(4,4,-1)
print(f'\nA=',A)
A = np.array([[2,1],[3,4]])
print(f'\nA=',A)
C = np.linalg.inv(A)
print(f'\nC=',C)

# question 2
B = np.array([[1,5,9,1], [3,4,1,2], [5,2,0,6]])
print(f'\nB=',B)
B = np.array([1,5,9,1,3,4,1,2,5,2,0,6])
print(f'\nB=',B)
B = B.reshape(3,4)
print(f'\nB=',B)

# question 3
B = B.reshape(4,3)
print(f'\nB=',B)
B = np.transpose(B)
B = np.append(B,[np.array([1,5,9,2])],axis=0)
print(f'\nB=',B)
print(f'Determinant of B:',np.linalg.det(B))

# question 4
# discutons les resultats des questions 2 et 3
print("Les résultats des questions 2 et 3 montrent comment les opérations de transformation de matrice peuvent affecter la structure et les propriétés d'une matrice.")