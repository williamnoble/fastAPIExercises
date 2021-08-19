import starlette.responses
from requests import Response
from starlette.testclient import TestClient

from async_api.app.main import app

client = TestClient(app)


def test_ping(test_app):
    response: Response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}
