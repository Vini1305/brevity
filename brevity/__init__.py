import logging
from flask import Flask
def create_app():
    app = Flask(__name__)

    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,  # or INFO for less noise
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    # Example: log startup
    app.logger.info("Brevity app initialized")

    from . import summary
    app.register_blueprint(summary.bp)

    from . import fetch_texts

    return app
