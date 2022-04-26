-- create tables for  merchants, tags and transactions
-- remember that names within this file should be plural 
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS tags;


CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    merchant_id SERIAL REFERENCES merchants(id),
    tag_id SERIAL REFERENCES tags(id),
    value FLOAT(2)
);

