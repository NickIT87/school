import telebot
import os
import json


GLOBAL_PATH = os.path.abspath(__file__).replace(os.path.basename(__file__), '')

if not os.path.exists(GLOBAL_PATH + 'uploads'):
    os.mkdir(GLOBAL_PATH + 'uploads')

FILE_UPLOAD_PATH = GLOBAL_PATH + 'uploads/' 

with open(
    GLOBAL_PATH + 'token.txt', 
    'r'
) as ftoken:
    mytoken = ftoken.read()

with open(GLOBAL_PATH + 'qbase.json') as json_file:
    q_base = json.load(json_file)

MypyBot = telebot.TeleBot(token=mytoken, parse_mode = None)
users: dict = dict()  # user session data