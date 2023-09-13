DROP TABLE IF EXISTS stores_workers;

CREATE TABLE stores_workers (
    shop_id INTEGER PRIMARY KEY,
    shop_number INTEGER NOT NULL,
    adress TEXT NOT NULL,
    worker_name TEXT NOT NULL,
    position TEXT NOT NULL
);

INSERT INTO stores_workers (shop_number, adress, worker_name, position) VALUES (
    21, 'Parkova st. 21', 'Petro', 'Dispatcher'
)