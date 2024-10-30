import os
class Config:
    SECRET_KEY = 'mySecretKey'
    SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME = '127.0.0.1:5000'
