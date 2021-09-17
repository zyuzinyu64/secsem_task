CREATE DATABASE test_project

USE test_project

CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(50) NOT NULL,
    money_amount INT,
    card_number VARCHAR(50),
    status INT
);

INSERT INTO users VALUES (0, 'admin', 10000, '4916569371411116', 1);
INSERT INTO users VALUES (0, 'vasya', 100, '4556342226261697', 1);
INSERT INTO users VALUES (0, 'petya', 5000, '4716262440751041', 1);
INSERT INTO users VALUES (0, 'katya', 1000, '4397041529898592', 0);
INSERT INTO users VALUES (0, 'sofya', 250, '4539725763131863', 0);

CREATE TABLE passwords(
    id INT AUTO_INCREMENT PRIMARY KEY,
    password VARCHAR(50)
);

INSERT INTO passwors VALUES (0, '12345');
INSERT INTO passwors VALUES (0, '123456');
INSERT INTO passwors VALUES (0, '1234567');
INSERT INTO passwors VALUES (0, '12345678');
INSERT INTO passwors VALUES (0, '123456789');