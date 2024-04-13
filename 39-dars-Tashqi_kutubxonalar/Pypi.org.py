# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:45:54 2024

@author: Suhrob
"""

from googletrans import Translator
tarjimon = Translator()

matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"

tarjima = tarjimon.translate(matn_uz)

#print(tarjima.origin)
#print(tarjima.text)
#print(tarjima.src)

tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
#print(tarjima_ru.text)

matn_en = 'London is the capital of Great Britain'
tarjima_en = tarjimon.translate(matn_en, dest='uz')
#print(tarjima_en.text)

msg = 'Tarjima uchun so\'z kiriting (chiqib ketish uchun "q" deb yozing): '
while True:
    text = input(msg)
    if text == "q":
        break
    else:
        tarjima = tarjimon.translate(text, src="en", dest="uz")
        print(tarjima.text)


