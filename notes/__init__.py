import os

from flask import Flask

from flask_bootstrap import Bootstrap


def create_app(config=os.environ["APP_CONFIG"]):
    app = Flask(__name__)
    app.config.from_object(config)

    # Plugins
    Bootstrap(app)

    from notes.main import bp as main_bp

    app.register_blueprint(main_bp, url_prefix="")

    return app
