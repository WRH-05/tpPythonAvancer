import cmath as cm
import math as m
import fractions as fr 
x = m.pi/3
print(x)

a = m.sin(2*x+1)/(m.cos(x)+1)
print(a)

print("%s = %e" % ("a", a))
b= 2**x + m.log10(abs(1-m.exp(1)))
print("b = %f \nb = %d" %(b,b) )
c1 = 3+4j
c2 = 2.5*cm.exp(3j)

print(f"partie relle c1 {c1.real}")
print(f"partie imaginaire c1 {c1.imag}")
print(f"conjuge c1 {c1.conjugate()}")

print(f"partie relle c2 {c2.real}")
print(f"partie imaginaire c2 {c2.imag}")
print(f"conjuge c2 {c2.conjugate()}")



print(complex(3, 4), cm.phase(complex(3, 4))) # cmath.phase(x)
print(f'arg(c1)= %f' % cm.phase(c1))
print(f'arg(c1)= %f' % cm.phase(c2))
print(cm.polar(c1)) # cmath.polar(x)
print(cm.polar(c2))
print('C3 = {:.02f}'.format(cm.rect(5, 0.9273))) # cmath.rect(x)
x1=fr.Fraction(1, 2) # fraction.Fraction(a,b)
x2=fr.Fraction(2, 3)
print('{} + {} = {}'.format(x1,x2,x1+x2))
print(f'{x1} + {x2} = {x1+x2}')