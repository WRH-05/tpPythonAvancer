
# Exercice 1 : les chaînes de caractères
print("bonjour tout le monde")
print("bonjour\n tout le monde")
print(r"bonjour\n tout le monde")
"bon" + "jour"
a = """bonjour
... a tous"""
print (a)
(a + '') * 2
a[0]
a[-1]
a[2:4]
a[-4:]
a[:]
a = "bonjour"
a.startwith("bon")
'jour' in a
" bonjour ".strip()
"bonjour a tous".split()

# Exercice 2 : les nombres flottants
print ('-'*20+'\n'+'Exercice 2 :')
0.1+ 0.2 
float.hex(0.1)
float.hex(0.2)
float.hex(0.1+0.2)
float.hex(0.3)

# arrondi inferieur: finit par un  3
print("{0:.32f}".format(0.1))
print("{0:.32f}".format(0.2))
print("{0:.32f}".format(0.3))

# exercice 3 : les nombres complexes
print('{}\n\tExercice 3:'.format('_'*30 ))

1j * 1j
import cmath
cmath.sqrt(-1)
a = 3 + 4j
a.real, a.imag
a * a.conjugate()


# exercice 4
"la valeur de '%.3s' est %d" % ('pi', 3.14159)
"la valeur de '{nom:3s}' est {valeur:.4f}".format(nom="pi", valeur=3.14159)
nom= "pi"
valeur = 3.14159
f"la valeur de {nom:>3s} est {valeur:.4f}"
f"{nom=:>3s} {valeur=:.4f}" 

#exercice 5
s1 = set(range(3))
s2 = set(range(0, -3, -1))
s1, s2
s1 | s2 # union
s1 & s2 # intersection
s1 - s2 # différence
chr(169) # chr(code_ascii)
list (range(5))
[i for i in range(5)] # équivalent à list(range(5))
[str(i) for i in [0, 1, 2, 3, 4]]
[i ** 2 for i in (0, 1, 2, 3, 4)]
[x.upper() for x in "hello"]
[i for i in range(10) if i % 2 == 0]
[(i, j) for i in range(4) for j in range(4) if i < j]