import flask
from flask import request
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABSE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = ''

@app.route('/getVaccineData', methods=['GET'])
def getVaccineData():
    vaccineParams = request.args.get('vaccineParams', '')
    print(vaccineParams)
    return 'To be Added'
    

app.run()
