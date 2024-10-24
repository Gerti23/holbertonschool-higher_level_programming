-- This script prints the description of the table first_table
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, EXTRA
FROM information_schema.columns
WHERE table_name = 'first_table'
AND table_schema = DATABASE();
