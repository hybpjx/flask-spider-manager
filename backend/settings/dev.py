import os
from datetime import timedelta

base_dir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SESSION_TYPE = 'filesystem'
SECRET_KEY = os.urandom(24)
PERMANENT_SESSION_LIFETIME = timedelta(weeks=1)
JSON_AS_ASCII = False
SQLALCHEMY_DATABASE_URI = "sqlite:///TianYaLunTan.db"
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

