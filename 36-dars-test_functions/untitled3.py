# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 19:41:41 2024

@author: user
"""
import unittest
from circle import getAria, getPerimeter

class CircleTest(unittest.TestCase):
    def test_aria(self):
        self.assertAlmostEqual(getAria(5), 78.53975)
        self.assertAlmostEqual(getAria(10), 314.159)
    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(10), 62.8318)
        self.assertAlmostEqual(getPerimeter(4), 25.13272)
        
unittest.main()