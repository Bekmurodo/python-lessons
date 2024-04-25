# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:38:59 2024

@author: Suhrob
Theme: Classes and methods
"""
class Talaba:
    """Talaba nomli klass yaratamiz"""

    def __init__(self, ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def set_bosqich(self, yangi_bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = yangi_bosqich

    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1

    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya

    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"

    def get_age(self, yil):
        """Talabaning yoshini qaytaradi"""
        return yil - self.tyil
        
talaba1 = Talaba("Suhrob", "Bekmurodov", 2002)
talaba2 = Talaba("Olim", "Toirov", 2005)

class Fan:
    
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
        
    def add_student(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
        
    def get_name(self):
        return self.nomi
        
    def get_students(self):
        return [x.get_info() for x in self.talabalar]
      
    def get_students_num(self):
        return self.talabalar_soni
      
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith("__") is False]

        
matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon", "Valiyev", 2000)
talaba2 = Talaba("Hasan", "Alimov", 2001)
talaba3 = Talaba("Akrom", "Boriyev", 2001)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)    
     
matem = Fan("Oliy matematika")  
 
#Amaliyot
#1)

class Avto:
    def __init__(self,kompaniya,model,rang,yili,narh):
        self.kompaniya = kompaniya
        self.model = model
        self.rang = rang
        self.yili = yili
        self.narh = narh
        self.kilometr = 0
        
    def get_company(self):
        return self.kompaniya
    
    def get_model(self):
        return self.model
    
    def get_color(self):
        return self.rang
    
    def add_price(self,narx):
        self.narh += narx
        
    def update_km(self,new_km):
       self.kilometr += new_km
    
    def get_info(self):
        return f"{self.kompaniya} {self.model} {self.yili} yilda chiqqan, {self.rang.title()} rangda, narhi: {self.narh}$ { self.kilometr} km"


avto1 = Avto("Toyota", "Camry", 'oq', 2020, 40000)
avto2 = Avto("Mercedes-Benz", "GLS", "qora", 2022, 300000)

class Avtosalon:
    def __init__(self,salon_nomi,manzili):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.salondagi_avtolar = []
        self.avtolar_soni = 0
        
    def add_cars(self,car):
        self.salondagi_avtolar.append(car)
        self.avtolar_soni += 1
        
    def get_cars(self):
        return [car.get_info() for car in self.salondagi_avtolar]
    

cars = Avtosalon("Lazy cars", "Toshkent", )








