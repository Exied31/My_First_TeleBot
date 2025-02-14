import telebot
import random
import os

bot = telebot.TeleBot("8005383006:AAH5pPQefWZbEf0SU7p1Ggmsn55sYXzC4DY")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['animals'])
def send_mem(message):
    img_name = random.choice(os.listdir('animals'))
    with open(f'animals/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

bot.infinity_polling()  
