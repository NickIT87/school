import sqlite3

connection = sqlite3.connect('libFond.db')
c = connection.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS historicalResources(pk INTEGER PRIMARY KEY AUTOINCREMENT,book_name TEXT NOT NULL,amount INTEGER NOT NULL,price TEXT NOT NULL);")

def data_entry():
    c.execute(
        "INSERT INTO historicalResources (book_name, amount, price) VALUES (?, ?, ?)",
        ('Ilustrated history of Kyiv', 4, '250 USD'),
    )
    connection.commit()
    c.close()
    connection.close()


#create_table()
data_entry()