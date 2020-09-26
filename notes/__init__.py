import os
from pathlib import Path

from flask import Flask

from flask_bootstrap import Bootstrap

BASE_DIR = Path(__file__).parent #os.path.dirname(os.path.realpath(__file__))


def create_app(config=os.environ["APP_CONFIG"]):
    app = Flask(__name__)
    app.config.from_object(config)

    # Plugins
    Bootstrap(app)

    from notes.main import bp as main_bp

    app.register_blueprint(main_bp, url_prefix="")

    return app
