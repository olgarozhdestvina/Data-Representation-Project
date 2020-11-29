from flask import Flask, request, abort, jsonify, render_template, session, url_for, redirect, flash
from datetime import timedelta
from DentalClinicDAO import dentalClinicDAO

app = Flask(__name__, static_url_path='', static_folder='templates')
app.secret_key = 'someKey'
# store session for 1 hour
app.permanent_session_lifetime = timedelta(hours=1)

# Main page
@app.route('/')
def home():
    return render_template("patients.html")

# Login
@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        # set session
        session.permanenet = True
        # get username from the form
        user = request.form["nm"]
        # store it in session
        session["user"] = user
        flash("Successfully logged in")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/databases", methods=['GET','POST'])
def database():
    # check if user is in session
    if "user" in session:
        user = session["user"]
        return render_template("databases.html", user=user)
    else:
        flash("Please login to access this page")
        return redirect(url_for("login"))

# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    # Only display the message if user is in the session
    flash(f"You have been logged out", "info")
    return redirect(url_for("login"))


# DENTIST TABLE
# Get all dentists
# curl http://127.0.0.1:5000/dentists
@app.route('/dentists')
def get_all_dentists():
    return jsonify(dentalClinicDAO.get_all_dentists())

# Find by dentistId
# curl http://127.0.0.1:5000/dentists/5
@app.route("/dentists/<int:dentistId>")
def find_by_dentistId(dentistId):
    return jsonify(dentalClinicDAO.find_by_dentistId(dentistId))

# Create dentist
# curl -X POST -H "content-type:application/json" -d "{\"dentistName\": \"Siobhan Fahey\", \"position\": \"endodontist\", \"regNumber\":\"123/2T\"}" http://127.0.0.1:5000/dentists
@app.route('/dentists', methods=['POST'])
def create_dentist():
    if not request.json:
        abort(400)
    dentist = {
        "dentistName": request.json["dentistName"],
        "position": request.json["position"],
        "regNumber": request.json["regNumber"]
    }
    values =(dentist['dentistName'],dentist['position'],dentist['regNumber'])
    newId = dentalClinicDAO.create_dentist(values)
    dentist['dentistId'] = newId
    return jsonify(dentist)


# Update dentist
# curl -X PUT -H "content-type:application/json" -d "{\"dentistName\": \"Siobhan Fahey\", \"position\": \"endodontist, implantologist\", \"regNumber\":\"123/2T\"}" http://127.0.0.1:5000/dentists/1
@app.route('/dentists/<int:dentistId>', methods=['PUT'])
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

    values = (foundDentist['dentistName'],foundDentist['position'],foundDentist['regNumber'],foundDentist['dentistId'])
    dentalClinicDAO.update_dentist(values)
    return jsonify(foundDentist)


# Delete dentist
# curl -X DELETE http://127.0.0.1:5000/dentists/1
@app.route("/dentists/<int:dentistId>", methods=['DELETE'])
def delete_dentist(dentistId):
    dentalClinicDAO.delete_dentist(dentistId)
    return jsonify({"Done":True})



# PATIENT TABLE
# Get all patient
# curl http://127.0.0.1:5000/patients
@app.route('/patients')
def get_all_patients():
    return jsonify(dentalClinicDAO.get_all_patients())

# Find by patientId
# curl http://127.0.0.1:5000/patients/5
@app.route("/patients/<int:patientId>")
def find_by_patientId(patientId):
    return jsonify(dentalClinicDAO.find_by_patientId(patientId))

# Create patient
# curl -X POST -H "content-type:application/json" -d "{\"patientName\": \"Siobhan Fahey\", \"phone\":\"0875467686\", \"dentistId\":null}" http://127.0.0.1:5000/patients
@app.route('/patients', methods=['POST'])
def create_patient():
    if not request.json:
        abort(400)
    patient = {
        "patientName": request.json["patientName"],
        "phone": request.json["phone"],
        "dentistId": request.json["dentistId"]
    }
    values =(patient['patientName'],patient['phone'],patient["dentistId"])
    newId = dentalClinicDAO.create_patient(values)
    patient['patientId'] = newId
    return jsonify(patient)


# Update patient
# curl -X PUT -H "content-type:application/json" -d "{\"patientName\": \"Siobhan Fay\", \"phone\":\"0895467690\", \"dentistId\":null}" http://127.0.0.1:5000/patients/1
@app.route('/patients/<int:patientId>', methods=['PUT'])
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

    values = (foundPatient['patientName'],foundPatient['phone'],foundPatient['patientId'],foundPatient['dentistId'])
    dentalClinicDAO.update_patient(values)
    return jsonify(foundPatient)


# Delete patient
# curl -X DELETE http://127.0.0.1:5000/patients/1
@app.route("/patients/<int:patientId>", methods=['DELETE'])
def delete_patient(patientId):
    dentalClinicDAO.delete_patient(patientId)
    return jsonify({"Done":True})


if __name__ == "__main__":
    app.run(debug=True)