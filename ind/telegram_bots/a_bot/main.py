from telebot import types

from settings import MypyBot, users, q_base, FILE_UPLOAD_PATH
from db_methods import *


#--------------------#
# COMMAND FUNCTIONS  #
#--------------------#

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
        reply_markup=types.ReplyKeyboardRemove()    # убираем клавиатуру если была
    )

# отладочная функция для отслеживания пользователей
@MypyBot.message_handler(commands=['users'])
def show_users(message):
    msg = ''
    if not users:
        MypyBot.send_message(message.chat.id, 'no one')
    else:
        print(len(users), users)
        for user in users:
            msg += str(user) + ' '
        MypyBot.send_message(message.chat.id, msg)


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
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    item1=types.KeyboardButton("Pepperoni")
    item2=types.KeyboardButton("Mushrooms")
    item3=types.KeyboardButton("Margarita")
    item4=types.KeyboardButton("With Pinneapples")
    item5=types.KeyboardButton("Ranger")
    item6=types.KeyboardButton("Maritime")
    markup.add(item1, item2, item3, item4, item5, item6)
    MypyBot.send_message(message.chat.id,'Какую пиццу предпочитаете?',reply_markup=markup)


@MypyBot.message_handler(commands=['dialog'])
def dialog(message):
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


#--------------------#
#  HELPER FUNCTIONS  #
#--------------------#

def dialogQuestion(msg):
    m = []      # markup objects
    scnt = 'q' + str(users[str(msg.chat.id)]['d_cnt'])      # q1 q8 
    q = q_base[scnt]['text']        # текст вопроса
    markup = types.ReplyKeyboardMarkup()
    for i in range(1, len(q_base[scnt])):
        item = types.KeyboardButton(q_base[scnt][str(i)]['text'])
        m.append(item)
    for i in m:
        markup.add(i)
    MypyBot.send_message(msg.chat.id, q, reply_markup=markup)


def check_result(message):
    if users[str(message.chat.id)]['d_cnt'] > 1:
        scnt = 'q' + str(users[str(message.chat.id)]['d_cnt'] - 1)
        for i in range(1, len(q_base[scnt])):
            if message.text in q_base[scnt][str(i)].values():
                a = list(q_base[scnt][str(i)].values())
                if a[1]:
                    users[str(message.chat.id)]['result'] += 1


#--------------------#
# REPLYER FUNCTIONS  #
#--------------------#

@MypyBot.message_handler(content_types = ['text'])
def replyer(message):
    if users:
        if users[str(message.chat.id)]['d_checker']:
            save_data(message)           # сохранение ответов
            check_result(message)        # проверка ответа
            if users[str(message.chat.id)]['d_cnt'] <= len(q_base):
                dialogQuestion(message)         # задать вопрос
                users[str(message.chat.id)]['d_cnt'] += 1
            else:
                users[str(message.chat.id)]['d_checker'] = False
                users[str(message.chat.id)]['d_cnt'] = 0
                save_result(message)
                MypyBot.send_message(
                    message.chat.id,
                    users[str(message.chat.id)]['result']
                )

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


@MypyBot.message_handler(content_types = ['sticker', 'photo'])
def content_replyer(message):
    if message.content_type == 'photo':
        raw = message.photo[2].file_id
        name = raw+".jpg"
        file_info = MypyBot.get_file(raw)
        downloaded_file = MypyBot.download_file(file_info.file_path)
        with open(FILE_UPLOAD_PATH + name,'wb') as new_file:
            new_file.write(downloaded_file)
        img = open(FILE_UPLOAD_PATH + name, 'rb')
        MypyBot.send_message(
            message.chat.id,
            "Запрос от\n*{name} {last}*".format(name=message.chat.first_name, last=message.chat.last_name),
            parse_mode="Markdown"
        ) #от кого идет сообщение и его содержание
        MypyBot.send_photo(message.chat.id, img)
        MypyBot.send_message(
            message.chat.id, 
            "*{name}!*\n\nСпасибо за инфу".format(
                name=message.chat.first_name, 
                last=message.chat.last_name, 
                text=message.text
            ), 
            parse_mode="Markdown"
        ) #то что пойдет юзеру после отправки сообщения


#--------------------#
#     ENTRY POINT    #
#--------------------#

if __name__ == "__main__":
    MypyBot.polling()