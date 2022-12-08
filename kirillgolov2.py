from math import *
from random import *


#1---------------------------------------
print("Puu läbimõõdu arvutamine")
C=float(input("Puu ümbermõõt: "))
d=2*(C/(2*pi))
print(f"Vastus:\nPuu läbimõõduga {C} ümbermõõt võrdub {d}")
print("Ristkülikukujulise maatüki diagonaal")
N=float(input("Sisesta ristküliku 1. külje pikkus => "))
M=float(input("Sisesta ristküliku 2. külje pikkus => "))
d=sqrt(N**2+M**2)
print(f"Maatüki diagonaal on {d} m**2")

aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus

#2---------------------------------------

print("Sinu kiirus oli " + " km/h")

A1=int(input("Siseta 1. arv => "))
A2=int(input("Siseta 2. arv => "))
A3=int(input("Siseta 3. arv => "))
A4=int(input("Siseta 4. arv => "))
A5=int(input("Siseta 5. arv => "))
Keskmine=(A1+A2+A3+A4+A5)/5

#3---------------------------------------

print()
print("Ruudu karakteristikud")
a=float(input("Siseta ruudu külje pikkus => "))
S=a**2
print("Ruudu pindala", round(S,1))
P=4*a 
print("Ruudu ümbermõõt", round(P,1))
di=a*sqrt(2)

#4---------------------------------------
print("  @..@ ")
print(" ´---- ")
print("  \__/ ")
print(" ^^ "" ^^ ") 

#5---------------------------------------

print()
print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => "))

#6---------------------------------------

a=randint(1,100)
b=randint(1,100)
c=randint(1,100)
print(f"Külg a={a}\nKülg b={b}\nKülg c={c}\nKülg")
print("Kolmnurga ümbermõõt = {a+b+с}")
print()

#7---------------------------------------

from math import *
print("3 sõbrad võtsite pitsa hinna 12,90")
s=10*12.90/100
s=round(s)
d=(s+12.90)
print(f"Vastus on {d}")
P=d/3
P=round(P,2)
print(f"Iga sõber maksa: {P}")
print()

#8---------------------------------------

from math import *
ltr=float(input("Sisetage tangitud kütuse liitrid"))
km=float(input("Sisetage läbitud kilomeetrid"))
kk=ltr/km*100
print(str(f"kütusekulu 100 kilomeetri kohta on: {kk}ltr\km"))
print() 

#9---------------------------------------

from math import *
from random import *
a=29.9
t=24
b=24/60
s=b*24
s=round(s,2)
print(f"24 minutiga sõitis: {s}km")

#10---------------------------------------

from random import *
minutit=float(input("Kasutaja sisetage minutit: "))
tunnid=int(minutit//60)
round(tunnid,2)
print(f"Minutit: {minutit}, Tunnid={tunnid}")
print()