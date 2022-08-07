import numpy as np
from telebot.types import InlineKeyboardButton
import telebot
from math import ceil
import os
import json


GLOBAL_PATH = os.path.abspath(__file__).replace(os.path.basename(__file__), '')
ROOT_ID = 655481481 #5085189951


with open(GLOBAL_PATH + 'qbase.json', encoding='utf-8') as json_file1:
    q_base = json.load(json_file1)

with open(GLOBAL_PATH + 'token.txt', 'r') as ftoken:
    mytoken = ftoken.read()


MypyBot = telebot.TeleBot(token=mytoken, parse_mode = "HTML")
users: dict = dict()  # user session data


# open catalog json
with open(GLOBAL_PATH + 'items.json', encoding='utf-8') as json_file2:
    items_base = json.load(json_file2)

# number of buttons per catalog page
MAX_BTNS: int = 10
COUNT_PAGES: int = ceil( len(items_base) / MAX_BTNS )

def __get_list_catalog_btns():
    all_btns, btns = [], []

    for key in items_base:
        btn = InlineKeyboardButton(
            items_base[key]['title'] + " (" + items_base[key]['price'] + " UAH)",
            url=items_base[key]['link']
        )
        all_btns.append(btn)
    
    if len(all_btns) > 0:
        all_btns.reverse()
        np_btns = np.array_split(np.array(all_btns), COUNT_PAGES)
        for i in np_btns:
            btns.append(list(i))
    
    return btns

# export list of buttons for pagination
BTNS_LIST: list = __get_list_catalog_btns()


# Templates
legend = """
Доброго дня, Вас вітає інтернет магазин прикрас: 
<b>Medved_biser.ua</b>
https://www.instagram.com/medved_biser.ua/

Подивитись посилання на актуальні новини нашого магазину:
/links

Подивитись каталог товарів у вигляді окремих посилань:
/catalog

Для замовлення товару використовуйте команду:
/buy
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