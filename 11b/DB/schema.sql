-- sqlite3 schemaExample.db < schema.sql

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS orders;

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL
);

ALTER TABLE users 
ADD COLUMN fname TEXT NOT NULL;

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    order_description TEXT,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

INSERT INTO users (username, fname) VALUES ('Alice', 'Daniels');
INSERT INTO users (username, fname) VALUES ('Bob', 'Dunkerk');
INSERT INTO orders (user_id, order_description) VALUES (1, 'Order 1');