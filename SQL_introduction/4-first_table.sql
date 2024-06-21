-- Script to create a table called first_table in the specified database
-- The table will have columns id (INT) and name (VARCHAR(256))
-- If the table already exists, the script will not fail

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

