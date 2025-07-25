import sys, os
import pytest

# Ensure project root is in Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from brevity import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True  # Flask test mode
    with app.test_client() as client:
        yield client
