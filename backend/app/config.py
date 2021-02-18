"""App configuration"""

import os
from datetime import timedelta


# MongoDB

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

MONGO_URI = f'mongodb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/'

MONGO_USER_COLLECTION = 'users'


# Authentication

SECRET_KEY = os.environ.get('SECRET_KEY')
ACCESS_TOKEN_EXPIRE_DAYS = timedelta(int(os.environ.get('ACCESS_TOKEN_EXPIRE_DAYS')))
