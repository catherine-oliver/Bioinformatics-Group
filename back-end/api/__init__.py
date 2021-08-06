import flask
from flask import request, json, jsonify, send_file
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL
import jwt
from datetime import datetime, timedelta
import io


def create_app():
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
        print(request)
        print(request.args)
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
        except 
            print(e)
            return app.response_class(status=400)

    @app.route('/api/login', methods=['POST'])
    def login():
        params = request.form.to_dict()
        print(params)
        username = params["username"]
        password = params["password"]
        print(username)
        print(password)

        cursor.execute('SELECT user_id, username, password FROM user WHERE username = \'{0}\''.format(username))
        user = cursor.fetchone()

        print(user)
        if (user):
            if user[2] == password:
                token = jwt.encode({
                    'user_id': user[0],
                    'exp': datetime.utcnow() + timedelta(minutes = 30)
                }, app.config['SECRET_KEY'])

                print(token)

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
        print(request.args)
        params = request.args.to_dict()
        if (decode(params)):
            username = params['username']
            userId = params['userId']
            cursor.execute("SELECT image_loc FROM user WHERE username = \'{0}\' AND user_id = \'{1}\'".format(username, userId))
            data = cursor.fetchone()

            if (data):
                print(data[0])
                return send_file(data[0], mimetype="image/*")
            else:
                return app.response_class(
                status = 400
                )
            
        # should return error from decode method


    return app
