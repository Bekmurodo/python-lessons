# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:22:12 2024

@author: Suhrob
Theme: Dunder methods
"""

class Avto:
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil 
        self.narh  = narh
        Avto.__num_avto += 1
        

    def __repr__(self):
        return f"Avto: {self.make} {self.model}"

    def __eq__(self,y):
        return self.narh == y.narh
        
    def __lt__(self,y):
        return self.narh < y.narh
    
    def __le__(self,y):
        return self.narh <= y.narh
    
    
class AvtoSalon:
    """Avtosalon klassi"""

    def __init__(self, name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,qiymat):
        self.avtolar[index] = qiymat
    
    def __len__(self):
        return len(self.avtolar)
    
    def __call__(self,*qiymat):
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]
    
    def __add__(self,y):
        if isinstance(y, AvtoSalon):
            yangi_salon = AvtoSalon(f"{self.name} {y.name}")
            yangi_salon.avtolar = self.avtolar + y.avtolar
            return yangi_salon
        elif isinstance(y, Avto):
            self.add_avto(y)
            
    def add_avto(self,*qiymat):
        for car in qiymat:
            if isinstance(car,Avto):
                self.avtolar.append(car)
            else:
                print("Avto klasiga tegishli avto kiriting!")
   
    
salon1 = AvtoSalon("MaxAvto")
salon2 = AvtoSalon("Avto Lider")   
    
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)
avto3 = Avto("Toyota", "Corolla", "Silver", 2019, 18000)
salon1.add_avto(avto1,avto2,avto3)

avto4 = Avto("Mazda", "6", "Qizil", 2015, 30000)
avto5 = Avto("Volkswagen", "Polo", "Qora", 2015, 30000)
avto6 = Avto("Honda", "Accord", "Oq", 2017, 40000)
salon2(avto4,avto5,avto6)


