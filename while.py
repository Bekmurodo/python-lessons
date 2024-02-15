# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:45:44 2024

@author: Suhrob
Theme: while
"""
#ism = input("Ismingiz nima? ")
#savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
#yosh = input(savol)
#yosh = int(yosh)
#height = input("Bo'yingiz nechi metr? ")
#height = float(height)

#son = 1
#while son<=5:
#    print(son, end=' ')
#    son += 1

#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni toxtatish uchun 'exit' dev yozing): "
#qiymat = ''
#while qiymat != 'exit':
#    qiymat = input(savol)
#   if qiymat != 'exit':
#        print(float(qiymat)**2)
#print("Dastur tugadi")


#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#avol = "Istalgan son kiriting "
#savol += "(dasturni toxtatish uchun 'exit' dev yozing): "
#ishora = True
#while ishora:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        ishora = False
#    else:
#        print(float(qiymat)**2)
#print('Dastur toxtadi!')

#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni toxtatish uchun 'exit' dev yozing): "

#while True:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        break
#    else:
#        print(float(qiymat)**2)
#print('Dastur toxtadi!')

#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 5:
#        continue
#    else:
#        print(f'{son} ning kvadrati {son**2} ga teng')

#son = 0
#while son<10:
#    son += 1
#    if son%2 != 0:
#        continue
#    else:
#        print(son)
 
#Infinite loop        
#son = 0
#while son<10:
#    son += 1
#    if son%2 != 0:
#        continue
#    else:
#        print(son)

#son = 1
#while son>0:
##    son += 1
#    if son%2 != 0:
#        continue
#    else:
#        print(son)
    
#Amaliyot
#kitob = "Yaxshi ko'rgan kitoblaringizni kiriting"
#kitob += " (dastur tugashi uchun 'stop' deb yozing): "

#while True:
#    a = input(kitob)
#    if a == 'stop':
#        break
#print("Rahmat!")


savol = "Yoshingiz nechida? "
savol += "Dastur to'xtashi uchun 'exit' yoki 'quit' deb yozing): "
 
while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)
    
    if yosh <= 7:
        narx = 2000
    if 18 >= yosh > 7:
        narx = 3000
    if 18 < yosh < 65:
        narx = 10000
    if yosh >= 65:
        narx = 0

    print(f"Chipta narxi {narx} so'm")
    
    
    




















