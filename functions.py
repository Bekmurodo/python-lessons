# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 20:23:42 2024

@author: Suhrob
Theme: Functions
"""

#def salom_ber():
#    """Salom beruvchi funksiya"""
#    print("Assalomu alaykum")
#salom_ber()

#def salom_bergin(ism):
#    """Fodyalanuvchi ismini qabul qilib,
#    unga salom beruvchi funksiya"""
#    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
    
#salom_bergin('hasan')
#salom_bergin()

#def toliq_ism(ism, familiya):
#    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#    print(f"Foydalanuvchi ismi: {ism.title()}\n"
#          f"Foydalanuvchi familiyasi: {familiya.title()}")

#toliq_ism('suhrob', 'bekmurodov')

#def yosh_hisobla(ism, t_yil):
#    """Foydalanuvchi yoshini hisoblaydigan dastur"""
#    print(f"{ism.title()} {2024-t_yil} yoshda")

#yosh_hisobla(t_yil=2002, ism='suhrob')

#def yosh_hisobla(tugilgan_yil, joriy_yil=2024): # joriy yil uchun st.qiymat 2020
#    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
#yosh_hisobla(2002)   
    
#def yosh_hisobla(tugilgan_yil, joriy_yil=2024):
#    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
#tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#yosh_hisobla(tugilgan_yil)
    
#Amaliyot
#Task 1
def info(ism, familiya, t_yil, joriy_yil=2024):
    """Foydalanuvchidan malumot qabul qilib yoshini hisoblovchi dastur"""
    print(f"{ism.title()} {familiya.title()} {joriy_yil-t_yil} yoshda.")
  
#info('suhrob', 'bekmurodov', 2002)
    
def kub(son):
    """Foydalanuvchidan son olib uni kvadrat va kubga kutaruvchi dastur"""
    print(f"{son} ning kvadrati {son**2} ga teng")
    print(f"{son} ning kubi {son**3} ga teng")

def son_turi(son):
    """Foydalanuvchidan son olib uning musbat yoki manfiy ekanini aniqlovchi dastur"""
    if son % 2:
       print("Manfiy son")
    else:
       print('Musbat son')    
    
def katta_son(son1, son2):
    """Kiritilgan sonning kattasini consolga chiqaruvchi son"""
    if son1 > son2:
        print(son1)
    elif son1 == son2:
        print("Sonlar teng")
    else:
        print(son2)
    
def daraja(son, son1=2):
    print(f"{son**son1}")
    
#daraja(1000)
 
def bolinish(son):
    """Foydalanuvchidan son qabul qilib,
    sonni 2 dan 10 gacha bo'lgan sonlarga
    qoldiqsiz bo'linishini tekshiruvchi funksiya """
    for n in range(2,11):
       if not son%n:
           print(f"{son} {n} ga qoldiqsiz bo'linadi")
           
bolinish(70)













   
    