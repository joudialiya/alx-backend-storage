# THIS SQL SCRIPT CREATES USER TABLE IN HELBERTON DATABASE
# create databse
CREATE DATABASE IF NOT EXISTS holberton;
# use that database
USE holberton;
# dropt table is exists
DROP TABLE users;
# create the users table
CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255)
);
