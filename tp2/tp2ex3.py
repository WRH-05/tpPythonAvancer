import random as rn
import math as m

b=rn.sample(range(5), 3)
print(b)
a=list(rn.randint(0, 4) for _ in range(3))
print(a)
elts = list(range(10))
rn.shuffle(elts)
print(elts)
