-- This script creates a table called first_table with id and name columns
-- It won't fail if the table already exists

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
