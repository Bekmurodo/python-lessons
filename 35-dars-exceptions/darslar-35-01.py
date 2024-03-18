# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:53:17 2024

@author: Suhrob
Theme: Xatolar bilan ishlash
"""

yosh = input("Yoshingizni kiriting: ")

try:
    yosh = int(yosh)
except ValueError:
    print("Siz butun son kiritmadingiz, butun son kiriting")
else:
    print(f"Siz {2024-yosh} yilda tug'ilgansiz")


while True:
    age = input("Yoshingizni kiriting: ")
    if age.isdigit():
        age = int
    
print("Salom Dunyo!")
