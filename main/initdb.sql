/* MySQL instructions to create database dentalclinic with two tables dentist and patient. */

/* 1. Create a database. */
CREATE DATABASE dentalclinic;

/* 2. Select it. */
use dentalclinic;

/* 3. Create dentist table. */
CREATE TABLE dentist (
    dentistId int AUTO_INCREMENT PRIMARY KEY,
    dentistName varchar(255) NOT NULL CHECK (dentistName <> ''),
    position varchar(255),
    regNumber  varchar(255) CHECK (regNumber<>'')),
    UNIQUE KEY unique_regNumber (regNumber)
    );

/* 4. Create patient table. */
CREATE TABLE patient (
    patientId int AUTO_INCREMENT PRIMARY KEY,
    patientName varchar(255) NOT NULL CHECK (patientName <> ''),
    phone int,
    dentistId int NOT NULL,
    FOREIGN KEY (dentistId) REFERENCES dentist(dentistId)
    );
