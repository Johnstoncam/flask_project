DROP TABLE IF EXISTS budgets;
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

CREATE TABLE budgets (
    id SERIAL PRIMARY KEY,
    value FLOAT(2),
    name VARCHAR(255)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    merchant_id SERIAL REFERENCES merchants(id),
    tag_id SERIAL REFERENCES tags(id),
    value FLOAT(2),
    budget_id integer NOT NULL REFERENCES budgets(id)
);

