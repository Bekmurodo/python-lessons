# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:55:45 2024

@author: Suhrob
"""
import json

filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)
    
print(type(bemor))
