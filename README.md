# Project assessment for Data Representation Module GMIT 2020

The repository contains a web application project.

*Submitted by:* Olga Rozhdestvina (Student No: G00387844) 

*Lecturer:* Andrew Beatty

*Programming Languages used:* [Python](https://www.python.org/), [HTML](https://html.com/), [JavaScript](https://www.javascript.com/), [MySQL](https://www.mysql.com/)


----


## Table of Contents
* [Set up](#set_up)
* [How to run the code](#how_to_run_the_code)
* [License](#licence)


----


### Set up <a name="set_up"></a>

Applications used for completion of the tasks are 
  * [Visual Studio Code](https://code.visualstudio.com/),
  * [cmder](http://cmder.net/),
 


Distribution of Python is [Anaconda Python distribution](https://www.anaconda.com/). 

Packages and modules used to complete the project: 
[mysql.connector](https://pypi.org/project/mysql-connector-python/),
[venv](https://docs.python.org/3/library/venv.html),
[flask](https://flask.palletsprojects.com/en/1.1.x/)



----


###  How to run the code <a name="how_to_run_the_code"></a>

1. Make sure that you have Python and above packages installed 
2. Download or clone current repository "Data-Representation-Project"
3. Open Command Interpreter and get into correct directory
4. Run createDatabase.py and then createTable.py to initialize a database called "dentalclinic" with a table called "dentists" // or use instructions from initdb.sql in MySQL command line client.
5. Make a virtual environment by running python -m venv venv and then .\venv\Scripts\activate.bat to activate it.
6. Set Flask app to flask_server and run it.
7. To open index.html follow the flask URL with index.html added to it. 
8. Or perform CRUD on the database through another instance of Command Interpreter.


----

### License <a name="licence"></a>

This project is licensed under the MIT License - see the LICENSE.md file for details