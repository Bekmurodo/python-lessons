# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 19:41:16 2024

@author: Suhrob

"""
import unittest
from shaxs import Shaxs, Talaba

class ShaxsTest(unittest.TestCase):
    def setUp(self):
        ism = "Suhrob"
        familiya = "Bekmurodov"
        passport = "403625888"
        tyil = 2002
        self.user1 = Shaxs(ism, familiya, passport, tyil)
        
    def test_info(self):
        user_info = 'Suhrob Bekmurodov. Passport:403625888, 2002-yilda tug`ilgan'
        self.assertEqual(user_info, self.user1.get_info())
        
    def test_age(self):
        self.assertEqual(22, self.user1.get_age(2024))
        
        
class TalabaTest(unittest.TestCase):
    def setUp(self):
        ism = "Suhrob"
        familiya = "Bekmurodov"
        passport = "403625888"
        tyil = 2002
        idraqam = "000021"
        self.talaba1 = Talaba(ism, familiya, passport, tyil, idraqam)

    def test_ID(self):
        self.assertEqual('000021', self.talaba1.get_id())
        
unittest.main()