from flask import Flask, request, abort, jsonify, render_template, session, url_for, redirect, flash
from datetime import timedelta
from DentistDAO import dentistDAO

app = Flask(__name__, static_url_path='', static_folder='templates')
app.secret_key = 'someKey'
# store session for 1 hour
app.permanent_session_lifetime = timedelta(hours=1)

# Main page
@app.route('/')
def index():
    return render_template("index.html")

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


@app.route("/user", methods=['GET','POST'])
def user():
    # check if user is in session
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
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