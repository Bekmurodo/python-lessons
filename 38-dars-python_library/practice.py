# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:31:17 2024

@author: Suhrob
"""
import datetime as dt #timedelta
import re
# # Amaliyot
#hozir = dt.now()
#now = hozir.date()

#for n in range(1,11):
#   yangi_kun = hozir + timedelta(weeks=n*2)
#    print(yangi_kun.strftime("%d-%m-%Y"))

# # 2
bugun = dt.date.today()
ramazon = dt.date(2024, 4, 10)
qurbon = dt.date(2024, 6, 16)
farq = ramazon - bugun
farq2 = qurbon - bugun

#print(f"Ramazon hayitiga {farq.days} kun qoldi.")
#print(f"Qurbon hayitiga {farq2.days} kun qoldi.")
 
# # 3
tugulgan_kunim = dt.datetime(2002, 9, 27, 12, 45,00)
hozirgi_vaqt = dt.datetime.now()
farqi = hozirgi_vaqt - tugulgan_kunim
soat = farqi.days * 24
minute = soat * 60
second = minute * 60
oy = int(farqi.days / 30)
yil = int(oy / 12)
yosh = f"Tug'ulganimga {yil} yil, {oy} oy, {farqi.days} kun {soat} soat {minute} daqiqa {second} soniya bo'libdi."
#print(yosh)

# # 4

msg = "Telefon raqamingizni kiriting: "

#while True:
#    raqam = input(msg)
#    andoza = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
#    if re.match(andoza, raqam):
#        print("Muvaffaqiyatli!")
#        break
#    else:
#        print("Qaerdadir xatolik bor yana urunib ko'ring \n ")
        
# # 5

matn = "Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI"
matn += "Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"

andozaa = "^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
link = re.findall(andozaa, matn)
print(link)









