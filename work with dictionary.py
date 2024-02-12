# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 18:21:05 2024

@author: Suhrob
Theme: Work with dictionary
"""
talaba_0 = {
    'ism': 'alijon',
    'familiya': 'shamshiyev',
    'yosh': 22,
    'fakultet': 'matematika',
    'kurs': 4
    }

#print(talaba_0.items())

#for kalit, qiymat in talaba_0.items():
#    print(f"Kalit: {kalit}")
#    print(f"Qiymat: {qiymat}\n")

telefonlar = {
    'ali': 'iphone X',
    'vali': 'galaxi s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310',
    'anvar': 'pixel 3'
    }

#for k, q in telefonlar.items():
#    print(f"{k.title()}ning telefoni {q}")
    
mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':5000,
    'anjir':25000,
    'shaftoli':30000
    }   
    
#print(mahsulotlar.keys())
    
#print('Dokondagi mahsulotlar: ')
#for mahsulot in mahsulotlar.keys():
#    print(mahsulot.title())
    
 
#print('Dokondagi mahsulotlar: ')
#for mahsulot in mahsulotlar:
#    print(mahsulot.title())
    
#bozorlik = ['uzum', 'anor', 'non', 'baliq']
#for mahsulot in mahsulotlar:
#    if mahsulot in bozorlik:
#        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm\n")
 
#for buyum in bozorlik:
#    if buyum not in mahsulotlar:
#        print(f"Iltimos do'koningizga {buyum} ham olib keling")
        
#print("Do'konimizdagi mahsulotlar:")   
#for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())
    
#print("Foydalanuvchilar quyidagi telefonlardan foydalanadi:")
#for tel in telefonlar.values():
#    print(tel)    
    
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }

#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in set(telefonlar.values()):
#    print(tel)   
    
toys = {"ball", 'car','lamp',"ball"}   
#print(toys)

#Amaliyot
python = {
    'Boolean': 'Mantiqiy qiymat',
    'Float': 'O\'nlik son',
    'For': 'Biror amalni qayta-qayta bajarish tsikli',
    'If': 'Shartlarni tekshirish operatori',
    'Integer': 'Butun son',
    'Else': 'Yoki',
    'String': 'Matn'
    }
#for kalit, qiymat in sorted(python.items()):
#    print(f"{kalit}- {qiymat}")

countries = {
    'aqsh':'vashington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    'qirg\'iziston':'bishkek',
    'singapur':'singapur',
    'italiya':'rim',
    "o'zbekiston":'toshkent',
    'malayziya':'kuala-lumpur',
    'qozoqiston':'nursulton'
    }
#print("Dunyo davlatlari:")
#for davlat, poytaxt in sorted(countries.items()):
#    print(f"{davlat.upper()}")
    
#print("\nDavlatlarning poytaxtlari: ")
#for poytaxt in sorted(countries.values()):
#    print(f"{poytaxt.title()}")

davlat = input("Qaysi davlatning poytaxtini bilishni istaysiz? ").lower()
capital = countries.get(davlat)
if capital == None:
    print("Kechirasiz, bizda bu haqida malumot yo'q ")
else:
    print(f"{davlat.upper()}ning poytaxti {capital.title()} shahri")

















