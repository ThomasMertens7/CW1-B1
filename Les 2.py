# We zoeken de oplossingen van een vierkenatsvergelijking d.m.v. een algorithme
# Het programma leest de coefficieten a, b en c in.
# Het programma schrijft uit of er geen wortels zijn, precies 1 wortel of 2 wortels.
# Als er wortels zijn, wordt de
# waarde van elke wortel uitgeschreven
from math import *
a=float(input("Geef coefficient a: "))
b=float(input("Geef coefficient b: "))
c=float(input("Geef coefficient c: "))

# In python behoren 53 bits bij de mantissa en 11 bits bij de exponent
# Mantissa bv 241 en exponent bv 2 dan 0.241*10^2=24.1
# Mantissa bv 10110 en exponent 110 in binaire getallen 0.10110*2^110
# 1*2^-1+0*2^-2+1*2^-3+1*2^-4+0*2^-5  * 2^6
# De notaties 6E5/6e5 of 6E-5 zijn leesbaar door python
# De function float maakt van een string een getal, een floating point blijft zo, een geheel getal krijgt .0 "NaN" (Not a number) of "inf"/"-inf" zijn speciale gevallen
# Nooit gewoon inf of NaN typen! Altijd float("inf") of float("NaN")
# Zet geen breuken in de string of andere operators in de string!
# Niet alle getallen kunnen exact worden omgezet van decimaal naar binair, dit zou een oneindig aantal bits vragen
# Bit       2^-n       Rest
#  0        2^-1=0.5     0
#  0        2^-2=0.25    0
#  0        2^-3=0.125   0
#  1        2^-4=0.0625  0.0375
#  1        2^-5=0.03125 0.00625
#  0        2^-6=0.015625 ....
# Zal oneindig lang doorgaan, we kunnen het dus nooit kunnen voorstellen in binaire getallen
# Zo zijn er ook decimale getallen zoals 1/3
# 0.1+0.2=0.30000000004, want het kan niet perfect gevormd worden met binaire getallen
# Wanneer 25.0//6.0=4.0 want floating point gedeeld door floating point blijft floating point
# != is een ongelijkheid

if (a==0) and (b==0) and(c!=0):
    print("Error")
elif (a==0) and (b==0) and(c==0):
    print("De vergelijking klopt voor elke x-waarde")
elif (a==0):
    x=-c/b
    print("x-waarde bedraagt: " , x)
else:
    discriminant=b**2-4.0*a*c
    print("Discriminant bedraagt:",discriminant)
    if discriminant < 0.0:
        print("Geen oplossingen!")
    elif discriminant == 0.0:
        x=-b/(2.0*a)
        print("1 x-waarde:", x)
    else:
        wortel_discriminant=sqrt(discriminant)
        if b>=0:
            grootste_x=(-b-wortel_discriminant)/(2.0*a)
        else:
            grootste_x=(-b+wortel_discriminant)/(2.0*a)
        kleinste_x=c/(a*grootste_x)
        print("2 Wortels:", grootste_x, kleinste_x)
    
    

