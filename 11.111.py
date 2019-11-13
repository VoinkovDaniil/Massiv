from random import *
mass=[]
for f in range (25):
    mass.append(int(random()*25))
print(mass)

max=0
for i in mass:
    if i>max:
        max=i
print("Победитель:",max,)
