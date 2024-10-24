-- Script to create user 'user_0d_1' and grant all privileges

-- Create the user 'user_0d_1' if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on the server to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Reload privilege tables to apply changes
FLUSH PRIVILEGES;
