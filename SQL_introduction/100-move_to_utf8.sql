-- Convert database to UTF8MB4
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET = utf8 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET = utf8 COLLATE utf8mb4_unicode_ci;

