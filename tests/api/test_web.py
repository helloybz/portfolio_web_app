from fastapi.testclient import TestClient
import pytest


@pytest.mark.parametrize("url", ["/", "/healthz", "/readyz", "/livez"])
def test_health(
    client: TestClient,
    url: str,
) -> None:
    response = client.get(url)
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
