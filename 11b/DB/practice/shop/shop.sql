DROP TABLE IF EXISTS products;

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    price FLOAT NOT NULL,
    discount FLOAT NOT NULL,
    product_description TEXT NOT NULL
);

INSERT INTO products (product_name, price, discount, product_description) VALUES (
    'Notebook Samsung A213', 234.45, 0.9, 'Fast gaming laptop'
);
INSERT INTO products (product_name, price, discount, product_description) VALUES (
    'Notebook Acer S456', 345.74, 0.5, 'Professional laptop for developers'
);

-- sqlite3 shop.db < shop.sql
-- SELECT product_name, ROUND(price * discount, 2) AS discounted_price FROM products;
-- SELECT product_name, ROUND(price * discount, 2) AS discounted_price FROM products WHERE product_id == 1;
