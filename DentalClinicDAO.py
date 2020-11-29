import mysql.connector
from mysql.connector.errors import Error
import dbconfig as cfg

class DentalClinicDAO:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host =      cfg.mysql['host'],
            user =      cfg.mysql['user'],
            password =  cfg.mysql['password'],
            database =  "dentalclinic"
        )
    
    # Create a dentist
    def create_dentist(self, values):
        try:
            cursor = self.db.cursor()
            sql = "INSERT INTO dentist (dentistName, position, regNumber) values (%s, %s, %s)"
            cursor.execute(sql, values)
            self.db.commit()
            return cursor.lastrowid
        except Error as err:
            print("Creation of a new dentist failed:", err)

    # Create a patient
    def create_patient(self, values):
        try:
            cursor = self.db.cursor()
            sql = "INSERT INTO patient (patientName, phone, dentistId) values (%s, %s, %s)"
            cursor.execute(sql, values)
            self.db.commit()
            return cursor.lastrowid
        except Error as err:
            print("Creation of a new patient failed:", err)

    # Get all dentists
    def get_all_dentists(self):
        try:
            cursor = self.db.cursor()
            sql="SELECT * FROM dentist"
            cursor.execute(sql)
            results = cursor.fetchall()
            returnArray = []
            for result in results:
                returnArray.append(self.convert_to_dict_dentist(result))
            return returnArray
        except Error as err:
            print("Error: ", err)

    # Get all patients
    def get_all_patients(self):
        try:
            cursor = self.db.cursor()
            sql="SELECT * FROM patient"
            cursor.execute(sql)
            results = cursor.fetchall()
            returnArray = []
            for result in results:
                returnArray.append(self.convert_to_dict_patient(result))
            return returnArray
        except Error as err:
            print("Error: ", err)
  
    # Get dentist by ID
    def find_by_dentistId(self, dentistId):
        try: 
            cursor = self.db.cursor()
            sql = "SELECT * FROM dentist WHERE dentistId = %s"
            values = (dentistId,)
            cursor.execute(sql, values)
            result = cursor.fetchone()
            return self.convert_to_dict_dentist(result)
        except Error as err:
            print(f"Dentist with id {dentistId} doesn't exist", err)

     # Get patient by ID
    def find_by_patientId(self, patientId):
        try:
            cursor = self.db.cursor()
            sql = "SELECT * FROM patient WHERE patientId = %s"
            values = (patientId,)
            cursor.execute(sql, values)
            result = cursor.fetchone()
            return self.convert_to_dict_patient(result)
        except Error as err:
            print(f"Patient with id {patientId} doesn't exist", err)

    # Update dentist.
    def update_dentist(self, values):
        try:
            cursor = self.db.cursor()
            sql = "UPDATE dentist SET dentistName = %s, position = %s, regNumber = %s WHERE dentistId = %s"
            cursor.execute(sql, values)
            self.db.commit()
        except Error as err:
            print("Creation of a new dentist failed: ", err)

    # Update patient.
    def update_patient(self, values):
        try: 
            cursor = self.db.cursor()
            sql = "UPDATE patient SET patientName = %s, phone = %s, dentistId= %s WHERE patientId = %s"
            cursor.execute(sql, values)
            self.db.commit()
        except Error as err:
            print("Creation of a new patient failed: ", err)

    # Delete dentist.
    def delete_dentist(self, dentistId):
        try:
            cursor = self.db.cursor()
            sql = "DELETE FROM dentist WHERE dentistId = %s"
            values = (dentistId,)
            cursor.execute(sql, values)
            self.db.commit()
        except Error as err:
            print(f"Failed to delete the dentist with id {dentistId}", err)
        

    # Delete patient.
    def delete_patient(self, patientId):
        try:
            cursor = self.db.cursor()
            sql = "DELETE FROM patient WHERE patientId = %s"
            values = (patientId,)
            cursor.execute(sql, values)
            self.db.commit()
        except Error as err:
            print(f"Failed to delete the patient with id {patientId}", err)
        


    # convert tuples to dictionary objects
    def convert_to_dict_dentist(self, result):
        colnames = ['dentistId', 'dentistName','position','regNumber']
        item = {}

        if result:
            for i, colname in enumerate(colnames):
                value = result[i]
                item[colname] = value
        return item

        # convert tuples to dictionary objects
    def convert_to_dict_patient(self, result):
        colnames = ['patientId', 'patientName','phone','dentistId']
        item = {}
        if result:
            for i, colname in enumerate(colnames):
                value = result[i]
                item[colname] = value
        return item

dentalClinicDAO = DentalClinicDAO()