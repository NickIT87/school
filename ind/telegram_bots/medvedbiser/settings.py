import telebot
import os
import json


GLOBAL_PATH = os.path.abspath(__file__).replace(os.path.basename(__file__), '')

with open(
    GLOBAL_PATH + 'token.txt', 
    'r'
) as ftoken:
    mytoken = ftoken.read()

# with open(GLOBAL_PATH + 'qbase.json', encoding='utf-8') as json_file:
#     q_base = json.load(json_file)

MypyBot = telebot.TeleBot(token=mytoken, parse_mode = None)
users: dict = dict()  # user session data