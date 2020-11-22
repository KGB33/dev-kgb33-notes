import os
from uuid import uuid4


class Base:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", str(uuid4()))


class Testing(Base):
    TESTING = True
    WTF_CSRF_ENABLED = False


class Development(Base):
    DEVELOPMENT = True
    DEBUG = True


class Production(Base):
    DEBUG = False
