#tp3_exo4.py
import numpy as np

def resoudre_systeme(A, b):
    solution = np.linalg.solve(A, b)
    return solution


def verifier_solution(A, b, x):
    resultat = np.dot(A, x)
    est_correcte = np.allclose(resultat, b)
    
    print("\nVerification:")
    print(f"A x x = {resultat}")
    print(f"b     = {b}")
    print(f"Solution correcte: {est_correcte}")
    
    return est_correcte


def systeme_predetermine():
    print("\nPartie 1 & 2: Systeme predetermine")
    
    A = np.array([[1, 5], [2, 9]], dtype=float)
    b = np.array([2, 3], dtype=float)
    
    print(f"\nSysteme: x + 5y = 2")
    print(f"         2x + 9y = 3")
    
    solution = resoudre_systeme(A, b)
    
    print(f"\nSolution:")
    print(f"x = {solution[0]:.6f}")
    print(f"y = {solution[1]:.6f}")
    
    verifier_solution(A, b, solution)


def systeme_utilisateur():
    print("\nPartie 3: Systeme utilisateur")
    
    n = int(input("\nNombre d'equations (2-5): "))
    
    A = np.zeros((n, n))
    b = np.zeros(n)
    
    print("\nSaisie des coefficients:")
    for i in range(n):
        print(f"\nEquation {i+1}:")
        for j in range(n):
            A[i][j] = float(input(f"  Coefficient {j+1}: "))
        b[i] = float(input(f"  Constante: "))
    
    solution = resoudre_systeme(A, b)
    
    print(f"\nSolution:")
    for i in range(n):
        print(f"x{i+1} = {solution[i]:.6f}")
    
    verifier_solution(A, b, solution)


def main():
    systeme_predetermine()
    
    reponse = input("\nResoudre un autre systeme? (o/n): ").lower()
    if reponse in ['o', 'oui']:
        systeme_utilisateur()
    
    print("\nProgramme termine.")


if __name__ == "__main__":
    main()