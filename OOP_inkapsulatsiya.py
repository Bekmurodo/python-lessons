# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 19:59:15 2024

@author: Suhrob
Theme:inkapsulyatsiya

"""
from uuid import uuid4
class Avto:
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil 
        self.narh  = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
        
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id

    def add_km(self,km):
        if km>=0:
            self.__km += km
        else:
            print("Mashina kilometrini kamaytirib bo'lmaydi")
            
avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)
avto3 = Avto("Toyota", "Corolla", "Silver", 2019, 18000)

print(Avto.get_num_avto())

class Boat:
    pass
 
class Bus: 
    pass


