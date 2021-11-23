CREATE USER new;
alter user 'new'@'%'  identified by 'Password1234';
GRANT ALL PRIVILEGES ON *.* TO 'new'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
SELECT user FROM mysql.user;