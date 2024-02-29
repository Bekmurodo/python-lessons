# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:08:34 2024

@author: Suhrob
"""
#Komputer
import random as r
def sontop(x=10):
    tasodifiy_son=r.randint(1,x)
    print(f"Men 1 dan {x} gacha bitta son o'yladim topa olasizmi?")
    taxminlar=0
    while True:
        taxminlar+=1
        taxminiy_son = int(input(">>>"))
        if tasodifiy_son>taxminiy_son:
            print("Men o'ylagan son bundan kattaroq. Yana harakat qilib ko'ring.")
        elif tasodifiy_son<taxminiy_son:
            print("Men o'ylagan son bundan kichikroq. Yana harakat qilib ko'ring.")
        else:
            break
        return taxminlar
    print(f"Tabriklaymiz. Siz {taxminlar} ta taxmin bilan topdingiz.") 
            
def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman ")
    quyi = 1
    yuqori = x 
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi !=yuqori:
            taxmin = r.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'gri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq(-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    
def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user>taxminlar_pc:
            print(f"Men {taxminlar_pc} ta taxmin bilan topdim va yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print(f"Siz {taxminlar_user} ta taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(1): "))