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
        f'CREATE TABLE IF NOT EXISTS {table_name}( title TEXT, size TEXT, amount TEXT, phone TEXT, destination TEXT, name TEXT, payment TEXT, datestamp TEXT, unix TEXT )'
    )
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute(
        f"INSERT INTO {table_name} (title, size, amount, phone, destination, name, payment, datestamp, unix) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
        (
            users[u_id]['order']['q1'], 
            users[u_id]['order']['q2'], 
            users[u_id]['order']['q3'], 
            users[u_id]['order']['q4'],
            users[u_id]['order']['q5'],
            users[u_id]['order']['q6'],
            users[u_id]['order']['q7'],
            date, unix
        )
    )
    connection.commit()
    c.close()
    connection.close()


def get_data(user_name_id):
    connection = sqlite3.connect(GLOBAL_PATH + 'mb_data.db')
    c = connection.cursor()
    c.execute(f"SELECT * FROM {user_name_id}")
    data = c.fetchall()
    print(data)
    c.close()
    connection.close()
    return f"Заказ {user_name_id}, {data}"
