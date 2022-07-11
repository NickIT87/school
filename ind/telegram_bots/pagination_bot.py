import json
import os
import telebot;
from telebot.types import  ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


GLOBAL_PATH = os.path.abspath(__file__).replace(os.path.basename(__file__), '')

with open(GLOBAL_PATH + 'mytoken.txt', 'r') as ftoken:
    mytoken = ftoken.read()

bot = telebot.TeleBot(mytoken)

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    req = call.data.split('_')
		#Обработка кнопки - скрыть
    if req[0] == 'unseen':
        bot.delete_message(call.message.chat.id, call.message.message_id)
    #Обработка кнопок - вперед и назад
    elif 'pagination' in req[0]:
      	#Расспарсим полученный JSON
        json_string = json.loads(req[0])
        count = json_string['CountPage']
        page = json_string['NumberPage']
				#Пересоздаем markup
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
        
        #markup для первой страницы
        if page == 1:

            ########## MINE ###############
            btn_link1 = InlineKeyboardButton(
                "1",
                url='https://google.com'
            )
            btn_link2 = InlineKeyboardButton(
                "2",
                url='https://google.com'
            )
            markup.add(btn_link1, btn_link2)
            ########## MINE ###############

            markup.add(
                InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                InlineKeyboardButton(
                    text=f'Вперёд --->',
                    callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                        page + 1
                    ) + ",\"CountPage\":" + str(count) + "}"
                )
            )
        #markup для второй страницы
        elif page == count:

            ########## MINE ###############
            btn_link1 = InlineKeyboardButton(
                "1",
                url='https://google.com'
            )
            btn_link2 = InlineKeyboardButton(
                "2",
                url='https://google.com'
            )
            markup.add(btn_link1, btn_link2)
            ########## MINE ###############

            markup.add(
                InlineKeyboardButton(
                    text=f'<--- Назад',
                    callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                        page - 1
                    ) + ",\"CountPage\":" + str(count) + "}"),
                InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' ')
            )
        #markup для остальных страниц
        else:

            ########## MINE ###############
            btn_link1 = InlineKeyboardButton(
                "1",
                url='https://google.com'
            )
            btn_link2 = InlineKeyboardButton(
                "2",
                url='https://google.com'
            )
            markup.add(btn_link1, btn_link2)
            ########## MINE ###############

            markup.add(
                InlineKeyboardButton(text=f'<--- Назад', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page-1) + ",\"CountPage\":" + str(count) + "}"),
                InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                InlineKeyboardButton(text=f'Вперёд --->', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page+1) + ",\"CountPage\":" + str(count) + "}")
            )
        bot.edit_message_text(f'Страница {page} из {count}', reply_markup = markup, chat_id=call.message.chat.id, message_id=call.message.message_id)


@bot.message_handler(content_types=['text'])
def start(m):
    count = 10
    page = 1
    markup = InlineKeyboardMarkup()

    ########## MINE ###############
    btn_link1 = InlineKeyboardButton(
        "1",
        url='https://google.com'
    )
    btn_link2 = InlineKeyboardButton(
        "2",
        url='https://google.com'
    )
    markup.add(btn_link1, btn_link2)
    ########## MINE ###############

    markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
    markup.add(
        InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
        InlineKeyboardButton(
            text=f'Вперёд --->', 
            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                page+1
            ) + ",\"CountPage\":" + str(count) + "}"
        )
    )

    bot.send_message(m.from_user.id, "Привет!!!", reply_markup = markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)