# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:02:47 2024

@author: user
"""

with open('codes.txt','a') as file:
     file.write("Suhrob Bekmurodov\n")
     file.write("2002")
    
with open('codes.txt') as file:
    codes = file.read()
 
#print(codes)


#with open("pi.txt") as file:
#    pi = file.read()
#print(pi)

#pi = pi.rstrip()
#pi = pi.replace('\n', '')
#pi = float(pi)
#print(pi)

with open('pi_million_digits.txt') as file:
    pi = file.read()
pi = pi.rstrip()
pi = pi.replace('\n','')
pi = pi.replace(' ','')

bdate = '27092002' 
print(bdate in pi)