"""
Project assessment
Data Representation Module GMIT 2020
Submitted by: Olga Rozhdestvina (Student No: G00387844)
Lecturer: Andrew Beatty
"""

# Main server.
from flask import Flask, render_template
from dentists.dentists import dentist_table
from patients.patients import patient_table
from login.login import log
from werkzeug.exceptions import BadRequest, NotFound, MethodNotAllowed, InternalServerError

# Flask app.
app = Flask(__name__, static_folder="main/static", template_folder="main/templates")

# Secret key to login.
app.secret_key = 'someKey'

# Blueprints
app.register_blueprint(dentist_table, url_prefix="/dentists")
app.register_blueprint(patient_table, url_prefix="/patients")
app.register_blueprint(log, url_prefix="/login")

# Main page
@app.route('/')
def home():
    return render_template("index.html")

# Error handlers
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return 'Bad request!', 400

@app.errorhandler(NotFound)
def handle_bad_request(e):
    return 'Page is not found!', 404

@app.errorhandler(MethodNotAllowed)
def handle_bad_request(e):
    return 'Method is not allowed!', 405
    
@app.errorhandler(InternalServerError)
def handle_bad_request(e):
    return 'Internal server error!', 500

# The debug mode is off as it doesn't allow POST (405 error)
if __name__ == '__main__':
    app.run(debug=True)