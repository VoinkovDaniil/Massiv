from random import *
mass=[]
mass=[randint(1982,2003) for f in range(30)]
print(mass)


max=999999
min=0
for i in mass:
    if i<max:
        max=i
    if i>min:
        min=i
bolshe=min-max
print("старший:",max,"младший:",min,"на сколько старше",bolshe,)

