# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:13:50 2024

@author: Suhrob
Theme: Work with files
"""
#file = open("pi.txt")
#PI = file.read()
#print(PI)
#file.close()

#with open("pi.txt") as file:
#    pi = file.read()
#print(pi)

#pi = pi.rstrip()
#pi = pi.replace('\n', '')
#pi = float(pi)
#print(pi)

faylnomi = 'new_file.txt'
ism = 'Olimjon Hasanov'
tyil = 2004
with open(faylnomi,'w') as fayl:
    fayl.write(ism+'\n')
    fayl.write(str(tyil)+'\n')
    
with open(faylnomi,'a') as fayl:
    fayl.write('Alijon Valiev\n')
    fayl.write('2000')    
    

import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

with open('info','wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)
    
with open('info','rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)
    
#print(talaba1)
#print(talaba2)

with open('codes.txt') as file:
    codes = file.read()
    
#print(codes)

with open('codes.txt','a') as file:
    x = file.write("Suhrob Bekmurodov\n")
#    file.write("2002")
    
#Amaliyot

with open('pi_million_digits.txt') as file:
    pi = file.read()
pi = pi.rstrip()
pi = pi.replace('\n','')
pi = pi.replace(' ','')

bdate = '2002' 
#print(bdate in pi)

pi = float(pi)

#with open("amaliyot/pi_float.dat",'wb') as file:
#    pickle.dump(pi, file)
    
    
#while True:
#    book = input("Yaxshi ko'rgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
#    if not book:break
#    with open('books.txt','a') as file:
#        file.write(book+'\n')
        
with open('books.txt') as file:
    kitob = file.read()
    print(kitob)