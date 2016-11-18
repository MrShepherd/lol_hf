-- create user and database for dev-env
CREATE USER 'lolhfdev'@'localhost';
  IDENTIFIED BY 'lolhfdev';
CREATE DATABASE lolhfdev;
GRANT ALL ON lolhfdev.* TO 'lolhfdev'@'localhost';

-- create user and database for test-env
CREATE USER 'lolhftest'@'localhost';
  IDENTIFIED BY 'lolhftest';
CREATE DATABASE lolhftest;
GRANT ALL ON lolhftest.* TO 'lolhftest'@'localhost';
