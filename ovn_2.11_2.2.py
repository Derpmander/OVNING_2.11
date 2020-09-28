import math #Importerar modulen math för att sedan kunna använda den
r=float(input("Vad är sfärens radie?:"))#Frågar efter radien
v=4*math.pi*r**3/3#räknar ut volymen från radiens data
a=4*math.pi*r**2#räknar ut arean från radiens data
print("Sfärens area är:",a,"Sfärens volym är:",v)#skriver ut både arean och volymen