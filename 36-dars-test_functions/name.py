# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:44:51 2024

@author: Suhrob
"""
def get_full_name(ism,familiya,otasi=''):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()
    else:
        return f"{ism} {familiya}".title()
