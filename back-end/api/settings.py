from os import environ

UPLOAD_FOLDER = environ.get('UPLOAD_FOLDER')
SECRET_KEY = environ.get('SECRET_KEY')
MYSQL_DATABASE_DB = environ.get('MYSQL_DATABASE_DB')