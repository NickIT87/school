from telebot import types

from settings import MypyBot, users, legend, q_base, ROOT_ID
from db_methods import save_data, get_data


#--------------------#
# COMMAND FUNCTIONS  #
#--------------------#

@MypyBot.message_handler(commands=['start', 'help'])
def start_message(message):
    MypyBot.send_message(
        message.chat.id,
        legend,
        reply_markup=types.ReplyKeyboardRemove()
    )


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
            'order_values': {
                'q1': False,
                'q2': False,
                'q3': False,
                'q4': False,
                'q5': False,
                'q6': False,
                'q7': False,
            }
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
#  HELPER FUNCTIONS  #
#--------------------#

def extract_arg(arg) -> list:
    return arg.split()[1:]


def dialogQuestion(msg):
    qcnt = 'q' + str(users[str(msg.chat.id)]['d_cnt'])
    MypyBot.send_message(msg.chat.id, q_base[qcnt])


def temp_save_ansvers(msg):
    if msg.text == '/by':
        users[str(msg.chat.id)]['order_status'] = True
    else:
        cnt = str(users[str(msg.chat.id)]['d_cnt'])
        users[str(msg.chat.id)]['order_values']['q' + cnt] = msg.text


def clear_user(id):
    users[str(id)]['d_checker'] = False
    users[str(id)]['d_cnt'] = 0
    users[str(id)]['order_status'] = False
    for key in users[str(id)]['order_values'].keys():
        users[str(id)]['order_values'][key] = False


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
                MypyBot.send_message(
                    ROOT_ID,
                    get_data(message)
                )
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