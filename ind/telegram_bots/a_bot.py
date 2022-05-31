import telebot                  # pip install pyTelegramBotAPI
from telebot import types
import sqlite3


with open(
    '/home/nick/programming/school/ind/telegram_bots/mytoken.txt', 
    'r'
) as ftoken:
    mytoken = ftoken.read()

MypyBot = telebot.TeleBot(token=mytoken, parse_mode = None)


#users = []
d_checker = False
d_cnt = 0


@MypyBot.message_handler(commands=['start'])
def start_message(message):
    MypyBot.send_message(
        message.chat.id,
        """
            Привет ✌️, я персональный бот Арины!
            у меня есть команды:
            /links 
            /pizza_menu
            /dialog
        """,
        reply_markup=types.ReplyKeyboardRemove()
    )


@MypyBot.message_handler(commands=['links'])
def button_message(message):
    markup=types.InlineKeyboardMarkup()
    item1=types.InlineKeyboardButton(
        "Акинатор", 
        url='https://ru.akinator.com'
    )
    item2=types.InlineKeyboardButton(
        "YouTube", 
        url='https://youtube.com'
    )
    item3=types.InlineKeyboardButton(
        "Author`s github", 
        url='https://github.com/medvedarina12/My_bot_arina'
    )
    markup.add(item1, item2, item3)
    MypyBot.send_message(message.chat.id,'Мои ссылки:',reply_markup=markup)


@MypyBot.message_handler(commands=['pizza_menu'])
def button_pmenu(message):
    markup = types.ReplyKeyboardMarkup()
    item1=types.KeyboardButton("Pepperoni")
    item2=types.KeyboardButton("Mushrooms")
    item3=types.KeyboardButton("Margarita")
    item4=types.KeyboardButton("With Pinneapples")
    item5=types.KeyboardButton("Ranger")
    item6=types.KeyboardButton("Maritime")
    markup.add(item1, item2, item3, item4, item5, item6)
    MypyBot.send_message(message.chat.id,'Какую пиццу предпочитаете?',reply_markup=markup)


def dialogQ1(msg):
    q = 'Question 1'
    markup = types.ReplyKeyboardMarkup()
    item1=types.KeyboardButton("answer Q1_1")
    item2=types.KeyboardButton("answer Q1_2")
    markup.add(item1, item2)
    MypyBot.send_message(msg.chat.id, q, reply_markup=markup)
    return q

def dialogQ2(msg):
    q = 'Question 2'
    markup = types.ReplyKeyboardMarkup()
    item1=types.KeyboardButton("answer Q2_1")
    item2=types.KeyboardButton("answer Q2_2")
    markup.add(item1, item2)
    MypyBot.send_message(msg.chat.id,q,reply_markup=markup)
    return q


@MypyBot.message_handler(commands=['dialog'])
def dialog(message):
    global d_checker
    global d_cnt
    d_checker = True
    d_cnt += 1
    MypyBot.send_message(message.chat.id,'Начало диалога')
    replyer(message)


def save_data(message):
    print(message.text)
    # print(message.from_user.first_name, message.from_user.last_name)
    # u_name = message.from_user.first_name + '_' + message.from_user.last_name
    # print(
    #     f'CREATE TABLE IF NOT EXISTS {u_name}(question TEXT, answer TEXT, datestamp TEXT)'
    # )
    # question
    # answer
    # datetamp
    # connection = sqlite3.connect('a_bot.db')
    # c.execute(f'CREATE TABLE IF NOT EXISTS {u_name}(question TEXT, answer TEXT, datestamp TEXT)')

    # c.execute(f"INSERT INTO {u_name} VALUES(1234, '2016-01-01', 'Python', 5)")
    # connection.commit()
    # c.close()
    # connection.close()



@MypyBot.message_handler(content_types = ['text'])
def replyer(message):
    global d_checker
    global d_cnt

    if d_checker:
        save_data(message)
        if d_cnt == 1:
            dialogQ1(message)
            d_cnt += 1
        elif d_cnt == 2:
            dialogQ2(message)
            d_cnt += 1
        else:
            d_checker = False
            d_cnt = 0


    match message.text:
        case "Pepperoni": 
            MypyBot.reply_to(message, "Хороший выбор")
        case "Mushrooms":
            MypyBot.reply_to(message, "ммм Вкусненько")
        case "Margarita":
            MypyBot.reply_to(message, "а эту я не люблю")
        case "With Pinneapples":
            MypyBot.reply_to(message, "Необычно")
        case "Ranger":
            MypyBot.reply_to(message, "любишь остренькое?")
        case "Maritime":
            MypyBot.reply_to(message, "Гурман?")
        case "😂":
            MypyBot.reply_to(message, "Эй не молчи!")
        case "АЛЕ!":
            MypyBot.reply_to(message, "НЕ ОРИ!")
        case _:
            if d_checker == False and d_cnt == 0:
                start_message(message)


MypyBot.polling()