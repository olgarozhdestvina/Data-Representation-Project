from flask import Flask, request, abort, jsonify
from DentistDAO import dentistDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

dentists = [
    {"dentistId": 1, "dentistName": "Natasha Wood", "position": "general dentist", "regNumber": "34/5Y"},
    {"dentistId": 2, "dentistName": "Ciaran Smith", "position": "orthodontist", "regNumber": "654/2"},
    {"dentistId": 3, "dentistName": "Sonia Alapont", "position": "maxillofacial surgeon", "regNumber": "56/3Z"}
]

@app.route('/')
def index():
    return "Hello, sad World"

# Get all
@app.route('/dentists')
def get_all():
    return jsonify(dentistDAO.get_all())

# Find by dentistId
@app.route("/dentists/<int:dentistId>")
def find_by_dentistId(dentistId):
    return jsonify(dentistDAO.find_by_dentistId(dentistId))

# Create
# curl -X POST -H "content-type:application/json" -d "{\"dentistName\": \"Siobhan Fahey\", \"position\": \"endodontist\", \"regNumber\":\"123/2T\"}" http://127.0.0.1:5000/dentists
@app.route('/dentists', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    dentist = {
        "dentistName": request.json["dentistName"],
        "position": request.json["position"],
        "regNumber": request.json["regNumber"]
    }
    return jsonify(dentistDAO.create(dentist))



# Update
# curl -X PUT -H "content-type:application/json" -d "{\"dentistName\": \"Siobhan Fahey\", \"position\": \"endodontist, implantologist\", \"regNumber\":\"123/2T\"}" http://127.0.0.1:5000/dentists/1

@app.route('/dentists/<int:dentistId>', methods=['PUT'])
def update(dentistId):
    founddentist = dentistDAO.find_by_dentistId(dentistId)
    if founddentist == {}:
        return jsonify({}), 404
    currentdentist = founddentist
    if 'dentistName' in request.json:
        currentdentist['dentistName'] = request.json['dentistName']
    if 'position' in request.json:
        currentdentist['position'] = request.json['position']
    if 'regNumber' in request.json:
        currentdentist['regNumber'] = request.json['regNumber']

    dentistDAO.update(currentdentist)
    return jsonify(currentdentist)



# Delete
# curl -X DELETE http://127.0.0.1:5000/dentists/1

@app.route("/dentists/<int:dentistId>", methods=['DELETE'])
def delete(dentistId):
    foundDentist = list(filter(lambda t: t["dentistId"] == dentistId, dentists))
    if len(foundDentist) == 0:
        return jsonify({}), 404
    dentists.remove(foundDentist[0])
    return jsonify({"Done":True})


if __name__ == "__main__":
    app.run(debug=True)