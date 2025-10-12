
# Exercice 1 : les chaînes de caractères
print("bonjour tout le monde")  # affiche une salutation simple
print("bonjour\n tout le monde")  # affiche avec un saut de ligne explicite (\n)
print(r"bonjour\n tout le monde")  # raw string: affiche le littéral \n au lieu d'un saut de ligne
"bon" + "jour"  # concaténation de chaînes; expression évaluée mais non affichée ni stockée
a = """bonjour
... a tous"""  # chaîne multi-lignes assignée à la variable a
print (a)  # affiche la variable a (contient la chaîne multi-lignes)
(a + '') * 2  # concatène a avec une chaîne vide puis répète 2 fois; résultat non affiché
a[0]  # indexation: premier caractère de a (évalué mais non affiché)
a[-1]  # indexation négative: dernier caractère de a (évalué mais non affiché)
a[2:4]  # slicing: sous-chaîne de l'indice 2 inclus à 4 exclus (évalué mais non affiché)
a[-4:]  # slicing: les 4 derniers caractères de a (évalué mais non affiché)
a[:]  # copie via slicing: renvoie toute la chaîne (évalué mais non affiché)
a = "bonjour"  # réaffecte a à une nouvelle chaîne
# Remarque : la ligne suivante contient une faute de frappe (startwith au lieu de startswith)
a.startswith("bon")  # ERREUR: provoquera AttributeError; corriger en a.startswith("bon")
'jour' in a  # test d'appartenance: True si 'jour' est une sous-chaîne de a (évalué mais non affiché)
" bonjour ".strip()  # supprime les espaces en début/fin; résultat non affiché
"bonjour a tous".split()  # découpe la chaîne en liste de mots en utilisant les espaces (évalué mais non affiché)

# Exercice 2 : les nombres flottants
print ('-'*20+'\n'+'Exercice 2 :')  # affiche une ligne de séparation et le titre Exercice 2
0.1+ 0.2  # addition de flottants; résultat non affiché
float.hex(0.1)  # affiche la représentation hexadécimale interne du flottant 0.1 (évalué mais non affiché)
float.hex(0.2)  # idem pour 0.2
float.hex(0.1+0.2)  # hex du résultat de 0.1+0.2 — utile pour voir la valeur binaire exacte
float.hex(0.3)  # hex de 0.3 pour comparer

# arrondi inferieur: finit par un  3 (note en français sur le comportement d'arrondi observé)
print("{0:.32f}".format(0.1))  # affiche 0.1 avec 32 décimales pour montrer les artefacts de représentation
print("{0:.32f}".format(0.2))  # idem pour 0.2
print("{0:.32f}".format(0.3))  # idem pour 0.3

# exercice 3 : les nombres complexes
print('{}\n\tExercice 3:'.format('_'*30 ))  # affiche un séparateur puis 'Exercice 3:'

1j * 1j  # multiplication de nombres imaginaires (résultat évalué mais non affiché)
import cmath  # import du module des fonctions complexes
cmath.sqrt(-1)  # racine carrée complexe de -1 (évaluée mais non affichée)
a = 3 + 4j  # affectation d'un nombre complexe à a
a.real, a.imag  # accède aux parties réelle et imaginaire (évalué mais non affiché)
a * a.conjugate()  # multiplie a par son conjugué (donne un réel: norme au carré) (évalué mais non affiché)


# exercice 4
"la valeur de '%.3s' est %d" % ('pi', 3.14159)  # ancienne syntaxe de formatage (ici incorrecte: %d pour float)
"la valeur de '{nom:3s}' est {valeur:.4f}".format(nom="pi", valeur=3.14159)  # format() avec noms de champs
nom= "pi"  # variable nom
valeur = 3.14159  # variable valeur (float)
f"la valeur de {nom:>3s} est {valeur:.4f}"  # f-string formatée (évaluée mais non affichée)
f"{nom=:>3s} {valeur=:.4f}"  # f-string utilisant l'affichage "name=value" (évaluée mais non affichée)

#exercice 5
s1 = set(range(3))  # crée un ensemble {0,1,2}
tuple(range(5))  # crée un tuple (0,1,2,3,4) (évalué mais non affiché)
s2 = set(range(0, -3, -1))  # crée un ensemble en décrémentant: {0, -1, -2}
s1, s2  # tuple contenant s1 et s2 (évalué mais non affiché)
s1 | s2 # union des ensembles (évalué mais non affiché)
s1 & s2 # intersection des ensembles (évalué mais non affiché)
s1 - s2 # différence des ensembles (évalué mais non affiché)
chr(169) # caractère correspondant au code Unicode 169 (©) (évalué mais non affiché)
list (range(5))  # liste des entiers 0..4 (évaluée mais non affichée)
[i for i in range(5)] # compréhension de liste équivalente à list(range(5))
[str(i) for i in [0, 1, 2, 3, 4]]  # convertit les entiers en chaînes
[i ** 2 for i in (0, 1, 2, 3, 4)]  # carrés des entiers 0..4
[x.upper() for x in "hello"]  # met en majuscule chaque caractère de la chaîne
[i for i in range(10) if i % 2 == 0]  # liste des nombres pairs entre 0 et 9
[(i, j) for i in range(4) for j in range(4) if i < j]  # liste de tuples (i,j) avec i<j
