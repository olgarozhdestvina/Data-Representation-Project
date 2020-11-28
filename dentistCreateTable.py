import mysql.connector
import dbconfig as cfg
db = mysql.connector.connect(
    host=cfg.mysql["host"],
    user=cfg.mysql["user"],
    password=cfg.mysql["password"],
    database=cfg.mysql["database"]
)

cursor = db.cursor()
sql = "CREATE TABLE dentist (dentistId int AUTO_INCREMENT PRIMARY KEY, dentistName varchar(255) NOT NULL, position varchar(255), regNumber varchar(255), UNIQUE KEY unique_regNumber (regNumber))"
cursor.execute(sql)