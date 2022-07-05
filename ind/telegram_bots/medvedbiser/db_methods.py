import sqlite3
import time
import datetime

from settings import users, GLOBAL_PATH


def save_data(message):
    u_name = message.from_user.first_name + '_' + message.from_user.last_name
    u_id = str(message.chat.id)
    table_name = u_name + '_' + u_id
    connection = sqlite3.connect(GLOBAL_PATH + 'mb_data.db')
    c = connection.cursor()
    c.execute(
        f'CREATE TABLE IF NOT EXISTS {table_name}(ansver TEXT, datestamp TEXT)'
    )
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute(
        f"INSERT INTO {table_name} (ansver, datestamp) VALUES (?, ?)", 
        (message.text, date)
    )
    connection.commit()
    c.close()
    connection.close()


def get_data(u_id):
    return f"Заказ {u_id} "



# def save_result(message):
#     connection = sqlite3.connect(GLOBAL_PATH + 'a_bot.db')
#     c = connection.cursor()
#     c.execute(f'CREATE TABLE IF NOT EXISTS results(user TEXT, result TEXT)')
#     c.execute(
#         f"INSERT INTO results(user, result) VALUES (?, ?)", 
#         (str(message.from_user.first_name), users[str(message.chat.id)]['result'])
#     )
#     connection.commit()
#     c.close()
#     connection.close()