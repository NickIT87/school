CREATE DATABASE IF NOT EXISTS `users`


    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL
    )

    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        order_description TEXT,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )