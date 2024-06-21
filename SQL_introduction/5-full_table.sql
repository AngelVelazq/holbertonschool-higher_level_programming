-- Script to print the description of the table first_table from the specified database

SELECT 
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM 
    information_schema.COLUMNS
WHERE 
    TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'first_table';

