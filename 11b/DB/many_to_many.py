import sqlite3

conn = sqlite3.connect('example2.db')
cursor = conn.cursor()

# Create the 'users' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL
    )
''')

# Create the 'products' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL
    )
''')

# Create the 'user_products' junction table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_products (
        user_id INTEGER,
        product_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (user_id),
        FOREIGN KEY (product_id) REFERENCES products (product_id)
    )
''')

# Insert some sample data
cursor.execute("INSERT INTO users (username) VALUES ('Alice')")
cursor.execute("INSERT INTO users (username) VALUES ('Bob')")
cursor.execute("INSERT INTO products (product_name) VALUES ('Product 1')")
cursor.execute("INSERT INTO products (product_name) VALUES ('Product 2')")
cursor.execute("INSERT INTO user_products (user_id, product_id) VALUES (1, 1)")
cursor.execute("INSERT INTO user_products (user_id, product_id) VALUES (1, 2)")
cursor.execute("INSERT INTO user_products (user_id, product_id) VALUES (2, 1)")

conn.commit()
conn.close()
