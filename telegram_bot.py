# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 18:52:32 2024

@author: Suhrob
Theme: Telegram bot
"""
from transliterate import to_cyrillic, to_latin
import telebot

bot = telebot.TeleBot("7162492776:AAGMlFiNmyZKZBkn3_Xdu9DeZmnBjPEqY74")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalom alaykum, Xush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.infinity_polling()




#matn = input("Matn kiriting:")
#if matn.isascii():
#    print(to_cyrillic(matn))
#else:
#    print(to_latin(matn))