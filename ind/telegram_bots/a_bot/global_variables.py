import telebot

# need change to dynamic path 
GLOBAL_PATH = '/home/nick/programming/school/ind/telegram_bots/a_bot/'

with open(
    GLOBAL_PATH + 'mytoken.txt', 
    'r'
) as ftoken:
    mytoken = ftoken.read()

# export:
MypyBot = telebot.TeleBot(token=mytoken, parse_mode = None)
users = dict()