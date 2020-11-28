use dentalclinic;

CREATE TABLE dentist (
    dentistId int AUTO_INCREMENT PRIMARY KEY,
    dentistName varchar(255) NOT NULL,
    position varchar(255),
    regNumber  varchar(255),
    UNIQUE KEY unique_regNumber (regNumber)
    );