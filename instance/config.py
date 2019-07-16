import os

#DB_USERNAME = os.environ.get("mysql_username")
DB_HOST = os.environ.get("mysql_host")
SECRET_KEY = 'p9Bv<3Eid9%$i01'
#SQLALCHEMY_DATABASE_URI = 'mysql://dt_admin:dt2016@70.0.0.4/dreamteam_db'
SQLALCHEMY_DATABASE_URI = 'mysql://dt_admin:dt2016@' + DB_HOST + '/dreamteam_db'
