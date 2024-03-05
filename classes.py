# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 21:09:07 2024

@author: Suhrob
Theme: Classes
"""
class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        
    def get_name(self):
        return self.ism
    
    def get_lastname(self):
        return self.familiya
    
    def get_age(self,yil):
        return yil - self.tyil
        
    def tanishtir(self):
        return f"Ismim {self.ism} {self.familiya}, tug'ulgan yilim {self.tyil}"
        
        
talaba1 = Talaba("Suhrob", "Bekmurodov", 2002)

#Topshiriq
#№1
class User:
    def __init__(self,name, lastname,login,email,number):
        self.name = name
        self.lastname = lastname
        self.login = login 
        self.email = email
        self.number = number
        
    def get_fullname(self):
        return self.lastname
    
    def get_phoneNumber(self):
        return self.number
    
    def get_email(self):
        return self.email
         
    def get_info(self):
        return f"Foydalanuvchi: {self.name}, ismi:{self.lastname}, email:{self.email}"

user1 = User("Farukh2002", "Bekmurodov Suhrob", "farukhjon0902", "zsuhrob240@gmail.com", +79771825747)
