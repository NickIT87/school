from telebot import types

from helpers import *
from settings import legend, ROOT_ID
from db_methods import save_data, get_data


#--------------------#
# COMMAND FUNCTIONS  #
#--------------------#

@MypyBot.message_handler(commands=['start', 'help'])
def start_message(message):
    MypyBot.send_message(message.chat.id, legend, reply_markup=types.ReplyKeyboardRemove())


@MypyBot.message_handler(commands=['links'])
def button_message(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(
        "Відгуки",
        url='https://www.instagram.com/s/aGlnaGxpZ2h0OjE3OTIyMTAyMzk4MzExODAx?igshid=YmMyMTA2M2Y='
    )
    item2 = types.InlineKeyboardButton(
        "Ukrainian collection",
        url='https://www.instagram.com/s/aGlnaGxpZ2h0OjE3OTA5OTc3ODYyMzkxNTk1?igshid=YmMyMTA2M2Y='
    )
    markup.add(item1, item2)
    MypyBot.send_message(
        message.chat.id, 'Актуальні новини магазину: ', reply_markup=markup)


@MypyBot.message_handler(commands=['catalog'])
def show_catalog(message):
    
    # functionality in progress ...
    
    markup = types.InlineKeyboardMarkup()
    btn_link1 = types.InlineKeyboardButton(
        "...",
        url='https://...'
    )
    btn_link2 = types.InlineKeyboardButton(
        "...",
        url='https://...'
    )
    markup.add(btn_link1, btn_link2)
    MypyBot.send_message(message.chat.id, 'Каталог: ', reply_markup=markup)


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


@MypyBot.message_handler(commands=['by'])
def by_item(message):
    if str(message.chat.id) not in users:
        users[str(message.chat.id)] = {
            'd_checker': False,
            'd_cnt': 0,
            'order_status': False,
            'order_values': dict(('q' + str(i), False) for i in range(1, len(q_base)+1))
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