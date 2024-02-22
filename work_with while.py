# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 18:25:10 2024

@author: Suhrob
Theme: Work with while list
"""
#print("Yaqin do'stlaringizning ro'yxatini tuzamiz.")
#ismlar = []
#n=1
#while True:
#    savol = f"{n}-do'stingizni kiriting:"
#    ism = input(savol)
#    ismlar.append(ism)
#    takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#    n+=1
#    if takrorlash != 'ha':
#        break
#print("Do'stlaringiz ro'yxati:")
#for ism in ismlar:
#    print(ism.title())


#print("Do'stlaringiz yoshini saqlaymiz.")
#dostlar = {}
#ishora = True
#while ishora:
#    ism = input("Do'stingizni ismini kiriting: ")
#    yosh = int(input(f"{ism.title()}ning yoshini kiriting: "))
#    dostlar[ism] = int(yosh)
#    
#    javob = input("Yana ma'lumot qoshasizmi? (ha/yo'q)")
#    if javob == "yo'q":
#        ishora = False
#for ism, yosh in dostlar.items():
#    print(f"{ism.title()} {yosh} yoshda.")
    
    
#cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
#car = 'nexia'
#while car in cars: # toki nexia cars ro'yxati ichida ekan...
#    cars.remove(car) # nexia ni ro'yxatdan olib tashla
#print(cars)

#talabalar = ['hasan', 'husan', 'olim','botir']
#baholangan_talabalar = {}
#while talabalar:
#    talaba = talabalar.pop()
#    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#    print(f"{talaba.title()} baholandi")
#    baholangan_talabalar[talaba] = int(baho)
#for ism, baho in baholangan_talabalar.items():
#    print(f"{ism.title()} {baho} baho oldi.")


#Amaliyot
#print("Oshxonamizga xush kelibsiz, nima buyurtma berasiz? ")
#royxat = []
#n=1
#while True:
#    savol = f"{n}-buyurtmangiz? "
#    mahsulot = input(savol)
#    royxat.append(mahsulot)
#    takrorlash = input("Ya buyurtma berasizmi? (ha/yo'q')")
#    n+=1
#    if takrorlash != 'ha':
#        break
#print("Buyurtmangiz:")
#for narsa in royxat:
#    print(narsa)
    
#Task 2
#print("Bozorimizda qanaqa mahsulot bolishini istaysiz? ")
#bozor = {'kartoshka': 3000, 'piyoz': 2000, 'pomidor': 10000, 'bodring': 7000}
#ishora = True
#while ishora:
#    mahsulot = input("mahsulot nomini kiriting? ")
#    narx = input(f"{mahsulot} narxini kiriting? ")
#    takrorlash = input("Yana mahsulot qoshasizmi? (ha/yo'q)")
#    bozor[mahsulot] = int(narx)
#    if takrorlash != 'ha':
#        ishora = False
        
#for mahsulot, narx in bozor.items():
#    print(f"{mahsulot.title()} - {narx} so'm")
    
#print("Do'konimizga xush kelibsiz, nima buyurtma berasiz? ")
#royxat = []
#n=1
#while True:
#    savol = f"{n}-buyurtmangiz? "
#    mahsulot = input(savol)
#    royxat.append(mahsulot)
#    takrorlash = input("Yana buyurtma berasizmi? (ha/yo'q')")
#    n+=1
#    if takrorlash != 'ha':
#        break
#print("Buyurtmangiz:")
#for narsa in royxat:
#    print(narsa)  
 
   
bozor = {'kartoshka': 3000, 'piyoz': 2000, 'pomidor': 10000, 'bodring': 7000, 'olma': 13000, 'anor': 20000}

print("Do'konimizga xush kelibsiz, nima buyurtma berasiz? ")
royxat = []
n=1
while True:
    savol = f"{n}-buyurtmangiz? "
    mahsulot = input(savol)
    royxat.append(mahsulot)
    takrorlash = input("Yana buyurtma berasizmi? (ha/yo'q')")
    n+=1
    if takrorlash != 'ha':
        break
#print("Buyurtmangiz:")
#for narsa in royxat:
#    print(narsa)

for tovar in royxat:
    if tovar in bozor:
        print(f"{tovar} {bozor[tovar]} so'm")
    else:
        print(f"Bizda {tovar} yo'q")
        






