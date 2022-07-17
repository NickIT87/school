from telebot.types import InlineKeyboardButton

from settings import MypyBot, users, q_base, items_base, NUM_BTNS


#--------------------#
#  HELPER FUNCTIONS  #
#--------------------#
def get_catalog_btns():
    all_btns = []
    for key in items_base:
        btn = InlineKeyboardButton(
            items_base[key]['title'] + " (" + items_base[key]['price'] + " UAH)",
            url=items_base[key]['link']
        )
        all_btns.append(btn)
    
    # btns = np.array_split()

    return all_btns


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
