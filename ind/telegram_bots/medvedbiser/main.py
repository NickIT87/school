from telebot import types

from settings import MypyBot, users, legend


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


#--------------------#
#  HELPER FUNCTIONS  #
#--------------------#

def extract_arg(arg) -> list:
    return arg.split()[1:]


#--------------------#
# REPLYER FUNCTIONS  #
#--------------------#

@MypyBot.message_handler(content_types = ['text'])
def replyer(message):
   print(message.text)


#--------------------#
#     ENTRY POINT    #
#--------------------#

if __name__ == "__main__":
    MypyBot.polling()