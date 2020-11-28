import mysql.connector
import dbconfig as cfg

class DentistDAO:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host =      cfg.mysql['host'],
            user =      cfg.mysql['user'],
            password =  cfg.mysql['password'],
            database =  "dentalclinic"
        )
    
    # create a dentist
    def create(self, values):
        cursor = self.db.cursor()
        sql = "INSERT INTO dentist (dentistName, position, regNumber) values (%s, %s, %s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    # get all dentists
    def get_all(self):
        cursor = self.db.cursor()
        sql="SELECT * FROM dentist"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convert_to_dict(result))

        return returnArray
  
    # get dentist by ID
    def find_by_dentistId(self, dentistId):
        cursor = self.db.cursor()
        sql = "SELECT * FROM dentist WHERE dentistId = %s"
        values = (dentistId,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convert_to_dict(result)


    def update(self, values):
        cursor = self.db.cursor()
        sql = "UPDATE dentist SET dentistName = %s, position = %s, regNumber = %s WHERE dentistId = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, dentistId):
        cursor = self.db.cursor()
        sql = "DELETE FROM dentist WHERE dentistId = %s"
        values = (dentistId,)
        cursor.execute(sql, values)
        self.db.commit()
        print("Delete done")


    # convert tuples to dictionary objects
    def convert_to_dict(self, result):
        colnames = ['dentistId', 'dentistName','position','regNumber']
        item = {}

        if result:
            for i, colname in enumerate(colnames):
                value = result[i]
                item[colname] = value
        return item

dentistDAO = DentistDAO()