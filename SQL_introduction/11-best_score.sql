-- Script to list records with score >= 10 from the table second_table
-- Displaying score and name, ordered by score in descending order

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

