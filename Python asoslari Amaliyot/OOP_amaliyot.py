# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:12:49 2024

@author: Suhrob
"""

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
        result = ""
        with open("Hayot_yoli.txt", 'r') as file:
            found = False
            for line in file:
                line = line.strip()
                if line.startswith(f"#{number}"):
                    if found:
                        break
                    found = True
                elif found:
                    if line.startswith("#"):
                        break
                    result += line + "\n"
        return result




odam = Person("Suhrob", "Bekmurodov", 21, 'zsuhrob240@gmail.com', (27, 9, 2002))
#print(odam.get_info())
t_kun = "27-09-2002"
raqam = Person.get_life_path_number(t_kun)
info = odam.get_info_by_number(raqam)
print(info)