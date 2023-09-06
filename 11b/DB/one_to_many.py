import sqlite3

# Create a connection to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the 'users' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL
    )
''')

# Create the 'orders' table with a foreign key reference to 'users'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        order_description TEXT,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )
''')

# Insert some sample data
cursor.execute("INSERT INTO users (username) VALUES ('Alice')")
cursor.execute("INSERT INTO users (username) VALUES ('Bob')")
cursor.execute("INSERT INTO orders (user_id, order_description) VALUES (1, 'Order 1')")
cursor.execute("INSERT INTO orders (user_id, order_description) VALUES (1, 'Order 2')")
cursor.execute("INSERT INTO orders (user_id, order_description) VALUES (2, 'Order 3')")

# Commit the changes and close the connection
conn.commit()
conn.close()
