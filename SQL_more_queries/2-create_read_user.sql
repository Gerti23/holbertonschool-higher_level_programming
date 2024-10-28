-- Write a script that creates the database hbtn_0d_2 and the user user_0d_2

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE USER IF NOT EXISTS hbtn_0d_2;

-- List privileges for user_0d_2

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';