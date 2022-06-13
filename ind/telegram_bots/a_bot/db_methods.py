import sqlite3
import time
import datetime

from global_variables import users, GLOBAL_PATH


def save_data(message):
    global users
    u_name = message.from_user.first_name + '_' + message.from_user.last_name
    connection = sqlite3.connect(GLOBAL_PATH + 'a_bot.db')            # подключиться к БД
    c = connection.cursor()                             # курсор по БД
    c.execute(f'CREATE TABLE IF NOT EXISTS {u_name}(ansver TEXT, datestamp TEXT, result TEXT)')
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute(
        f"INSERT INTO {u_name} (ansver, datestamp, result) VALUES (?, ?, ?)", 
        (message.text, date, users[str(message.chat.id)]['result'])
    )
    connection.commit()
    c.close()
    connection.close()


def save_result(message):
    global users
    connection = sqlite3.connect(GLOBAL_PATH + 'a_bot.db')            # подключиться к БД
    c = connection.cursor()                             # курсор по БД
    c.execute(f'CREATE TABLE IF NOT EXISTS results(user TEXT, result TEXT)')
    c.execute(
        f"INSERT INTO results(user, result) VALUES (?, ?)", 
        (str(message.from_user.first_name), users[str(message.chat.id)]['result'])
    )
    connection.commit()
    c.close()
    connection.close()