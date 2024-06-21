-- Attempt to drop the database hbtn_0c_0 if it exists
DROP DATABASE IF EXISTS hbtn_0c_0;

-- Check if the database was dropped successfully
-- This block will attempt to create a dummy table in the hbtn_0c_0 database.
-- If it succeeds, it means the database wasn't dropped, and an error is raised.
-- If it fails (due to the database not existing), it means the database was successfully dropped.
DO $$
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLSTATE '42S02' BEGIN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Database hbtn_0c_0 dropped successfully';
    END;
    
    USE hbtn_0c_0;
    CREATE TEMPORARY TABLE test_drop (id INT);
END $$;

