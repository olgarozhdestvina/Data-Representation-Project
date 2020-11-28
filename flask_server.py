from flask import Flask, request, abort, jsonify, render_template, session, url_for
from DentistDAO import dentistDAO

app = Flask(__name__, static_url_path='', static_folder='templates')
app.secret_key = 'someKey'

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/login", methods=['GET','POST'])
def login():
    return render_template()

@app.route("/<usr>", methods=['GET','POST'])
def user(usr):
    return "<h1>Hello, {usr} </h1>"

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
    values =(dentist['dentistName'],dentist['position'],dentist['regNumber'])
    newId = dentistDAO.create(values)
    dentist['dentistId'] = newId
    return jsonify(dentist)



# Update
# curl -X PUT -H "content-type:application/json" -d "{\"dentistName\": \"Siobhan Fahey\", \"position\": \"endodontist, implantologist\", \"regNumber\":\"123/2T\"}" http://127.0.0.1:5000/dentists/1

@app.route('/dentists/<int:dentistId>', methods=['PUT'])
def update(dentistId):
    foundDentist = dentistDAO.find_by_dentistId(dentistId)
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

    values = (foundDentist['dentistName'],foundDentist['position'],foundDentist['regNumber'],foundDentist['dentistId'])
    dentistDAO.update(values)
    return jsonify(foundDentist)



# Delete
# curl -X DELETE http://127.0.0.1:5000/dentists/1

@app.route("/dentists/<int:dentistId>", methods=['DELETE'])
def delete(dentistId):
    dentistDAO.delete(dentistId)
    return jsonify({"Done":True})


if __name__ == "__main__":
    app.run(debug=True)