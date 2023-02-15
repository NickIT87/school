import sqlite3


connection = sqlite3.connect('libFond.db')
c = connection.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS historicalResources(pk INTEGER PRIMARY KEY AUTOINCREMENT,book_name TEXT NOT NULL,amount INTEGER NOT NULL,price TEXT NOT NULL);")


def data_entry(book_name: str, amount: int, price: str):
    c.execute(
        "INSERT INTO historicalResources (book_name, amount, price) VALUES (?, ?, ?)",
        (book_name, amount, price)
    )
    connection.commit()
    c.close()
    connection.close()


def read_from_db():
    c.execute("SELECT * FROM historicalResources WHERE pk == 2")
    
    for row in c.fetchall():
        print(row)


#create_table()
#data_entry("World history", 5, "285 UAH")
read_from_db()