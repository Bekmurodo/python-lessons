# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:06:02 2024

@author: Suhrob
"""
import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data)
#print(data_json)

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba = json.loads(talaba_json)
#print(talaba)

with open('data_json', 'w') as f:
    json.dump(data,f)

with open('talaba_json','w') as f:
    json.dump(talaba,f)

#4
with open('students.json') as f:
    datas = json.load(f)
 

#for item in datas['student']:
#   print(f"{item['name']} {item['lastname']}." f" Faculty of {item['faculty']} ")

#5
with open('wikipedia.json') as f:
    wiki = json.load(f)
     
print(wiki['query']['pages']['13801']['title'])
print(wiki['query']['pages']['13801']['extract'])


