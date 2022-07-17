from settings import MypyBot, users, q_base


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
