import json
from telebot.types import InlineKeyboardMarkup, \
    InlineKeyboardButton, ReplyKeyboardRemove

from helpers import *
from settings import legend, ROOT_ID, COUNT_PAGES, BTNS_LIST
from db_methods import save_data, get_data


#--------------------#
# CALLBACK FUNCTION  #
#--------------------#

@MypyBot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    req = call.data.split('_')
	    # Обработка кнопки - скрыть
    if req[0] == 'unseen':
        MypyBot.delete_message(call.message.chat.id, call.message.message_id)
        #Обработка кнопок - вперед и назад
    elif 'pagination' in req[0]:
      	    #Расспарсим полученный JSON
        json_string = json.loads(req[0])
        count = json_string['CountPage']
        page = json_string['NumberPage']
            #Пересоздаем markup
        markup = InlineKeyboardMarkup()
        
        for button in BTNS_LIST[page-1]:
            markup.add(button)
        markup.add(InlineKeyboardButton(text='Приховати', callback_data='unseen'))

        if page == 1:
            markup.add(
                InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                InlineKeyboardButton(text=f'Вперед --->', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page + 1) + ",\"CountPage\":" + str(count) + "}")
            )
        #markup для последней страницы
        elif page == count:
            markup.add(
                InlineKeyboardButton(text=f'<--- Назад', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page - 1) + ",\"CountPage\":" + str(count) + "}"),
                InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' ')
            )
        #markup для остальных страниц
        else:
            markup.add(
                InlineKeyboardButton(text=f'<--- Назад', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page-1) + ",\"CountPage\":" + str(count) + "}"),
                InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                InlineKeyboardButton(text=f'Вперед --->', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page+1) + ",\"CountPage\":" + str(count) + "}")
            )
        MypyBot.edit_message_text(f'Сторінка {page} з {count}', reply_markup = markup, chat_id=call.message.chat.id, message_id=call.message.message_id)


#--------------------#
# COMMAND FUNCTIONS  #
#--------------------#

@MypyBot.message_handler(commands=['start', 'help'])
def start_message(message):
    MypyBot.send_message(message.chat.id, legend, reply_markup=ReplyKeyboardRemove())


@MypyBot.message_handler(commands=['links'])
def button_message(message):
    markup = InlineKeyboardMarkup()
    item1 = InlineKeyboardButton(
        "Відгуки",
        url='https://www.instagram.com/s/aGlnaGxpZ2h0OjE3OTIyMTAyMzk4MzExODAx?igshid=YmMyMTA2M2Y='
    )
    item2 = InlineKeyboardButton(
        "Ukrainian collection",
        url='https://www.instagram.com/s/aGlnaGxpZ2h0OjE3OTA5OTc3ODYyMzkxNTk1?igshid=YmMyMTA2M2Y='
    )
    markup.add(item1, item2)
    MypyBot.send_message(
        message.chat.id, 'Актуальні новини магазину: ', reply_markup=markup)


@MypyBot.message_handler(commands=['catalog'])
def show_catalog(message):
    page = 1
    markup = InlineKeyboardMarkup()
    if len(BTNS_LIST) > 0:
        for button in BTNS_LIST[page-1]:
            markup.add(button)
        markup.add(InlineKeyboardButton(text='Приховати', callback_data='unseen'))
    else:
        return MypyBot.send_message(message.from_user.id, "Empty catalog!")
    if len(BTNS_LIST) > 1:
        markup.add(
            InlineKeyboardButton(text=f'{page}/{COUNT_PAGES}', callback_data=f' '),
            InlineKeyboardButton(
                text=f'Вперед --->', 
                callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page+1) + ",\"CountPage\":" + str(COUNT_PAGES) + "}"
            )
        )
    MypyBot.send_message(message.from_user.id, "Каталог: <b>Medved_biser.ua</b>", reply_markup = markup)


@MypyBot.message_handler(commands=['find'])
def find_item(message):
    status: list = extract_arg(message.text)
    print(status)


@MypyBot.message_handler(commands=['users'])
def show_users(message):
    msg = ''
    if not users:
        MypyBot.send_message(message.chat.id, 'no one')
    else:
        print(len(users), users)
        for user in users:
            msg += str(user)
            print(users[user]["d_checker"])
        MypyBot.send_message(message.chat.id, msg)


@MypyBot.message_handler(commands=['buy'])
def by_item(message):
    if str(message.chat.id) not in users:
        users[str(message.chat.id)] = {
            'd_checker': False,
            'd_cnt': 0,
            'order_status': False,
            'order_values': dict(('q' + str(i+1), False) for i in range(len(q_base)))
        }
    users[str(message.chat.id)]['d_checker'] = True
    MypyBot.send_message(
        message.chat.id,
        'Ви розпочали оформлення замовлення, для скасування введіть команду /cancel'
    )
    replyer(message)


@MypyBot.message_handler(commands=['cancel'])
def cancel_dialog(message):
    if not users:
        MypyBot.send_message(message.chat.id, 'without cancellation')
    else:
        clear_user(message.chat.id)
        MypyBot.send_message(message.chat.id, "Придбання товару відмінено!")


#--------------------#
# REPLYER FUNCTIONS  #
#--------------------#

@MypyBot.message_handler(content_types=['text'])
def replyer(message):
    if str(message.chat.id) in users:
        if users[str(message.chat.id)]['d_checker']:
            temp_save_ansvers(message)
            if users[str(message.chat.id)]['d_cnt'] < len(q_base):
                dialogQuestion(message)
                users[str(message.chat.id)]['d_cnt'] += 1
            else:
                save_data(message)
                MypyBot.send_message(ROOT_ID, get_data(message))
                clear_user(message.chat.id)
                MypyBot.send_message(
                    message.chat.id,
                    "Ваше замовлення передано в обробку, менеджер зв'яжеться з Вами для підтвердження замовлення. Дякуємо за співпрацю."
                )

#--------------------#
#     ENTRY POINT    #
#--------------------#

if __name__ == "__main__":
    MypyBot.polling()