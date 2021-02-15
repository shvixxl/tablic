"""App configuration"""

import os


MONGO_URI = 'mongodb://{username}:{password}@{host}:{port}/{db}'.format(
    db = os.environ.get('DB_NAME'),

    host = os.environ.get('DB_HOST'),
    port = os.environ.get('DB_PORT'),

    username = os.environ.get('DB_USERNAME'),
    password = os.environ.get('DB_PASSWORD'),
)

MONGO_USER_COLLECTION = 'users'
