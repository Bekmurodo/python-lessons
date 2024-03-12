# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:45:00 2024

@author: Suhrob
Theme: Dunder methods
"""
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __diplom = 1
    odamlar_soni = 0
    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        Shaxs.odamlar_soni +=1
        
    @classmethod
    def num_diploma(cls):
        return cls.__diplom

    def get_num_people(cls):
        return cls.odamlar_soni

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

    def __repr__(self):
        return f"Fuqoro {self.ism} {self.familiya}"
    
    def __lt__(self,y):
        return self.tyil > y.tyil
    
    

user1 = Shaxs("Rahmon", 'Nurmatov', 403245678, 2003)
user2 = Shaxs("Suhrob", "Bekmurodov", 403625888, 2002)
user3 = Shaxs("Kamol", "Davlatov", 403549217, 1997)


class Fan:
    def __init__(self,nomi):
        self.nomi = nomi
        self.fanga_yozilgan_talabalar = []
        
    def __repr__(self):
        return f' Fanga yozilgan talabalar: {self.fanga_yozilgan_talabalar}'
        
    


    def get_student(self):
        return self.fanga_yozilgan_talabalar
        
    def add_student(self,talaba):
        return self.fanga_yozilgan_talabalar.append(talaba)
        
    def __getitem__(self,index):
        return self.fanga_yozilgan_talabalar[index]
    
    def __setitem__(self,index,qiymat):
        self.fanga_yozilgan_talabalar[index] = qiymat
        
    def __len__(self):
        return len(self.fanga_yozilgan_talabalar)
    
    def __add__(self,x):
        return self.fanga_yozilgan_talabalar + x
talaba = Fan("Adabiyot")
talaba1 = "Ali"
talaba.add_student(talaba1)
talaba2 = 'Husan'