# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:20:45 2024

@author: Suhrob
"""
import random
n=100
numbers = list(range(1,n+1))
x = numbers.pop(random.randint(1, n+1))
print(x)

summa = n*(n+1)/2
print(summa - sum(numbers))
