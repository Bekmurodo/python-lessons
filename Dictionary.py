# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 12:23:59 2024

@author: Suhrob
Theme: Dictionary
"""
car_0 = {'model':'ferrari','rang':'qizil'}
#print(car_0['model'])
#print(car_0['rang'])

en_uz = {'apple':'olma', 'apricot':"o'rik", 'banana':'banan'}

mevalar = {'olma':10000, 'tarvuz':8000, 'qovun':10000}
#print(f"Olma narxi {mevalar['olma']} so'm")

talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2000}
#print(f"{talaba_0['ism'].title()},\
# {talaba_0['t_yil']}-yilda tu'gulgan.\
# {talaba_0['yosh']} yoshda") 

talaba_0['kurs'] = 4
talaba_0['fakultet'] = 'informatika'
talaba_0['ism'] = 'abdulloh'
talaba_0['yosh'] = 22


#Bosh royxatga lugat qoshish
talaba_1 = {}
talaba_1['ism'] = 'qobil rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 21
#print(talaba_1)
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
talaba_1['kurs'] = 4
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2000}
#print(talaba_0)
#del talaba_0['yosh']
#print(talaba_0)

telefonlar = {
    'ali': 'iphone X',
    'vali': 'galaxi s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310',
    'anvar': 'pixel 3'
    }

#phone = telefonlar.get('Hasan',)
#print(phone)

#Amaliyot 
#Task №1
otam = {}
onam = {}
akam = {}
men = {}
otam['ism'] = 'Haydarqul Bekmurodov'
otam['yosh'] = 55
otam['manzil'] = 'Kuybesh'
#print(f"Otamning ismi {otam['ism']}\
# yoshi {otam['yosh']} da\
# {otam['manzil']} da tug'ulgan")

onam['ism'] = 'Habiba Abdurasulova'
onam['yosh'] = 53
onam['manzil'] = 'Qumsangir'
#print(f"Onamning ismi {onam['ism']}\
# yoshi {onam['yosh']} da\
#{onam['manzil']} rayonida tug'ulgan")

#Task 2
favorite_foods = {
    'otam':'mantu',
    'ayam': 'osh',
    'men':'sho\'rva',
    'opam':'go\'sht',
    'bobom':'kabob'
    }
#print(f"Ayamning sevimli taomi {favorite_foods['ayam']}")
#print(f"Otamning sevimli taomi {favorite_foods['otam']}")
#print(f"Opamning sevimli taomi {favorite_foods['opam']}")

#Task 3
lugat = {
    'integer' : 'butun son',
    'float' : "O'nlik son",
    'string' : 'matn',
    'for' : 'takrorlanuvchi sikl',
    'or' : 'yo',
    'and' : 'va',
    'if' : 'agar',
    'elif' : 'yoki agar',
    'else' : 'yoki',
    'del' : ' elementni indeksi bilan ochirish',
    'range' : 'sanoq',
    'len' : 'uzunlik, element miqdori',
    'append' : 'element qoshish',
    'remove' : 'malum elementni ochirish',
    'strit' : 'elementdagi keraksiz bo\'sh joylarni ochiradi',
    'True' : 'to\'gri',
    'False' : 'noto\'gri',
    'in' : 'ichida',
    'not in' : 'ichida emas',
    'get' : 'biron elementni olish'
    }

#user = input("Kalit so'z kiriting: ")
#print(lugat.get(user, "Bunday so'z mavjud emas."))

kalit = input("Kalit so'z kiriting: ").lower()
tarjuma = lugat.get(kalit)
if tarjuma==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjuma} deb tarjuma qilinadi")
    







