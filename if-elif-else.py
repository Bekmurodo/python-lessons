# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 18:15:34 2024

@author: Suhrob
Theme: if-elif-else
"""
#yosh = int(input('Yoshingiz nechida? '))
#if yosh<=4:
#    narh = 0
#elif yosh<=12:
#    narh = 5000
#else:
#    narh = 10000
    
#print(f'Sizga kirish {narh} so\'m')
    
#kun = input("Bugun nima kun?>>>")
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#    print("Bugun dam olish kuni.")
#else:
#    print("Bugun ish kuni.")

#kun = input("Bugun nima kun?")
#harorat = float(input("Havo harorati qanday?"))
#if (kun.lower()=='yakshanba' or 'shanba') and harorat>=30:
#    print("Chomilgani kettik!")
#elif kun.lower()=='yakshanba' and harorat<=30:
#    print("Uyda dam olamiz!")
#else:
#    print("Bugun ish kuni!")

#narh = 15000
#choy = True
#salad = False

#if choy and salad:
#    narh = narh + 10000
#elif choy or salad:
#    narh = narh + 5000

#print(f"Jami {narh} so'm")

narh = 15000
choy = True
salad = False
non = True
kompot = True
assarti = True

#if choy:
#    print("Mijoz choy oldi.")
#    narh = narh + 3000
#if salad:
#    print("Mijoz salad oldi.")
#    narh= narh + 5000
#if non:
#    print("Mijoz non oldi.")
#    narh= narh + 2000
#if kompot:
#    print("Mijoz kompot oldi.")
#    narh= narh + 5000
#if assarti:
#    print("Mijoz assarti oldi.")
#    narh= narh + 15000
#print(f"Jami: {narh} so'm")

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#ovqat = input("Nima ovqat yeysiz?>>>")
#if ovqat.lower() not in menu:
#    print("Afsuski bizda bunday ovqat yo'q")
#else:
#    print("Buyurtma qabul qilindi.")

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#buyurtmalar = ['osh','somsa','manti','shashlik']
#if buyurtmalar:
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f"Menuda {taom} bor")
#        else:
#            print(f"Kechirasiz, menuda {taom} yoq")
#else:
#    print("Savatchangiz bo'sh")
    
#Amaliyot
#Task№1
#juftSon = int(input("Juft son kiriting: "))
#if juftSon % 2:
#    print("Bu son juft emas.")
#else:
#    print("Rahmat!")
    
#№2
#yosh = int(input("Yoshingiz nechida?>>>"))
#if yosh <= 4 or yosh >= 65:
#    narh = 0
#elif yosh < 18:
#    narh = 10000
#elif yosh > 18:
#    narh = 20000
#print(f"Chipta narxi {narh} so'm")
    
#birinchi_son = float(input("Birinchi sonni kiriting: "))
#ikkinchi_son = float(input("Ikkinchi sonni kiriting: "))
#if birinchi_son < ikkinchi_son:
#    print(f"{birinchi_son} < {ikkinchi_son}")
#elif birinchi_son == ikkinchi_son:
#    print(f"{birinchi_son} = {ikkinchi_son}")
#else:
#    print(f"{birinchi_son} > {ikkinchi_son}")

#Task№3
#mahsulotlar = ['olma','anor','uzum','banan','anjir','shaftoli','pomidor','bodring','mandarin','xurmo','nok','ananas','qulpinay','kivi']
#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
       
#for meva in savat:
#        if meva in mahsulotlar:
#            print(f"Do'konimizda {meva} bor")
#        else:
#            print(f"Do'konimizda {meva} yo'q")

#Task №4
#mahsulotlar = ['un','olma','anor','uzum','banan','anjir','shaftoli','pomidor','bodring','mandarin','xurmo','nok','ananas','qulpinay','kivi']
#bor_mahsulotlar = []
#avjud_emas = []
#for n in range(5):
#    mahsulot = input(f"Savatga {n+1}-mahsulotni qoshing: ")
#    if mahsulot in mahsulotlar:
#        bor_mahsulotlar.append(mahsulot)
#    if mahsulot not in mahsulotlar:
#        mavjud_emas.append(mahsulot)
#if mavjud_emas:
#    print("Do'konimizda quyidagi mahsulotlar yo'q: ")
#    for mahsulot in mavjud_emas:
#        print(mahsulot)
#else:
#    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
#Task №5
#foydalanuvchilar = ['ali','vali','usmon','umar','hasan','husan']
#login = input("Yangi login tanlang: ")
#if login in foydalanuvchilar:
#    print("Login band, yangi login tanlang!")
#else:
#    print(f"Xush kelibsiz {login.title()} !")
    
  #Task №6
random = int(input("Istalgan butun son kiriting: "))
for n in range(2,11):
    if not (random%n):
        print(f"{random} soni {n} ga qoldiqsiz bo'linadi")
        
  
    
    
    
    
    
    
    
    
    
    
    
    

