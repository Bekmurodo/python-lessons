# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 18:50:24 2024

@author: Suhrob
Theme: Functions
"""
def toliq_ism_yasa(ism, familiya):
    """Toliq isma qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz

talaba = toliq_ism_yasa('olim', 'kukiev')
#print(talaba.title())

def nom_nasab(ism, familiya, otasining_ismi=''):
    if otasining_ismi:
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()
        
talaba1 = nom_nasab('suhrob', 'bekmurodov', 'haydarqulovich')
#print(talaba1)

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
avtolar = [avto1, avto2]
#print('Onlayn bozordagi mavjud avtomashinalar:')
#for avto in avtolar:
#    if avto['narh']:
#        narh = avto['narh']
#    else:
#        narh = "Noma'lum"
#    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

def oraliq(min,max,qadam=''):
    sonlar=[]
    while min<max:
        if qadam:
            sonlar.append(min)
            min += int(qadam)
        else:
            sonlar.append(min)
            min += 1 
    return sonlar
        
#print(oraliq(0,31,3))

#print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
#while True:
#    print("\nQuyidagi ma'lumotlarni kiriting",end=' ')
#    kompaniya=input("\nIshlab chiqaruvchi: ")
#    model=input("Modeli: ")
##    rangi=input("Rangi: ")
 #   korobka=input("Korobka: ")
 #   yili=input("Ishlab chiqarilgan yili: ")
#    narhi=input("Narhi: ")
    
    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
#    javob = input("Yana avto qo'shasizmi? (yes/no): ")
#    if javob=='no':
#       break

#print("Sizning avtomobillaringiz: ")
#for avto in avtolar:
#    if avto['narh']:
#        narh = avto['narh']
#    else:
#        print("Noma'lum")
#    print(f"{avto['model'].title()} {avto['rang'].title()} {avto['yil']} {narh}")

#Amaliyot

def info_user(ismi,familiyasi,t_yili,t_joyi,telefoni,emaili='',joriy_yil=2024):
    user = {
        'ism':ismi,
        'familiya':familiyasi,
        't_joy':t_joyi,
        't_yil':t_yili,
        'joriy_yil':2024,
        'yosh':(joriy_yil-t_yili),
        'email':emaili,
        'tel':telefoni}
    return user

#print("Mijozlarimiz malumotlarini shakillantiramiz", end=' ')
#mijozlar = []
#while True:
#    ismi = input("\nIsmingiz: ")
#    familiyasi = input('Familiyangiz: ')
#    t_yili = int(input("Tug'ulgan yilingiz: "))
#    t_joyi = input("Tugulgan joyingiz: ")
#    emaili = input("Emailingiz: ")
#    telefoni = input("Telefonongiz: ")
#    
#    mijozlar.append(info_user(ismi, familiyasi, t_yili, t_joyi, telefoni))

#    javob = input("Yana ma'lumot qoshasizmi? (yes/no) ")
#    if javob == 'no':
#        break
    
#for mijoz in mijozlar:
#    print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()} {mijoz['yosh']}yoshda {mijoz['t_joy'].title()}dan telefon raqami: {mijoz['tel']}")
    
#Task 2
def bigger(x,y,z):
    if x > y and x > z:
        return x 
    if y > x and y > z:
        return y
    if z > x and z > y:
        return z
    
son = bigger(9, 6, 11)
#print(son)

#Task 3
def radius(son):
    aylana={
        'radius':son,
        'diametr':son*2,
        'perimetr':2*3.14*son,
        'yuzi':3.14*son**2}
    return aylana

son1 = radius(15)
#print(son1)

#Task 4
def tub_sonlar_top(min, max):
    tub_sonlar = []
    for n in range(min, max + 1):
        tub = True
        if n == 1:
            tub = False
        elif n == 2:
            tub = True
        else:
            for x in range(2, n):
                if n % x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar
print(tub_sonlar_top(2, 100))










