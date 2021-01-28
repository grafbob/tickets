import os

db_host = os.environ.get('DB_HOST', default='<10.0.1.152>')
db_name = os.environ.get('DB_NAME', default='cloud_user')
db_password = os.environ.get('DB_PASSWORD', default='IisWgdcwjq')
db_port = os.environ.get('DB_PORT', default='5432')
db_user = os.environ.get('DB_USERNAME', default='cloud_user')

SQLALCHEMY_DATABASE_URI = f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


