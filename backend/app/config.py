"""App configuration"""

import os
from typing import List
from datetime import timedelta


SECRET_KEY = os.environ.get('SECRET_KEY')
CORS_ORIGINS = [s.strip() for s in os.environ.get('CORS_ORIGINS').split(',')]
ACCESS_TOKEN_EXPIRE_DAYS = timedelta(int(os.environ.get('ACCESS_TOKEN_EXPIRE_DAYS')))


DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

DB_URI = f'mongodb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/'

USER_COLLECTION_NAME = 'users'
