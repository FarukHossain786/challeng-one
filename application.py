# Clone the repo and run pip install requirements.txt
# python version 3.7

from flask import Flask, render_template, request
import logging
from challenge.Pdfcreater import Pdfcreater
from challenge.Check import Database
from challenge import Dbconnection
import os
logging.basicConfig(filename='log/app.log', filemode='w',level=logging.INFO)

application = Flask(__name__)
app=application

@app.route('/')
def home():
    if request.method == 'GET':
        connection = Dbconnection.DB()
        mongo_db= connection.mongo()
        c_details = mongo_db['course_details']
        course = c_details.find().limit(25)
        path = os.path
        return render_template("home.html",result = course, path=path)

@app.route('/grabe-all')
def graball():
    grabcat = Pdfcreater()
    grabcat.grab_category()
    return "Nothig"

@app.route('/create-database')
def create_database():
    create = Database()
    create.create_table()
    create.mongo_test()
    return "Database updated Done!"





if __name__ == '__main__':
    app.run(host='0.0.0.0')

