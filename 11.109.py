from random import *
mass=[]
for f in range (50):
    mass.append(int(random()*100))
print(mass)

max=0
for i in mass:
    if i>max:
        max=i
print("Самый дорогой=",max,)
