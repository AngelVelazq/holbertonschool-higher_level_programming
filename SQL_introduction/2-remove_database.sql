-- This SQL script retrieves the IDs and names of the first 3 students in Batch ID=3.
-- This is done because Batch 3 is considered the best!
SELECT id, name
FROM students
WHERE batch_id = 3
ORDER BY created_at DESC
LIMIT 3;

