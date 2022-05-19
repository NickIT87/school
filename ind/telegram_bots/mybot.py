import telebot
from telebot import types

mytoken = ''
MypyBot = telebot.TeleBot(token=mytoken, parse_mode = None)


@MypyBot.message_handler(commands=['start'])
def start_message(message):
    MypyBot.send_message(message.chat.id,"Привет ✌️ ")


@MypyBot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("btn1")
    markup.add(item1)
    MypyBot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)


@MypyBot.message_handler(content_types = ['text'])
def replyer(message):
    MypyBot.reply_to(message, message.text)


MypyBot.polling()