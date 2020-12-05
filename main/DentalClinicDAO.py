# Manipulating MySQL database dentalclinic with DAO

import mysql.connector
from mysql.connector.errors import Error
# Configurations to access MySQL
import dbconfig as cfg


class DentalClinicDAO:
    # Connect to the database.
    def init_connect_to_db(self):
        db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql["database"],
            pool_name=cfg.mysql["pool_name"],
            pool_size = 10
        )
        return db

    def get_connection(self):
        db = mysql.connector.connect(
            pool_name=cfg.mysql["pool_name"]
        )
        return db

    def __init__(self):
        db = self.init_connect_to_db()
        db.close()


    # DENTIST TABLE.
    # Create a dentist.
    def create_dentist(self, values):
        try:
            db = self.get_connection()
            cursor = db.cursor()
            sql = "INSERT INTO dentist (dentistName, position, regNumber) values (%s, %s, %s)"
            cursor.execute(sql, values)
            self.db.commit()
            lastrowid = cursor.lastrowid
            db.close()
            return lastrowid
        except Error as err:
            print("Creation of a new dentist failed:", err)
            exit(1)

    # Get all dentists.
    def get_all_dentists(self):
        try:
            db = self.get_connection()
            cursor = db.cursor()
            sql = "SELECT * FROM dentist"
            cursor.execute(sql)
            results = cursor.fetchall()
            returnArray = []
            for result in results:
                returnArray.append(self.convert_to_dict_dentist(result))
            db.close()
            return returnArray
        except Error as err:
            print("Error: ", err)

    # Get dentist by ID.
    def find_by_dentistId(self, dentistId):
        try:
            db = self.get_connection()
            cursor = db.cursor()
            sql = "SELECT * FROM dentist WHERE dentistId = %s"
            values = (dentistId,)
            cursor.execute(sql, values)
            result = cursor.fetchone()
            dentist = self.convert_to_dict_dentist(result)
            db.close()
            return dentist
        except Error as err:
            print(f"Dentist with id {dentistId} doesn't exist", err)

    # Update dentist.
    def update_dentist(self, values):
        try:
            db = self.get_connection()
            cursor = db.cursor()
            sql = "UPDATE dentist SET dentistName = %s, position = %s, regNumber = %s WHERE dentistId = %s"
            cursor.execute(sql, values)
            db.commit()
            db.close()
        except Error as err:
            print("Creation of a new dentist failed: ", err)

    # Delete dentist.
    def delete_dentist(self, dentistId):
        try:
            db = self.get_connection()
            cursor = db.cursor()
            sql = "DELETE FROM dentist WHERE dentistId = %s"
            values = (dentistId,)
            cursor.execute(sql, values)
            db.commit()
            db.close()
        except Error as err:
            print(f"Failed to delete the dentist with id {dentistId}", err)

    # Convert tuples with dentist info to dictionary objects.
    def convert_to_dict_dentist(self, result):
        colnames = ['dentistId', 'dentistName', 'position', 'regNumber']
        item = {}

        if result:
            for i, colname in enumerate(colnames):
                value = result[i]
                item[colname] = value
        return item

    # PATIENT TABLE.
    # Create a patient.
    def create_patient(self, values):
        try:
            db = self.get_connection()
            cursor = db.cursor()
            sql = "INSERT INTO patient (patientName, phone, dentistId) values (%s, %s, %s)"
            cursor.execute(sql, values)
            db.commit()
            lastrowid = cursor.lastrowid
            db.close()
            return lastrowid
        except Error as err:
            print("Creation of a new patient failed:", err)

    # Get all patients.
    def get_all_patients(self):
        try:
            db = self.get_connection()
            cursor = db.cursor()
            sql = "SELECT * FROM patient"
            cursor.execute(sql)
            results = cursor.fetchall()
            returnArray = []
            for result in results:
                returnArray.append(self.convert_to_dict_patient(result))
            db.close()
            return returnArray
        except Error as err:
            print("Error: ", err)

    # Get patient by ID.
    def find_by_patientId(self, patientId):
        try:
            db = self.get_connection()
            cursor = db.cursor()
            sql = "SELECT * FROM patient WHERE patientId = %s"
            values = (patientId,)
            cursor.execute(sql, values)
            result = cursor.fetchone()
            patient = self.convert_to_dict_patient(result)
            db.close()
            return patient
        except Error as err:
            print(f"Patient with id {patientId} doesn't exist", err)

    # Update patient.
    def update_patient(self, values):
        try:
            db = self.get_connection()
            cursor = db.cursor()
            sql = "UPDATE patient SET patientName = %s, phone = %s, dentistId= %s WHERE patientId = %s"
            cursor.execute(sql, values)
            db.commit()
            db.close()
        except Error as err:
            print("Creation of a new patient failed: ", err)

    # Delete patient.
    def delete_patient(self, patientId):
        try:
            db = self.get_connection()
            cursor = db.cursor()
            sql = "DELETE FROM patient WHERE patientId = %s"
            values = (patientId,)
            cursor.execute(sql, values)
            db.commit()
            db.close()
        except Error as err:
            print(f"Failed to delete the patient with id {patientId}", err)

    # Convert tuples with patient info to dictionary objects.
    def convert_to_dict_patient(self, result):
        colnames = ['patientId', 'patientName', 'phone', 'dentistId']
        item = {}
        if result:
            for i, colname in enumerate(colnames):
                value = result[i]
                item[colname] = value
        return item


# An instance of DAO.
dentalClinicDAO = DentalClinicDAO()