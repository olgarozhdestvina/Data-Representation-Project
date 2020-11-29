import mysql.connector
from mysql.connector.errors import Error
import dbconfig as cfg

db = mysql.connector.connect(
    host=cfg.mysql["host"],
    user=cfg.mysql["user"],
    password=cfg.mysql["password"]
)

try:
    cursor = db.cursor()
    sql = "CREATE DATABASE dentalclinic"
    cursor.execute(sql)
    print("Database created.")
except Error as err:
        print("Database creation failed:", err)
        exit(1)
