import mysql.connector
import dbconfig as cfg

class DentistDAO:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host =      cfg.mysql['host'],
            user =      cfg.mysql['user'],
            password =  cfg.mysql['password'],
            database =  cfg.mysql['database']
        )
    
    # create a dentist
    def create(self, values):
        cursor = self.db.cursor()
        sql = "INSERT INTO dentists (dentistName, position, regNumber) values (%s, %s, %s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    # get all dentists
    def get_all(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM dentists"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        # print(results)
        for result in results:
            result_as_dict = self.convert_to_dict(result)
            returnArray.append(result_as_dict)
        
        return returnArray

    def find_by_dentistId(self, dentistId):
        cursor = self.db.cursor()
        sql = "SELECT * FROM dentists WHERE dentistId = %s"
        values = (dentistId,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convert_to_dict(result)


    def update(self, values):
        cursor = self.db.cursor()
        sql = "UPDATE dentists SET dentistName = %s, position = %s, regNumber = %s WHERE dentistId = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, dentistId):
        cursor = self.db.cursor()
        sql = "DELETE FROM dentists WHERE dentistId = %s"
        values = (dentistId,)
        cursor.execute(sql, values)
        self.db.commit()
        print("Delete done")


    # convert tuples to dictionary objects
    def convert_to_dict(self, result):
        colnames = ['dentistId', 'dentistName','position','regNumber']
        dentist = {}

        if result:
            for i, colname in enumerate(colnames):
                value = result[i]
                dentist[colname] = value
        return dentist

dentistDAO = DentistDAO()