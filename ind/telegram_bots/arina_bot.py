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


d_checker = False
d_cnt = 0
 

def dialogQ1(msg):
    markup = types.ReplyKeyboardMarkup()
    item1=types.KeyboardButton("answer Q1_1")
    item2=types.KeyboardButton("answer Q1_2")
    markup.add(item1, item2)
    MypyBot.send_message(msg.chat.id,'Question 1',reply_markup=markup)


def dialogQ2(msg):
    markup = types.ReplyKeyboardMarkup()
    item1=types.KeyboardButton("answer Q2_1")
    item2=types.KeyboardButton("answer Q2_2")
    markup.add(item1, item2)
    MypyBot.send_message(msg.chat.id,'Question 2',reply_markup=markup)


@MypyBot.message_handler(commands=['dialog'])
def dialog(message):
    global d_checker
    global d_cnt
    d_checker = True
    d_cnt += 1
    dialogQ1(message)


@MypyBot.message_handler(content_types = ['text'])
def replyer(message):
    global d_checker
    global d_cnt

    if d_checker:
        if d_cnt == 1:
            dialogQ2(message)
            d_cnt += 1
        elif d_cnt == 2:
            d_checker = False
            d_cnt = 0
        else:
            pass

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
            if d_checker == False:
                MypyBot.reply_to(message, message.text)    
    

MypyBot.polling()