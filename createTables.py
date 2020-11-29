import mysql.connector
from mysql.connector.errors import Error
import dbconfig as cfg

db = mysql.connector.connect(
    host=cfg.mysql["host"],
    user=cfg.mysql["user"],
    password=cfg.mysql["password"],
    database=cfg.mysql["database"]
)

# Dentist Table
def create_dentist_table():
    try:
        cursor = db.cursor()
        sql = "CREATE TABLE dentist (dentistId int AUTO_INCREMENT PRIMARY KEY, dentistName varchar(255) NOT NULL CHECK (dentistName <> ''), position varchar(255), regNumber varchar(255), UNIQUE KEY unique_regNumber (regNumber))"
        cursor.execute(sql)
        print("Table DENTIST created.")
    except Error as err:
        print("Creation of dentist_table failed:", err)
        exit(1)

# Patient Table
def create_patient_table():
    try:
        cursor = db.cursor()
        sql = "CREATE TABLE patient (patientId int AUTO_INCREMENT PRIMARY KEY, patientName varchar(255) NOT NULL CHECK (patientName <> ''), phone int, dentistId int NULL, FOREIGN key (dentistId) REFERENCES dentist(dentistId))"
        cursor.execute(sql)
        print("Table PATIENT created.")
    except Error as err:
        print("Creation of patient_table failed:", err)
        exit(1)

create_dentist_table()
create_patient_table()