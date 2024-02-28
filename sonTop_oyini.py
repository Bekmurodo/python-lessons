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
    print(f"Tabriklaymiz. Siz {taxminlar} urunushda topdingiz.") 
            
        