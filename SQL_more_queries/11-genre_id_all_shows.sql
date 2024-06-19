-- Retrieve the first 3 students from Batch ID=3
SELECT id, name 
FROM students 
WHERE batch_id = 3 
ORDER BY created_at DESC 
LIMIT 3;
