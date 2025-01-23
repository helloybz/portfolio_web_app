from fastapi.testclient import TestClient


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
