# PATIENT TABLE

from flask import Blueprint, abort, jsonify, request
from main.DentalClinicDAO import dentalClinicDAO

patient_table = Blueprint("patient_table", __name__, static_folder="static", template_folder="templates")
# Get all patient
# curl http://127.0.0.1:5000/patients/
@patient_table.route('/')
def get_all_patients():
    return jsonify(dentalClinicDAO.get_all_patients())

# Find by patientId
# curl http://127.0.0.1:5000/patients/1
@patient_table.route('/<int:patientId>')
def find_by_patientId(patientId):
    return jsonify(dentalClinicDAO.find_by_patientId(patientId))

# Create patient
# Make sure there is at least one dentist in the dentist table to be able to create a patient as tables are connected on foreign key. 
# curl -X POST -H "content-type:application/json" -d "{\"patientName\": \"Sinead Howe\", \"phone\": \"0895467690\", \"dentistId\":1}" http://127.0.0.1:5000/patients/
@patient_table.route('/', methods=['GET','POST'])
def create_patient():
    if not request.json:
        abort(400)
    patient = {
        'patientName': request.json['patientName'],
        'phone': request.json['phone'],
        'dentistId': request.json['dentistId']
    }
    values =(patient['patientName'],patient['phone'],patient['dentistId'])
    newId = dentalClinicDAO.create_patient(values)
    patient['patientId'] = newId
    return jsonify(patient)


# Update patient
# curl -X PUT -H "content-type:application/json" -d "{\"patientName\": \"Sinead Spillane\", \"phone\": \"0875467696\", \"dentistId\":1}" http://127.0.0.1:5000/patients/1
@patient_table.route('/<int:patientId>', methods=['PUT'])
def update_patient(patientId):
    foundPatient = dentalClinicDAO.find_by_patientId(patientId)
    if not foundPatient:
        abort(404)
    if not request.json:
        abort(400)
    if 'patientName' in request.json:
        foundPatient['patientName'] = request.json['patientName']
    if 'phone' in request.json:
        foundPatient['phone'] = request.json['phone']
    if 'dentistId' in request.json:
        foundPatient['dentistId'] = request.json['dentistId']

    values = (foundPatient['patientName'],foundPatient['phone'],foundPatient['dentistId'],foundPatient['patientId'])
    dentalClinicDAO.update_patient(values)
    return jsonify(foundPatient)


# Delete patient
# curl -X DELETE http://127.0.0.1:5000/patients/1
@patient_table.route('/<int:patientId>', methods=['DELETE'])
def delete_patient(patientId):
    dentalClinicDAO.delete_patient(patientId)
    return jsonify({'Done':True})