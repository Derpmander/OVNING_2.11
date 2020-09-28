import math
i=float(input("Mätarställning i dag?: "))
v=float(input("Mätarställning för ett år sedan?: "))
m=i-v
print("Antal mil körda?: ",m)
b=float(input("Antal liter?: "))
p=b/m
print("Förbrukning per mil:",p)