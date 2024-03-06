# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:15:29 2024

@author: Suhrob
Theme: Functions last word
"""
from math import sqrt
import random as r

uzunlik = lambda pi, r :2*pi*r
#print(uzunlik(math.pi,10))

kvadrat = lambda x, y  : x**y
#print(kvadrat(3, 2))

def daraja(n):
    return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)
#print(f"3-ning kvadrati {kvadrat(3)} ga, "
#      f"kubi {kub(3)} ga teng")

sonlar = list(range(11))
ildizlar = list(map(sqrt, sonlar))
#print(ildizlar)

def daraja2(x):
    return x*x

#print(list(map(daraja2, sonlar)))

kvadratlar = list(map(lambda x :x*x, sonlar))
#print(kvadratlar)

kvadrats = []
for son in sonlar:
    kvadrats.append(son*son)
#print(kvadrats)    

a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x,y:x+y, a,b))
#print(a_plus_b)

sonlar = r.sample(range(100), 10)
#print(sonlar)
def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaruvchi funksiya"""
    return x%2==0

#juftmi_sonlar = list(filter(juftmi, sonlar))
#print(juftmi_sonlar)

juftSonlar = list(filter(lambda son:son%2==0, sonlar))
#print(juftSonlar)

mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
harf = 'a'
mevalar_b = list(filter(lambda meva:meva.startswith(harf),mevalar))
#print(mevalar_b)

mevalar2 = list(filter(lambda meva: len(meva)<=5, mevalar))
#print(mevalar2)

print(list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar)))

















