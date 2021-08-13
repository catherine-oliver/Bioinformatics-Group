"""
@package Flask API
This code is used to configure a Flask API app.

Dependencies:
 - Flask
 - Flask_CORS
 - JSON WebToken
 - DateTime
 - flask-mysql
"""
import flask
from flask import request, json, jsonify, send_file
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL
import jwt
from datetime import datetime, timedelta
import io


def create_app():
    """Generates the API app

    Loads default parameters into the app config. These remain constant no matter what environment they are loaded in.
     - CORS_HEADER = Content-Type
     - MYSQL_DATABASE_USER
     - MYSQL_DATABASE_PASSWORD
     - MYSQL_DATABASE_HOST
     - MYSQL_DATABASE_PORT

    Parameters are loaded from environment files by calling settings.py

    @return app - the configured API app.

    The API consists of 4 API hooks:

    - getVaccineData() - GET Request - Located at /api/getVaccineData

        Takes the state abbreviation, age range, and vaccine type query parameters from the request file.
        Then, these are used to determine what columns from the total_vaccine table to query. Finally, the
        query string is built and used to query the database. Once the data is returned, any null values are replaced with
        "Unreported" and sent back in the response.
    
    - getCard() - GET Request - Located at /api/getCard

        Grabs the header from the request and passes it to the decode method. If the decode method is able to decode the header, the username and userID are used
        to query the user table for the correpsonding image file location. The image is retrieved from this location in binary format and returned. If there is no existing user, a 400
        status is returned.

    - createUser() - POST Request - Located at /api/createUser

        Grabs the username, password, and image file from the request object. The image is then saved in the upload location provided in
        the app configuraton. Then, the username and password are inserted into the database using an INSERT statement. If this is successful, 
        a 200 status will be returned in the request. Otherwise, a 400 status will be returned.

    - login() - POST Request - Located at /api/login

        Grabs the username and password from the request object's parameters and then uses the username to query the user table.
        If a user is not found, a 401 status is returned. If the user is found, the stored password and provided password are compared. If they do not match,
        a 401 status is returned. If the passwords do match, the user's userId is used to generate a JSON webtoken. This token is returned along with the userID, username, and a 201 status.

    Additionally, the API has 1 helper function:

    - decode(param)

        Decodes a JSON webtoken using the secret key. This token can then be comapred to a user ID to validate that a user has logged in.
        @param param the header of the request containing the token, userID, and username of a logged in user.
    """
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config.from_pyfile('settings.py')
    app.config['MYSQL_DATABASE_USER'] = 'api'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'csci4830'
    app.config['MYSQL_DATABASE_HOST'] = 'ec2-52-14-14-132.us-east-2.compute.amazonaws.com'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    mysql = MySQL()
    print(app.config)
    mysql.init_app(app)

    conn = mysql.connect()
    cursor = conn.cursor()

    def decode(params):
        token = None

        if 'x-access-token' in params:
            token = params['x-access-token']

        if not token:
            return app.response_class(status = 401) 

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            if data == params['userId']:
                return true
        except:
            return app.response_class(status = 401)

        return app.response_class(status = 400)
            

    @app.route('/api/getVaccineData', methods=['GET'])
    def getVaccineData():
        state = request.args.get('state', '')
        ages = request.args.get('ages', '')
        vaxType = request.args.get('vaxType', '')

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

        print('SELECT * FROM {0} WHERE location == \'{1}\''.format(colString, state))
        cursor.execute('SELECT {0} FROM total_vaccinations WHERE location = \'{1}\''.format(colString, state))
        data = list(cursor.fetchone())
        
        for i in range(0, len(data)):
            if data[i] == None:
                data[i] = "Unreported"

        response = app.response_class(
            response=json.dumps(data),
            status = 200,
        )
        return response
        

    @app.route('/api/createUser', methods=['POST'])
    def createUser():
        params = request.form.to_dict()
        files = request.files.to_dict()
        username = params["username"]
        password = params["password"]
        img = files["image"]
        imgPath = app.config['UPLOAD_FOLDER'] + username + '.jpg'
        img.save(imgPath)

        try:
            print('INSERT INTO user (username, password, image_loc) VALUES (\'{0}\',\'{1}\',\'{2}\');'.format(username, password, imgPath))
            cursor.execute('INSERT INTO user (username, password, image_loc) VALUES (\'{0}\',\'{1}\',\'{2}\');'.format(username, password, imgPath))
            conn.commit()
            data = cursor.fetchone()
            print(data)
            return app.response_class(status = 200)
        except:
            print(e)
            return app.response_class(status=400)

    @app.route('/api/login', methods=['POST'])
    def login():
        params = request.form.to_dict()
        username = params["username"]
        password = params["password"]

        cursor.execute('SELECT user_id, username, password FROM user WHERE username = \'{0}\''.format(username))
        user = cursor.fetchone()

        if (user):
            if user[2] == password:
                token = jwt.encode({
                    'user_id': user[0],
                    'exp': datetime.utcnow() + timedelta(minutes = 30)
                }, app.config['SECRET_KEY'])

                return app.response_class(
                    response=json.dumps({
                        'token': token,
                        'username': user[1],
                        'userId': user[0]}), 
                    status =201)
            else:
                return app.response_class(
                    status = 401
                )
        else:
            return app.response_class(
                status = 401
            )


    @app.route('/api/getCard', methods=['GET'])
    def getCard():
        params = request.args.to_dict()
        if (decode(params)):
            username = params['username']
            userId = params['userId']
            cursor.execute("SELECT image_loc FROM user WHERE username = \'{0}\' AND user_id = \'{1}\'".format(username, userId))
            data = cursor.fetchone()

            if (data):
                return send_file(data[0], mimetype="image/*")
            else:
                return app.response_class(
                status = 400
                )


    return app
