# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 17:13:32 2024

@author: Suhrob
Theme: Function and list
"""
#def bahola(ismlar):
#    baholar = {}
#    while ismlar:
#        ism = ismlar.pop()
#        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#        baholar[ism] = int(baho)
#    return baholar


talabalar = ["ali", "vali", "hasan", "husan"]
#baholar = bahola(talabalar[:])
#print(baholar)
#print(talabalar)

def katta_harf(names):
    name = []
    while names:
        for ism in names[:]:
            name.append(ism.title())
        return name

talabalar = ["ali", "vali", "hasan", "husan"]
#print(katta_harf(talabalar))
#print(talabalar)

def baholar(ismlar):
    baholar = {}
    for ism in ismlar[:]:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism.title()] = int(baho)
    return baholar
   
end = baholar(talabalar)
print(end)












