import telebot
import os
import json


GLOBAL_PATH = os.path.abspath(__file__).replace(os.path.basename(__file__), '')
ROOT_ID = 655481481 #5085189951

# number of buttons per catalog page
NUM_BTNS = 10

with open(GLOBAL_PATH + 'token.txt', 'r') as ftoken:
    mytoken = ftoken.read()

with open(GLOBAL_PATH + 'qbase.json', encoding='utf-8') as json_file1:
    q_base = json.load(json_file1)

with open(GLOBAL_PATH + 'items.json', encoding='utf-8') as json_file2:
    items_base = json.load(json_file2)

MypyBot = telebot.TeleBot(token=mytoken, parse_mode = None)
users: dict = dict()  # user session data

legend = """
Доброго дня, Вас вітає інтернет магазин прикрас: Medved_biser.ua
https://www.instagram.com/medved_biser.ua/

Подивитись посилання на актуальні новини нашого магазину:
/links

Для замовлення товару використовуйте команду:
/by
"""

order_template = """
Заказ від: 
    {0} ;

Назва товару: 
    {1[0]} ;
    
Розмір: 
    {1[1]} ;
    
Кількість: 
    {1[2]} ;
    
Телефон: 
    {1[3]} ;
    
Адреса: 
    {1[4]} ;

ПІБ замовника: 
    {1[5]} ;

Оплата: 
    {1[6]} ;

Дата: 
    {1[7]} ;
"""