use dentalclinic;

CREATE TABLE dentist (
    dentistId int AUTO_INCREMENT PRIMARY KEY,
    dentistName varchar(255) NOT NULL CHECK (dentistName <> ''),
    position varchar(255),
    regNumber  varchar(255) CHECK (([regNumber]<>N'')),
    UNIQUE KEY unique_regNumber (regNumber)
    );

CREATE TABLE patient (
    patientId int AUTO_INCREMENT PRIMARY KEY,
    patientName varchar(255) NOT NULL CHECK (patientName <> ''),
    phone int,
    dentistId int NOT NULL,
    FOREIGN KEY (dentistId) REFERENCES dentist(dentistId)
    );
