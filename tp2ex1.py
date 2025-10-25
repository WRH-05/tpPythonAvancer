def pgcd(a: int, b: int) -> int:
    """Calcul du PGCD de deux entiers.
    Les paramètres a et b sont convertis en entier avant le calcul du PGCD.
    Une exception ValueError est levée si un des entiers est négatif ou nul.
    """
    a, b = int(a), int(b)
    if (a <= 0 or b <= 0):
        raise ValueError("a et b doivent être deux entiers positifs")
    while a != b:
        if (a > b):
            a = a - b
        else:
            b = b - a
    return a


def print_pgcd(elts: list) -> None:
    for (a, b) in elts:
        try:  # séquence à protéger des exceptions
            x = pgcd(a, b)
        except ValueError as e:
            # traitement de l'exception ValueError
            print(f"ValueError: {e}")
        else:  # exécuté si aucune exception n'est levée (bloc optionnel)
            print(f"pgcd({a}, {b}) = {x}")
        finally:  # exécuté dans tous les cas (bloc optionnel)
            print("------")