-- This script lists all databases in the MySQL server
-- The output will be sorted alphabetically

SELECT SCHEMA_NAME AS 'Database'
FROM information_schema.SCHEMATA
ORDER BY SCHEMA_NAME;
