from fastapi.testclient import TestClient
import pytest

from src.domain.service import BadFormattedImageBytes


def test_mnist_classification_api_return_prediction(
    client: TestClient,
) -> None:
    with open("./tests/data/mnist_0.jpg", "rb") as io:
        image_bytes = io.read()

    response = client.post(
        url="/api/v1/mnist-prediction",
        files={"image": ("mnist_0.jpg", image_bytes, "image/jpeg")},
    )
    label = response.json().get("label")
    probability = response.json().get("probability")

    assert response.status_code == 200
    assert label is not None
    assert isinstance(label, int)
    assert probability is not None
    assert isinstance(probability, float)


def test_return_400_given_bad_formatted_image_bytes(
    client: TestClient,
) -> None:
    # Given
    bad_image_bytes_data = b"bad image bytes"

    # When
    response = client.post(
        url="/api/v1/mnist-prediction",
        files={"image": ("mnist_0.jpg", bad_image_bytes_data, "image/jpeg")},
    )

    # Then
    assert response.status_code == 400
    assert response.json().get("detail") == "Bad formatted image bytes"
