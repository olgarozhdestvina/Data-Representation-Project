import mysql.connector
import dbconfig as cfg
db = mysql.connector.connect(
    host=cfg.mysql["host"],
    user=cfg.mysql["user"],
    password=cfg.mysql["password"],
    database=cfg.mysql["database"]
)

cursor = db.cursor()
sql = "CREATE TABLE dentists (dentistId INT AUTO_INCREMENT PRIMARY KEY, dentistName VARCHAR(255), position VARCHAR(255), regNumber  VARCHAR(255))"
cursor.execute(sql)