import mysql.connector
import dbconfig as cfg

db = mysql.connector.connect(
    host=cfg.mysql["host"],
    user=cfg.mysql["user"],
    password=cfg.mysql["password"],
    database=cfg.mysql["database"]
)

cursor = db.cursor()
sql = "CREATE DATABASE dentalclinic"
cursor.execute(sql)