-- creates the MySQL server user user_0d_1 and grant all priviledges
CREATE USER IF NOT EXISTS
user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRAND ALL PRIVILEGES ON * . *
TO user_0d_1@localhost;
