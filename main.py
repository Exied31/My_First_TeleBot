import telebot

bot = telebot.TeleBot("8005383006:AAH5pPQefWZbEf0SU7p1Ggmsn55sYXzC4DY")

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message,"Для начало выбери командой, что ты хочешь вывести")
    
@bot.message_handler(commands=["hello"])
def hello(message):
    bot.reply_to(message,"Привет, дорогой пользователь нашего бота")

@bot.message_handler(commands=["buy"])
def buy(message):
    bot.reply_to(message,"Чего желаете преобрести сэр?")

@bot.message_handler(commands=["info"])
def info(message):
    bot.reply_to(message,"/hello\n/start\n/buy")



bot.polling(none_stop=True)
