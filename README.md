## Dental Clinic
### [Project assessment for Data Representation Module GMIT 2020]

<img height="220" src="https://drdds.com/wp-content/uploads/2019/09/Illustration_DentalClinic.png">

<br>

The repository contains a CRUD (Create, Read, Update, Delete) dentist/ patient management web application **Dental Clinic.** It is built using *Flask*, a microframework for Python, and *MySQL*, a database management system. 
<br>

The project has the following features:
 * A Flask server with a REST API
 * Interaction with a third party API using jQuery
 * MySQL database with two table accessible with authorization
 * Web interface using AJAX calls
 * Online hosted on PythonAnywhere

<br>

*Submitted by:* Olga Rozhdestvina (Student No: G00387844) 

*Lecturer:* Andrew Beatty

*Programming Languages used:* [Python](https://www.python.org/), [HTML](https://html.com/), [JavaScript](https://www.javascript.com/), [MySQL](https://www.mysql.com/)


----


### Table of Contents
* [Set up](#set_up)
* [How to run the code](#how_to_run_the_code)
* [License](#licence)
* [Acknowledgment](#acknowledgment)


----


#### Set up <a name="set_up"></a>

Applications used for completion of the tasks are 
  * [Visual Studio Code](https://code.visualstudio.com/)
  * [cmder](http://cmder.net/)

Distribution of Python is [Anaconda Python distribution](https://www.anaconda.com/). 

Packages and modules used to complete the project: 
  * [mysql.connector](https://pypi.org/project/mysql-connector-python/)
  * [venv](https://docs.python.org/3/library/venv.html)
  * [flask](https://flask.palletsprojects.com/en/1.1.x/)
  * [datetime](https://docs.python.org/3/library/datetime.html)



----


####  How to run the code <a name="how_to_run_the_code"></a>

  * _On remote._

To view the project on remove please follow the link http://olgarozhdestvina.pythonanywhere.com/ on PythonAnywhere.

  * _Locally._
  
To run on your local machine follow the instructions below. 

1. Get into directory _"Data-Representation-Project"_ in your Command Interpreter
2. Run __createDatabase.py__ and then __createTables.py__ to initialize a database _"dentalclinic"_ or follow instructions in _initdb.sql_ in MySQL command line client.
3. Run __python -m venv venv__ to make a virtual environment.
4. Activate venv by running:

    * Windows:
    ```bash
    .\venv\Scripts\activate.bat
    ```
    * Linux:
    ```bash
    source venv/bin/activate
    ```
5. Install packages by running __pip install -r requirements.txt__
6. Set Flask app to flask_server and run it: 
    
    * Windows:
    ```bash
    set FLASK_APP=flask_server
    flask run
    ```
    * Linux: 
    ```bash
    export FLASK_APP=flask_server
    flask run
    ```
7. Follow the flask URL to perform CRUD operations on the database or do it through another instance of Command Interpreter with CURL.
8. Run __deactivate__ to exit venv.


----

#### License <a name="licence"></a>

This project is licensed under the MIT License - see the LICENSE.md file for details

----


#### Acknowledgment <a name="acknowledgment"></a>

- GMIT Lecturer [Andrew Beatty](https://github.com/andrewbeattycourseware) 
- [Stack Overflow](https://stackoverflow.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Tech With Tim: Flask Tutorials](https://www.youtube.com/playlist?list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX)
- [teclado](https://blog.tecladocode.com)
- [Caspio](https://forums.caspio.com/)
- [w3schools.com](http://w3schools.com/)
- [Unsplash](https://unsplash.com/)
- [PythonAnywhere](https://www.pythonanywhere.com/)
