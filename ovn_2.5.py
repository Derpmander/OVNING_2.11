import math#importerar math
x1=float(input("Kordinat för x1: "))#läser in x1
x2=float(input("Kordinat för x2: "))#läser in x2
y1=float(input("Kordinat för y1: "))#läser in y1
y2=float(input("Kordinat för y2: "))#läser in y2
s=(x1-x2)**2+(y1-y2)**2#räknar ut avståndet innan roten ur
o=math.sqrt(s)#tar ut rotten och skapar rotten ur
print(o,"cm")#skriver ut avståndet