# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 18:50:25 2024

@author: user
"""

from OOP_inkapsulatsiya import Avto, Boat
avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)
avto3 = Avto("Toyota", "Corolla", "Silver", 2019, 18000)

print(Avto.get_num_avto())
