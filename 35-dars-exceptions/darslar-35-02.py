# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:26:43 2024

@author: Suhrob
"""
#ZeroDivisionErrorS
#x,y = 10,5
#try:
#    x/(y-5)
#except ZeroDivisionError:
#    print("0 ga bo'lish mumkun emas")
   
    
#IndexError
mevalar = ['olma','anor','anjir','uzum']
#try:
#    print(mevalar[5])
#except IndexError:
#    print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")
   
#keyError
user = {"username":"sariqdev",
        "status":"admin",
        "email":"admin@sariq.dev",
        "phone":"99897123456"}

#key="tel"
#try:
#    print(f'Foydalanuvchi: {user[key]}')
#except KeyError:
#    print("Bunday kalit mavjud emas")
    
#FileNotFoundError
filename = 'data.txt'
try:
    with open(filename) as f:
        text = f.read
except FileNotFoundError:
    print(f"{filename} nomli fayl mavjud emas")
    
    
#import json
#files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
#for filename in files:
#    try:
#        with open(filename) as f:
#            talaba = json.load(f)        
#    except FileNotFoundError:
#        print(f"{filename} mavjud emas")
#    else:
#        print(talaba['ism'])
        # fayl ustida turli amallar     

#n = input("Butun son kiriting: ")
#try:
#    n = int(n)
#    x=20/n
#except ValueError: # agar foydalanuvchi butun son kiritmasa
#    print("Butun son kiritmadingiz")
#except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
#    print("0 ga bo'lib bo'lmaydi")
#else:
#    print(f"x={x}")    
    
while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break        

print(f"Siz {2024-yosh} yilda tug'ilgansiz")  
    
    
    
    
    
    
    
    