import telebot                  # pip install pyTelegramBotAPI
from telebot import types


with open(
    '/home/nick/programming/school/ind/telegram_bots/mytoken.txt', 
    'r'
) as ftoken:
    mytoken = ftoken.read()

MypyBot = telebot.TeleBot(token=mytoken, parse_mode = None)


@MypyBot.message_handler(commands=['start'])
def start_message(message):
    MypyBot.send_message(
        message.chat.id,
        """
            Привет ✌️, я персональный бот Арины!
            у меня есть команды:
            /links 
            /pizza_menu
        """
    )


@MypyBot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("btn1")
    item2=types.KeyboardButton("btn2")
    # markup=types.InlineKeyboardMarkup()
    # item1=types.InlineKeyboardButton("btn1", url='https://google.com')
    # item2=types.InlineKeyboardButton("btn2", url='https://youtube.com')
    markup.add(item1, item2)
    MypyBot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)


@MypyBot.message_handler(content_types = ['text'])
def replyer(message):
    if message.text == 'btn1':
        MypyBot.reply_to(message, "выбрана опция 1")
    elif message.text == 'btn2':\
        MypyBot.reply_to(message, "выбрана опция 2")
    else:
        MypyBot.reply_to(message, message.text)


MypyBot.polling()