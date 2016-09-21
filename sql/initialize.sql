-- create user and database for dev-env
create user 'lolhfdev'@'localhost' identified by 'lolhfdev';
create database lolhfdev;
grant all on lolhfdev.* to 'lolhfdev'@'localhost';

-- create user and database for test-env
create user 'lolhftest'@'localhost' identified by 'lolhftest';
create database lolhftest;
grant all on lolhftest.* to 'lolhftest'@'localhost';	