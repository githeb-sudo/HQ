CREATE USER DoceboDeveloper;
alter user 'DoceboDeveloper'@'%'  identified by 'password1234';
GRANT ALL PRIVILEGES ON *.* TO 'DoceboDeveloper'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
SELECT user FROM mysql.user;