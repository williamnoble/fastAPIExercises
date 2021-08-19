import pytest
from starlette.testclient import TestClient

from async_api.app.main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client
