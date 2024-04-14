# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:55:22 2024

@author: Suhrob
"""
import requests 
from pprint import pprint

#sahifa = "https://kun.uz/news/main"
#r = requests.get(sahifa)
#pprint(r.text)

#restcountries API
country = "Tajikistan"
url = f"https://restcountries.eu/rest/v2/name/{country}"
r = requests.get(url)
r_json = r.json()[0]
#print(r_json.keys())
#print(r_json["capital"])
