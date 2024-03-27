# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:36:46 2024
@author: Suhrob
"""
import unittest
from car import Car


class CarTest(unittest.TestCase):
    def setUp(self):
        make = 'GM'
        model = 'Malibu'
        year = 2020
        self.price = 40000
        self.km = 10000
        self.avto1 = Car(make, model, year)
        self.avto2 = Car(make, model, year, price=self.price)
        
    def test_create(self):
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)

        self.assertIsNone(self.avto1.price)

        self.assertEqual(0, self.avto1.get_km())
        
        self.assertEqual(self.price, self.avto2.price)
        
    
    def test_set_price(self,price):
        self.price = price
        
    def add_km(self,km):
        if km >= 0:
            self.__km += km
        else:
            raise ValueError("km manfiy bo'lishi mumkun emas")

    def test_set_price(self):
        new_price = 45000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price, self.avto2.price)
        
    def test_add_km(self):
        self.avto1.add_km(self.km)
        self.assertEqual(self.km, self.avto1.get_km())
        
        new_km = -5000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)
        
    def test_get_info(self):
        avto1_info = "GM Malibu, 2020-yil, 0km yurgan."
        self.assertEqual(avto1_info, self.avto1.get_info())
        
        self.avto1.set_price(50000)
        self.avto1.add_km(10000)
        avto1_info = "GM Malibu, 2020-yil, 10000km yurgan. Narhi: 50000"
        self.assertEqual(avto1_info, self.avto1.get_info())

        
    
    
unittest.main()