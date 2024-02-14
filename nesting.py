# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:04:25 2024

@author: Suhrob
Theme: Nesting
"""
car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }

car = car0
#print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']}-yil, {car['narh']}$")

car = car1
#print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']}-yil, {car['narh']}$")

car = car2
#print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']}-yil, {car['narh']}$")


cars = [car0, car1, car2]
#for car in cars:
#    print(f"{car['model'].title()}, "
#          f"{car['rang']} rang, "
#          f"{car['yil']}-yil, {car['narh']}$")

#print(f"{cars[2]['rang'].title()} "
#      f"{cars[2]['model']}")

malibus = []
for n in range(10):
    new_car = {
        'model':'malibu',
        'rang':None,
        'yil':2020,
        'narh':None,
        'km':0,
        'korobka':'avto'
        }

    malibus.append(new_car)

for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'


for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'


for malibu in malibus[6:]:
    malibu['rang'] = 'oq'
    malibu['korobka'] = 'mexanika'

for malibu in malibus:
    if malibu['korobka'] == 'avto':
        malibu['narh']=40000
    else:
        malibu['narh']=35000


dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} qutidagi dasturlash tillarini biladi")
#    for til in tillar:
#        print(f"{til.upper()}", end=' ')
        

hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }

#for ism, info in hamkasblar.items():
#    print(f"\n{ism.title()} {info['familiya'].title()}, "
#          f"{info['tyil']}-yilda tug'ilgan. "
#          f"Ma'lumoti: {info['malumot']}. \n"
#          "Quyidagi dasturlash tillarini biladi:")
#    for til in info['tillar']:
#        print(til.upper())


#Task 1
shaxs_0 = {
    'ism':'Abu Abdulloh Muhammad ibn Ismoil',
    't_yil':810,
    't_joy':'Buxoro',
    'umr':63,
    'asarlar': ['Al-jome as-sahih','Al-adab al-mufrad','At-tarix al-kabir','At-tarix as-sag\'ir']
    }

shaxs_1 = {
    'ism':'Abdulla Qodiriy',
    't_yil':1894,
    't_joy':'Toshkent',
    'umr':44,
    'asarlar': ["O'tkan kunlar",'Mehrobdan Chayon', 'Obid ketmon']
    }

shaxs_2 = {
    'ism':'Erkin Vohidov',
    't_yil':1936,
    't_joy':'Farg\'ona',
    'umr':80,
    'asarlar': ["Tong nafasi", "Qoshiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"]
    }

shaxs_3 = {
    'ism':'Alisher Navoiy',
    't_yil':1441,
    't_joy':'Hirot',
    'umr':60,
    'asarlar': ['Hamsa', 'Lison ut-Tayr', 'Mahbub Al-Qulub','Munojot']
    }

shaxslar = [shaxs_0, shaxs_1, shaxs_2, shaxs_3]
#for shaxs in shaxslar:
#    print(f"{shaxs['ism']} {shaxs['t_yil']}-yilda "
#          f"{shaxs['t_joy']}da tavallud topgan. "
#          f"{shaxs['umr']} yil umr ko'rgan.")

#Task 2
#for shaxs in shaxslar:
#    ism = shaxs['ism']
#    asarlar = shaxs['asarlar']
#    print(f"\n{ism}ning mashxur asarlari: ")
#    for asar in asarlar:
#        print(asar)

oila = {
        'ali': ['terminator','rambo','titanic'],
        'vali': ['tenet', 'inception','intersteller'],
        'hasan': ['abdullajon','bomba','shaytanat'],
        'husan': ['Mahallada duv-duv gap','jhon Wick']
        }
#for ism, kinolar in oila.items():
#    print(f"\n{ism.title()}ning sevimli kinolari:")
#    for kino in kinolar:
#        print(f"{kino.capitalize()}")

davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }

for davlat, info in davlatlar.items():
    if davlat.lower()=="aqsh":
        davlat=davlat.upper()
    else:
        davlat = davlat.capitalize()
#    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()} "
#          f"\nHududi: {info['maydon']} kv.km "
#         f"\nAholisi: {info['aholi']} "
#          f"\nPul birligi: {info['pul birligi']}")
    
davlat = input("Davlat nomini kiriting: ").lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.title()}ning poytaxti {info['poytaxt'].title()} "
          f"\nHududi: {info['maydon']} kv.km "
          f"\nAholisi: {info['aholi']} "
          f"\nPul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida malumot yo'q")









