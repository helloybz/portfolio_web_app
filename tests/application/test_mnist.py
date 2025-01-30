import pytest
from src.application.mnist import MNISTPredictionApplication
from src.domain.service import (
    BadFormattedImageBytes,
    MNISTPredictionService,
    MNISTPreprocessingService,
)
from src.domain.vo import MNISTPrediction


def test_mnist_application_returns_prediction_for_valid_image(
    fake_mnist_preprocessing_service: MNISTPreprocessingService,
    fake_mnist_prediction_service: MNISTPredictionService,
    sample_mnist_image_bytes: bytes,
) -> None:
    # Given
    mnist_app = MNISTPredictionApplication(
        mnist_preprocessing_service=fake_mnist_preprocessing_service,
        mnist_prediction_service=fake_mnist_prediction_service,
    )
    valid_image_bytes = sample_mnist_image_bytes

    # When
    prediction = mnist_app.predict(image_bytes=valid_image_bytes)

    # Then
    assert isinstance(prediction, MNISTPrediction)


def test_mnist_application_raise_exception_given_malformed_image(
    fake_mnist_preprocessing_service: MNISTPreprocessingService,
    fake_mnist_prediction_service: MNISTPredictionService,
) -> None:
    # Given
    mnist_app = MNISTPredictionApplication(
        mnist_preprocessing_service=fake_mnist_preprocessing_service,
        mnist_prediction_service=fake_mnist_prediction_service,
    )
    bad_image_bytes = b"bad image bytes"

    # When & Then
    with pytest.raises(BadFormattedImageBytes) as e:
        mnist_app.predict(image_bytes=bad_image_bytes)
