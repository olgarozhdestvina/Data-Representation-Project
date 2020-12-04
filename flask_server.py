# Main server.
from flask import Flask, render_template
from dentists.dentists import dentist_table
from patients.patients import patient_table
from login.login import log

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

# Turned off the debug mode as it doesn't allow POST (405 error)
if __name__ == '__main__':
    app.run()