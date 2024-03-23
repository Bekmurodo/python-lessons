# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:33:04 2024

@author: Suhrob
"""
import unittest
from practice import katta_son, bigFirstWord, juftson

talabalar = ['ali', 'vali', 'hasan', 'husan']
raqamlar = [12,45,81,27,347,76,90,45,24,10,54,67]


class Test_practice(unittest.TestCase):
 
    def test_kattaSon(self):
        self.assertEqual(katta_son(4,8,1), 8)
        self.assertEqual(katta_son(43,21,39), 43)
        self.assertEqual(katta_son(43,21,389), 389)
        
        
    def test_bigWord(self):
        self.assertEqual(bigFirstWord(talabalar), ['Ali', 'Vali', 'Hasan', 'Husan'])
    
    def test_evenNum(self):
        self.assertEqual(juftson(raqamlar), [12, 76, 90, 24, 10, 54])
    
unittest.main()