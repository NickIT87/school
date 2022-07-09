import telebot
import os
import json


GLOBAL_PATH = os.path.abspath(__file__).replace(os.path.basename(__file__), '')
ROOT_ID = 655481481 #5085189951 

with open(
    GLOBAL_PATH + 'token.txt', 
    'r'
) as ftoken:
    mytoken = ftoken.read()

with open(GLOBAL_PATH + 'qbase.json', encoding='utf-8') as json_file:
    q_base = json.load(json_file)

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
    {1} ;
    
Розмір: 
    {2} ;
    
Кількість: 
    {3} ;
    
Телефон: 
    {4} ;
    
Адреса: 
    {5} ;

ПІБ замовника: 
    {6} ;

Оплата: 
    {7} ;

Дата: 
    {8} ;
"""