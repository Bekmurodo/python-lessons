# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:59:21 2024

@author: user
"""
#import random

#def add_username():
#    username = input("Username kiriting: ")
#    reverse_username = username[::-1]
    
#    random_number = random.randint(0, 9)
#    new_username = reverse_username + str(random_number)
 
#    return f"Sizning uchun generatsiya qilingan username: {new_username.lower()}"

#print(add_username())



Convert_add = lambda string_list: sum([int(item[::-1]) for item in string_list])

x = ['1','3','55']
#print(Convert_add(x))




    def get_text_by_number(number):
        try:
            with open('Hayot_yoli.txt', 'r') as file:
                for line in file:
                    data = line.strip().split('#')
                    if data[0] == number:
                        return data[1]  # Matn qaytariladi (raqamni boshqa indeksda o'rnating kerak bo'ladi)
            return 'Matn topilmadi'
        except FileNotFoundError:
            return 'Fayl topilmadi'

# Faylni o'zgartiring 'Hayot_yoli.txt' deb va uni nomlaydigan raqam, matn qatorlari bo'lishi kerak



odam = Person("Suhrob", "Bekmurodov", 21, 'zsuhrob240@gmail.com', (27, 9, 2002))