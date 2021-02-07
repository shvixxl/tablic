import os


# Basic Flask configuration
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', os.urandom(64))


# MongoDB configuration
MONGODB_SETTINGS = {
    'db': os.environ.get('DB_NAME', 'tablic'),
    
    'host': os.environ.get('DB_HOST', 'localhost'),
    'port': os.environ.get('DB_PORT', 27017),

    'username': os.environ.get('DB_USERNAME', ''),
    'password': os.environ.get('DB_PASSWORD', ''),
}
