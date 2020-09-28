i=float(input("Mätarställning i dag?: "))#Läser in dagens mätarställning
v=float(input("Mätarställning för ett år sedan?: "))#läser in mätarställningne för ett år sedan
m=i-v#Räknar ut hur många mil man åkt på ett år
print("Antal mil körda?: ",m)#Läser in atal mil körda
b=float(input("Antal liter?: "))#läser in antal liter
p=b/m#Räknar ut bensin förbrukningen per mil
print("Förbrukning per mil:",p)#Skriver ut förbrukningen per mil