-- Write a script that creates the database hbtn_0d_2 and the user user_0d_2

CREATE USER IF NOT EXISTS hbtn_0d_2;

-- Write a script that creates the MySQL server user user_0d_2

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Write a script that gives the user user_0d_2 read privilege

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';