"""
@package Load Settings

Loads the environment-dependent application config data including
 - UPLOAD_FOLDER - location where images are stored
 - SECRET_KEY - used to generate authentication tokens
 - MYSQL_DATABASE_DB
"""
from os import environ

UPLOAD_FOLDER = environ.get('UPLOAD_FOLDER')
SECRET_KEY = environ.get('SECRET_KEY')
MYSQL_DATABASE_DB = environ.get('MYSQL_DATABASE_DB')