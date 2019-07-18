import os

DB_USERNAME = os.environ.get("mysql_username")
DB_HOST = os.environ.get("mysql_host")
DB_PASSWORD = os.environ.get("mysql_password")
SECRET_KEY = 'p9Bv<3Eid9%$i01'
#SQLALCHEMY_DATABASE_URI = 'mysql://dt_admin:dt2016@70.0.0.4/dreamteam_db'
SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST + '/dreamteam_db'
print SQLALCHEMY_DATABASE_URI
