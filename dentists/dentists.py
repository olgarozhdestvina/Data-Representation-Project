# DENTIST TABLE

from flask import Blueprint, abort, jsonify, request
from main.DentalClinicDAO import dentalClinicDAO

# Create a blueprint.
dentist_table = Blueprint("dentists", __name__,
                          static_folder="static", template_folder="templates")

# Get all dentists.
# curl http://127.0.0.1:5000/dentists/
@dentist_table.route('/')
def get_all_dentists():
    return jsonify(dentalClinicDAO.get_all_dentists())

# Find by dentistId.
# curl http://127.0.0.1:5000/dentists/1
@dentist_table.route('/<int:dentistId>')
def find_by_dentistId(dentistId):
    return jsonify(dentalClinicDAO.find_by_dentistId(dentistId))

# Create dentist.
# curl -X POST -H "content-type:application/json" -d "{\"dentistName\": \"Siobhan Fahey\", \"position\": \"Endodontist\", \"regNumber\":\"123/2T\"}" http://127.0.0.1:5000/dentists/
@dentist_table.route('/', methods=['GET', 'POST'])
def create_dentist():
    if not request.json:
        abort(400)
    dentist = {
        'dentistName': request.json['dentistName'],
        'position': request.json['position'],
        'regNumber': request.json['regNumber']
    }
    values = (dentist['dentistName'],
              dentist['position'], dentist['regNumber'])
    newId = dentalClinicDAO.create_dentist(values)
    dentist['dentistId'] = newId
    return jsonify(dentist)

# Update dentist.
# curl -X PUT -H "content-type:application/json" -d "{\"dentistName\": \"Siobhan Fahey\", \"position\": \"Implantologist\", \"regNumber\":\"123/2T\"}" http://127.0.0.1:5000/dentists/1
@dentist_table.route('/<int:dentistId>', methods=['PUT'])
def update_dentist(dentistId):
    foundDentist = dentalClinicDAO.find_by_dentistId(dentistId)
    if not foundDentist:
        abort(404)
    if not request.json:
        abort(400)
    if 'dentistName' in request.json:
        foundDentist['dentistName'] = request.json['dentistName']
    if 'position' in request.json:
        foundDentist['position'] = request.json['position']
    if 'regNumber' in request.json:
        foundDentist['regNumber'] = request.json['regNumber']

    values = (foundDentist['dentistName'], foundDentist['position'],
              foundDentist['regNumber'], foundDentist['dentistId'])
    dentalClinicDAO.update_dentist(values)
    return jsonify(foundDentist)


# Delete dentist.
# curl -X DELETE http://127.0.0.1:5000/dentists/1
@dentist_table.route('/<int:dentistId>', methods=['DELETE'])
def delete_dentist(dentistId):
    dentalClinicDAO.delete_dentist(dentistId)
    return jsonify({'Done': True})
