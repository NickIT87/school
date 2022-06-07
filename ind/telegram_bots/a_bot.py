import telebot                  # pip install pyTelegramBotAPI
from telebot import types
import sqlite3
import time
import datetime

from qbase import q_base


with open(
    '/home/nick/programming/school/ind/telegram_bots/mytoken.txt', 
    'r'
) as ftoken:
    mytoken = ftoken.read()

MypyBot = telebot.TeleBot(token=mytoken, parse_mode = None)

users = dict()


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
            /users
        """,
        reply_markup=types.ReplyKeyboardRemove()
    )


@MypyBot.message_handler(commands=['users'])
def show_users(message):
    global users
    if not users:
        MypyBot.send_message(message.chat.id, 'no one')
    else:
        MypyBot.send_message(message.chat.id, users)


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


def dialogQuestion(msg):
    global users
    m = []
    scnt = 'q' + str(users[str(msg.chat.id)]['d_cnt'])
    q = q_base[scnt]['text']
    markup = types.ReplyKeyboardMarkup()
    for i in range(1, len(q_base[scnt])):
        item = types.KeyboardButton(q_base[scnt][str(i)]['text'])
        m.append(item)
    for i in m:
        markup.add(i)
    MypyBot.send_message(msg.chat.id, q, reply_markup=markup)


@MypyBot.message_handler(commands=['dialog'])
def dialog(message):
    global users
    if str(message.chat.id) not in users:
        users[str(message.chat.id)] = {
            'd_checker': False,
            'd_cnt': 0,
            'result': None
        }
    users[str(message.chat.id)]['d_checker'] = True
    users[str(message.chat.id)]['d_cnt'] += 1
    users[str(message.chat.id)]['result'] = 0
    MypyBot.send_message(message.chat.id,'Начало диалога')
    replyer(message)


def save_data(message):
    u_name = message.from_user.first_name + '_' + message.from_user.last_name
    connection = sqlite3.connect('a_bot.db')
    c = connection.cursor()
    c.execute(f'CREATE TABLE IF NOT EXISTS {u_name}(ansver TEXT, datestamp TEXT)')
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute(f"INSERT INTO {u_name} (ansver, datestamp) VALUES (?, ?)", (message.text, date))
    connection.commit()
    c.close()
    connection.close()


def check_result(message):
    if users[str(message.chat.id)]['d_cnt'] > 1:
        scnt = 'q' + str(users[str(message.chat.id)]['d_cnt'] - 1)
        for i in range(1, len(q_base[scnt])):
            if message.text in q_base[scnt][str(i)].values():
                a = list(q_base[scnt][str(i)].values())
                if a[1]:
                    users[str(message.chat.id)]['result'] += 1


@MypyBot.message_handler(content_types = ['text'])
def replyer(message):
    global users
        
    if users:
        if users[str(message.chat.id)]['d_checker']:
            #save_data(message)          # сохранение ответов
            check_result(message)
            if users[str(message.chat.id)]['d_cnt'] <= len(q_base):
                dialogQuestion(message)
                users[str(message.chat.id)]['d_cnt'] += 1
            else:
                users[str(message.chat.id)]['d_checker'] = False
                users[str(message.chat.id)]['d_cnt'] = 0
                print(users[str(message.chat.id)]['result'])

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
            if users:
                if users[str(message.chat.id)]['d_checker'] == False \
                    and users[str(message.chat.id)]['d_cnt'] == 0:
                    start_message(message)
            else:
                start_message(message)


MypyBot.polling()