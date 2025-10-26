import random as rn


def script():
    while True:
        username = input("entrer un nom de plus de 3 caracteres:")
        if username.isalpha() and len(username) > 3:
            b = rn.randint(0,20)
            if b<10:
                print(f"{username} ajourne \nmoyenne:{b}")
            else:
                print(f"{username} admis \nmoyenne:{b}")
            break
        else:
            print("Le nom doit contenir uniquement des lettres et avoir plus de 3 caractères.")

script()