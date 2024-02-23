# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 20:47:07 2024

@author: Suhrob
Theme: Agrrement functions
"""
def summa(*sonlar):
    """Kiritilgan sonlarning yigindisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

#print(summa(2,6,4))
#print(summa(2,3))
#print(summa(2,6,4,76,54,34,67,29))


def summaa(*sonlar):
    """Kiritilgan sonlarning yigindisini hisoblaydigan funksiya"""
    return sum(sonlar)

#print(summaa(2,6,4))
#print(summaa(2,3))
#print(summaa(2,6,4,76,54,34,67,29))

def suma(x,y,*sonlar):
    """Kiritilgan sonlarning yigindisini hisoblaydigan funksiya"""
    return x+y+sum(sonlar)

#print(suma(2,6,4))
#print(suma(2,7))
#print(suma(2,6,4,76,54,34,67,29))


def avto_info(kompaniya,model,**malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar

avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000, davlat='O\'zbekiston')

#Amaliyot
def kopaytma(*sonlar):
    """Foydalanuvchidan qiymat qabul qilib olib uni ko'paytiradi"""
    yigindi = 1
    for son in sonlar:
        yigindi *= son
    return yigindi

#print(kopaytma(2,6,5))
#print(kopaytma(8,3))

def talabalar(ism,familiya,**malumotlar):
    """talabalar haqidagi malumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar

talaba1 = talabalar("Ilhom", "Shernazarov", yosh=21,malumot="o'rta kaspiy",jins='erkak',boyi=1.70)
print(talaba1)