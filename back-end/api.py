import flask
from flask import request, json
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL
import jwt
from datetime import datetime, timedelta

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

def decode(request):
    token = None

    if 'x-access-token' in request.headres:
        token = request.headers['x-access-token']

    if not token:
        return app.response_class(status = 401) 

    try:
        data = jwt.decode(token, app.config['SECRET_KEY'])
        if data == request.headers['userId']:
            return true
    except:
        return app.response_class(status = 401)

    return app.response_class(status = 400)
        

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
    

@app.route('/createUser', methods=['POST'])
def createUser():

    params = request.form.to_dict()
    files = request.files.to_dict()
    username = params["username"]
    passowrd = params["password"]
    img = files["image"]

    # Query

    response = app.response_class(
        status = 200
    )

    return response

@app.route('/login', methods=['POST'])
def login():

    username = request.args.get("username")
    password = request.args.get("password")

    # Add Queries

    token = jwt.encode({
        'public_id': user.public_id,
        'exp': datetime.utcnow() + timedelta(minutes = 30)
    }, app.config['SECRET_KEY'])

    return make_response(jsonify({'token': token.decode("UTF-8")}), 201)


@app.route('/getCard', methods=['POST'])
def getCard():
    decode(request)

    # Query


app.run()
