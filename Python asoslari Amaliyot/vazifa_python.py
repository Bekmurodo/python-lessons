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



#Convert_add = lambda string_list: sum([int(item[::-1]) for item in string_list])

#x = ['1','3','55']
#print(Convert_add(x))

class Person:
    def __init__(self, first_name, last_name, age, email, birth_day):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self._birth_day = birth_day
        
    @property
    def birth_day(self):
        return self._birth_day
        
    def get_info(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nAge: {self.age}\nEmail: {self.email}\nBirth Day: {self.birth_day}"
      
  
def get_life_path_number(birth_date):
    day, month, year = map(int, birth_date.split('-'))
    
    total_sum = sum(map(int, str(day))) + sum(map(int, str(month))) + sum(map(int, str(year)))
    
    life_path_number = total_sum
    while life_path_number >= 10:
        life_path_number = sum(map(int, str(life_path_number)))
    
    return life_path_number


def get_info_by_number(number):
    try:
        with open('malumotlar.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == number:
                    return {'number': data[0], 'name': data[1], 'age': data[2]}  # ko'rsatiladigan ma'lumotlar
        return 'Ma\'lumot topilmadi'
    except FileNotFoundError:
        return 'Fayl topilmadi'


birth_date = "27-09-2002"
life_path_number = get_life_path_number(birth_date)
#print("Life Path Number:", life_path_number)


odam = Person("Suhrob", "Bekmurodov", 21, 'zsuhrob240@gmail.com', (27, 9, 2002))