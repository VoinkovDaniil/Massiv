from random import*
mass=[]
for f in range(100):
    mass.append(int(random()*100))
print(mass)

mx = mass[0]
mn = mass[0]
max=0
min=999
for i in mass:
    if mass[i]>mx:
        max=i; mx=mass[i]
    if mass[i]<mn:
        min=i; mn=mass[i]
naib=mx-mn
 
print("ind max=",max, "ind min=",min, "max=",mx, "min",mn,"naib=",naib,)
