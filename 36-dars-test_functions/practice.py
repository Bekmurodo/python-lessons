# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:03:03 2024

@author: Suhrob
"""
def katta_son(a,b,c):
    if a > b and c:
        max = a
    if c > a and b:
        max = c
    if b > a and c:
        max = b
    return max

#print(katta_son(111, 44, 789))


talabalar = ['ali', 'vali', 'hasan', 'husan']

def bigFirstWord(ismlar):
    royxat = []
    for ism in ismlar:
        royxat.append(ism.title())
    return royxat

centense = bigFirstWord(talabalar)
#print(centense)
        

def juftson(sonlar):
    jsonlar = []
    for son in sonlar:
        if son  % 2:
            pass
        else:
            jsonlar.append(son)
    return jsonlar

raqamlar = [12,45,81,27,347,76,90,45,24,10,54,67]

son = juftson(raqamlar)
print(son)









