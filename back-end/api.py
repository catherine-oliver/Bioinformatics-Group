import flask
from flask import request, json
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'api'
app.config['MYSQL_DATABASE_PASSWORD'] = 'csci4830'
app.config['MYSQL_DATABASE_DB'] = 'vaccineData'
app.config['MYSQL_DATABASE_HOST'] = 'ec2-3-16-22-47.us-east-2.compute.amazonaws.com'
app.config['MYSQL_DATABASE_PORT'] = 3306
print(app.config)
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

@app.route('/getVaccineData', methods=['GET'])
def getVaccineData():
    state = request.args.get('state', '')
    ages = request.args.get('ages', '')
    vaxType = request.args.get('vaxType', '')
    print(state)
    print(ages)
    print(vaxType)
    
    colString = 'administered'

    if (ages == '12-17'):
        colString = colString + ', administered_12Plus'
    elif (ages == '18-64'):
        colString = colString + ', administered_18Plus'
    elif (ages == '65+'):
        colString = colString + ', administered_65Plus'
    else:
        colString = colString + ', administered'

    if (vaxType == 'Johnson & Johnson'):
       colString = colString + ', administered_Janssen'
    elif (vaxType == 'Moderna'):
        colString = colString + ', administered_Moderna'
    elif (vaxType == 'Pfizer'):
        colString = colString + ', administered_Pfizer'
    else:
        colString = colString + ', administered' 
    print(colString)

    print('SELECT * FROM {0} WHERE location == \'{1}\''.format(colString, state))
    cursor.execute('SELECT {0} FROM total_vaccinations WHERE location = \'{1}\''.format(colString, state))
    data = cursor.fetchone()

    response = app.response_class(
        response=json.dumps(data),
        status = 200,
    )
    return response
    

app.run()
