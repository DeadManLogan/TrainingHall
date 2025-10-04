CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    genre VARCHAR(50),
    price NUMERIC(6,2) CHECK (price >= 0),
    -- author_id INT REFERENCES authors(author_id) ON DELETE CASCADE,
    stock_quantity INT DEFAULT 0
);
