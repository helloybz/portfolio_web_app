from fastapi.testclient import TestClient
from pytest import fixture

from src.api.web.app import create_web_app


@fixture
def client() -> TestClient:
    app = create_web_app()
    return TestClient(app)
