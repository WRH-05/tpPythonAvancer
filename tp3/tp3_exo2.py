import numpy as np

# 1. Une matrice carrée (5×5) nommée cinq remplis par des 5
cinq = np.full((5, 5), 5)
print("1. Matrice carrée 5×5 remplie de 5:")
print(cinq)
print()

# 2. Une matrice transpose de la matrice cinq
transpose_cinq = np.transpose(cinq)
print("2. Transpose de la matrice cinq:")
print(transpose_cinq)
print()

# 3. Une matrice de 2 lignes inclut 10 valeurs uniformément espacées entre 1 et 19
matrice_uniforme = np.linspace(1, 19, 10).reshape(2, 5)
print("3. Matrice de 2 lignes avec 10 valeurs uniformément espacées entre 1 et 19:")
print(matrice_uniforme)
print()

# 4. Une matrice de 3 lignes tient 12 nombres entiers aléatoires dans l'intervalle 0 et 20
matrice_aleatoire = np.random.randint(0, 21, size=(3, 4))
print("4. Matrice de 3 lignes avec 12 nombres entiers aléatoires entre 0 et 20:")
print(matrice_aleatoire)
print()