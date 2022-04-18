from app.app import createApp
import pytest

@pytest.fixture()
def test_client():
    app = createApp()

    with app.test_client() as test_client:
        with app.app_context():
            yield test_client;