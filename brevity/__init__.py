
from flask import Flask
def create_app():
    app = Flask(__name__)

    from . import summary
    app.register_blueprint(summary.bp)

    from . import fetch_texts

    return app
