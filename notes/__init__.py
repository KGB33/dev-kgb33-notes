import os

from flask import Flask



def create_app(config=os.environ["APP_CONFIG"]):
    app = Flask(__name__)
    app.config.from_object(config)

    from notes.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='')

    return app
