import telebot
from telebot import types
import random

bot = telebot.TeleBot("6919449758:AAHR0O5dNPvQdsMRQ2-HRbcldhtCBIMO5uQ")

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Рандомное число"))
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)

@bot.message_handler(commands=["hello"])
def hello(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(commands=["random"])
def randomize(message):
    num = random.randint(1, 100)
    bot.send_message(message.chat.id, str(num))


bot.polling(none_stop=True)
