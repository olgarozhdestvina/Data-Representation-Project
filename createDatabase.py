# Create dentalclinic database

import mysql.connector
from mysql.connector.errors import Error
import dbconfig as cfg

# Connect to MySQL.
db = mysql.connector.connect(
    host=cfg.mysql["host"],
    user=cfg.mysql["user"],
    password=cfg.mysql["password"]
)

# Create a database.
def create_database():
    try:
        cursor = db.cursor()
        sql = "CREATE DATABASE dentalclinic"
        cursor.execute(sql)
        print("Database created.")
        cursor.close()
    except Error as err:
        print("Database creation failed:", err)
        exit(1)

# Call the function.
create_database()
