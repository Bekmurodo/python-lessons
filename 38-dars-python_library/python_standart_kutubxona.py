# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 20:24:07 2024

@author: Suhrob
"""
import datetime as dt

# # # datetime
hozir = dt.datetime.now()
#print(hozir)
#print(hozir.date)
#print(hozir.time)
#print(hozir.hour)
#print(hozir.minute)
#print(hozir.second)

# # date()
#bugun = dt.date.today()
#print(f"Bugungi sana: {bugun}")
#ertaga = dt.date(2021,3,22)
#print(f"Ertagangi sana: {ertaga}")

# # time()
#hozir = dt.datetime.now()
#vaqtHozir = hozir.time()
#print(f"Hozir soat: {vaqtHozir}")
#vaqtKeyin = dt.time(23,45,55)
#print(vaqtKeyin)

# # sanalar orasidagi farq
#bugun = dt.date.today()
#ramazon = dt.date(2024, 4, 11)
#farq = ramazon - bugun
#print(farq)
#print(f"Ramazonga {farq.days} kun qoldi")

# # soatlar orasidagi farq
hozir = dt.datetime.now()
football = dt.datetime(2024, 3, 22, 23, 45, 00)
farq = football - hozir
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)

print(f"Futbol boshlanishiga {farq.days} kunu {soatlar }soat  qoldi")














