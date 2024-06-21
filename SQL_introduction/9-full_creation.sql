-- Script to create the table second_table if it does not exist
-- and insert multiple rows into it

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT,
    PRIMARY KEY (id)
);

INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8)
ON DUPLICATE KEY UPDATE
    name = VALUES(name),
    score = VALUES(score);

