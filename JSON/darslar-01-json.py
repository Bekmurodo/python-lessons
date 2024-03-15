# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:09:58 2024

@author: Suhrob
Theme: JSON
"""

import json

x = 10
x_json = json.dumps(x)

y = 5.5
y_json = json.dumps(y)

m = True
m_json = json.dumps(m)

sonlar = (12, 45, 23, 67)
sonlar_json = json.dumps(sonlar)
 
with open('sonlar_json','w') as f:
     json.dump(sonlar,f)

bemor = {
  "ism": "Alijon Valiyev",
  "yosh": 30,
  "oila": True,
  "farzandlar": ("Ahmad","Bonu"),
  "allergiya": None,
  "dorilar": [
    {"nomi": "Analgin", "miqdori": 0.5},
    {"nomi": "Panadol", "miqdori": 1.2}
  ]
}

bemor_json = json.dumps(bemor)
#print(bemor_json)

bemor_json = json.dumps(bemor,indent=4)
#print(bemor_json)

with open('bemor.json','w') as f:
    json.dump(bemor,f)
    
bemor2 = json.loads(bemor_json)
print(bemor2)














