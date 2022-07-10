import sqlite3
import time
import datetime

from settings import users, GLOBAL_PATH, order_template


def save_data(message):  
    u_name = message.from_user.first_name + '_' + message.from_user.last_name
    u_id = str(message.chat.id)
    table_name = u_name + '_' + u_id
    connection = sqlite3.connect(GLOBAL_PATH + 'mb_data.db')
    c = connection.cursor()
    c.execute(
        f'CREATE TABLE IF NOT EXISTS {table_name}( title TEXT, size TEXT, amount TEXT, phone TEXT, destination TEXT, name TEXT, payment TEXT, datestamp TEXT, unix REAL )'
    )
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    data_val = list(users[u_id]['order_values'].values())
    data_val.extend([date, unix])
    c.execute(
        f"INSERT INTO {table_name} (title, size, amount, phone, destination, name, payment, datestamp, unix) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
        data_val
    )
    connection.commit()
    c.close()
    connection.close()


def get_data(message):
    user_name_id = message.from_user.first_name + '_' \
        + message.from_user.last_name + '_' + str(message.chat.id)
    connection = sqlite3.connect(GLOBAL_PATH + 'mb_data.db')
    c = connection.cursor()
    c.execute(f"SELECT * FROM {user_name_id}")
    data = c.fetchall()
    c.close()
    connection.close()
    return order_template.format(
        user_name_id, 
        data[-1]
    )
