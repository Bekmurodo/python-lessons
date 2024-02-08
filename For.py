# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:12:41 2024

@author: Suhrob
Theme: For Loop
"""
#mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
#for mehmon in mehmonlar:
#    print("Salom", mehmon)
#    print("Xayr", mehmon)

#mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
#for mehmon in mehmonlar:
#    print(f"Hurmatli {mehmon}, sizni 20 Fevral kuni nahorga oshga taklif etamiz")
#    print("Hurmat bilan, Bekmurodovlar oulasi\n")
    
#sonlar = list(range(1,11))
#for son in sonlar:
#    print(f"{son} ning kvadrati {son**2} ga teng")
    
#sonlar = list(range(11))
#sonlar_kvadrati = []
#for son in sonlar:
#    sonlar_kvadrati.append(son**2)
    
#print(sonlar)
#print(sonlar_kvadrati)

#dostlar = []
#print("5 ta yaqin dostingiz kim?")
#for n in range(5):
#    dostlar.append(input(f"{n+1}-dostingizni kiriting>>>"))
#print(dostlar)


#Amaliyot
#kitoblar = ["Men", "Lol", "Sir","Baxtiyor oila", "Sen"]
#for kitob in kitoblar:
#    print(f"Men '{kitob}' kitobini oqimoqchiman")
#print("Kod 5 marta takrorlandi")

#for n in range(11,100,2):
#    print(f"{n**3}")

#kinolar = []
#print("O'zingiz sevgan 5 ta kino nomini kiriting")
#for n in range(5):
#    kinolar.append(input(f"{n+1}-kino nomini kiriting:"))
#print(f"Siz yoqtiradigan kinolar: {kinolar.title()}.")

odam_soni =int(input("Assalomu alaykum, bugun nechi odam bilan suhbatlashdingiz?>>>"))
suhbatdosh = []
for n in range(odam_soni):
    suhbatdosh.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))

print(suhbatdosh)






