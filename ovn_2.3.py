svar=input("Hur många grader i farenheit?: ")#tar in vilken farenheit det är ## kan göras bättre
f=float(svar)#omvandlar svaret till formel formen
c=(f-32)*5/9#räknar om farenheit till celsius
print(c,"grader celsius")#skriver ut vilken grader celsius det är

if c>30:
    print (c,"Sir, it's very hot today")
elif c<-10: 
    print (c,"Sir, bring plenty of clothes")
else:
    print (c, "Sir, the temperature is to your liking")