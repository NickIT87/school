CREATE TABLE IF NOT EXISTS historicalResources(
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    book_name TEXT NOT NULL,
    amount INTEGER NOT NULL,
    price TEXT NOT NULL
);