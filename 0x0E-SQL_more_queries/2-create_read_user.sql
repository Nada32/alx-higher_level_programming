-- sql.
CREATE DATABASE hbtn_0d_2;
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT PRIVILEGE ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
GRANT SELECT TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
