from telebot import types

from settings import MypyBot, users, legend, q_base


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
    markup=types.InlineKeyboardMarkup()
    item1=types.InlineKeyboardButton(
        "Відгуки", 
        url='https://www.instagram.com/s/aGlnaGxpZ2h0OjE3OTIyMTAyMzk4MzExODAx?igshid=YmMyMTA2M2Y='
    )
    item2=types.InlineKeyboardButton(
        "Ukrainian collection", 
        url='https://www.instagram.com/s/aGlnaGxpZ2h0OjE3OTA5OTc3ODYyMzkxNTk1?igshid=YmMyMTA2M2Y='
    )
    markup.add(item1, item2)
    MypyBot.send_message(message.chat.id,'Мои ссылки:',reply_markup=markup)




@MypyBot.message_handler(commands=['find'])
def yourCommand(message):
    status: list = extract_arg(message.text)
    print(status)


# отладочная функция для отслеживания пользователей
@MypyBot.message_handler(commands=['users'])
def show_users(message):
    msg = ''
    if not users:
        MypyBot.send_message(message.chat.id, 'no one')
    else:
        print(len(users), users)
        for user in users:
            msg += str(user) + ' '
        MypyBot.send_message(message.chat.id, msg)


@MypyBot.message_handler(commands=['by'])
def by_item(message):
    if str(message.chat.id) not in users:
        users[str(message.chat.id)] = {
            'd_checker': False,
            'd_cnt': 0,
        }
    users[str(message.chat.id)]['d_checker'] = True
    users[str(message.chat.id)]['d_cnt'] += 1
    MypyBot.send_message(
        message.chat.id,
        'Ви розпочали оформлення замовлення, для скасування введіть команду /cancel'
    )
    replyer(message)

#--------------------#
#  HELPER FUNCTIONS  #
#--------------------#

def extract_arg(arg) -> list:
    return arg.split()[1:]


def dialogQuestion(msg):
    qcnt = 'q' + str(users[str(msg.chat.id)]['d_cnt'])      # q1 q8 
    q = q_base[qcnt]
    MypyBot.send_message(
        msg.chat.id, 
        q, 
    )


#--------------------#
# REPLYER FUNCTIONS  #
#--------------------#

@MypyBot.message_handler(content_types = ['text'])
def replyer(message):
   if users:
        if users[str(message.chat.id)]['d_checker']:
            #save_data(message)           # сохранение ответов
            if users[str(message.chat.id)]['d_cnt'] <= len(q_base):
                dialogQuestion(message)         # задать вопрос
                users[str(message.chat.id)]['d_cnt'] += 1
            else:
                users[str(message.chat.id)]['d_checker'] = False
                users[str(message.chat.id)]['d_cnt'] = 0
                #save_result(message)
                MypyBot.send_message(
                    message.chat.id,
                    "Ваше замовлення передано в обробку, менеджер зв'яжеться з Вами для підтвердження замовлення. Дякуємо за співпрацю."
                )


#--------------------#
#     ENTRY POINT    #
#--------------------#

if __name__ == "__main__":
    MypyBot.polling()