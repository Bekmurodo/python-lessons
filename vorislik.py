# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:40:18 2024

@author: Suhrob
Theme: Vorislik va polimorfizm
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

    

class Talaba(Shaxs):
    """Talaba klassi"""
    talabalar_soni = 0
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
        Talaba.talabalar_soni += 1
        
    @classmethod
    def num_students(cls):
        return cls.talabalar_soni
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    
user1 = Shaxs("Rahmon", 'Nurmatov', 403245678, 2003)
user2 = Shaxs("Suhrob", "Bekmurodov", 403625888, 2002)

class Manzil:
    """Manzil saqlash uchun klass"""

    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil


talaba1_manzil = Manzil(12, "Olmazor", "Bog'bon", "Samarqand")
talaba1 = Talaba("Valijon", "Aliyev", "FA112299", 2000, "0000012", talaba1_manzil)

#Amaliyot
class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil,yonalish,malaka):
        super().__init__(ism, familiya, passport, tyil)
        self.yonalish = yonalish
        self.malaka = 30
        
    def get_info(self):
        return f"Professor {self.ism} {self.familiya} {self.tyil} yilda tugulgan.\
            {self.yonalish} fanlari doktori, {self.malaka} yillik malakaga ega."
            
            
inson1 = Professor('Faxriddin', "Olimov", 403625888, 1976, "tibbiyot",30)        
            
class Foydalanuvchi(Shaxs):   
    def __init__(self, ism, familiya, passport, tyil,porol,email):
        super().__init__(ism, familiya, passport, tyil)
        self.porol = porol
        self.email = email
        
    def get_email(self):
        return self.email
        
    def get_info(self):
        return f"Foydalanuvchi {self.familiya} {self.ism} sizning emailingiz shumi {self.email} tasdiqlang."
 
user1 = Foydalanuvchi("Suhrob", "Bekmurodov", 403625888, 2002, "farukh2002", "zsuhrob240@gmail.com")        
        
class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, passport, tyil, porol, email,vakolat):
        super().__init__(ism, familiya, passport, tyil, porol, email)
        self.vakolat = vakolat
        
    def ban_user(self):
        return f"Foydalanuvchi {self.ism} bloklandi"
    
class Vakolat:
    def __init__(self,rutba):
        self.rutba = rutba
vakolati = Vakolat("General polkovnik")    
user2 = Admin("Suhrob", "Bekmurodov", 403625888, 2002, '5-854938549', "suhrob2312", vakolati)

        
        
        
        
        
        
        
        
        
        