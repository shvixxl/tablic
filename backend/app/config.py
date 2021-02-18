"""App configuration"""

import os
from datetime import timedelta


MONGO_URI = 'mongodb://{username}:{password}@{host}:{port}/'.format(
    host = os.environ.get('DB_HOST'),
    port = os.environ.get('DB_PORT'),

    username = os.environ.get('DB_USERNAME'),
    password = os.environ.get('DB_PASSWORD'),
)

MONGO_USER_COLLECTION = 'users'


SECRET_KEY = os.environ.get('SECRET_KEY')
ACCESS_TOKEN_EXPIRE_DAYS = timedelta(int(os.environ.get('ACCESS_TOKEN_EXPIRE_DAYS')))
