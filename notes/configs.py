import os


class Base:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ["FLASK_SECRET_KEY"]


class Testing(Base):
    TESTING = True
    WTF_CSRF_ENABLED = False


class Development(Base):
    DEVELOPMENT = True
    DEBUG = True


class Production(Base):
    DEBUG = False
