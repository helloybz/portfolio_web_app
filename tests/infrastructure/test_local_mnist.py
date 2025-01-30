from src.domain.vo import MNISTImage, MNISTLabel
from src.infrastructure.local_mnist import (
    LocalMNISTPredictionService,
    LocalMNISTPreprocessingService,
)


def test_preprocessing_service_returns_dummy_image():
    # Given
    service = LocalMNISTPreprocessingService()

    # When
    image = service.process_from_bytes(b"")

    # Then
    assert image.pixels == [1] * (28 * 28)
    assert image.size == (28, 28)
    assert image.label is None


def test_prediction_service_returns_dummy_prediction():
    # Given
    service = LocalMNISTPredictionService()

    # When
    prediction = service.do(
        MNISTImage(pixels=[1] * (28 * 28), size=(28, 28), label=None)
    )

    # Then
    assert prediction.predicted_label == MNISTLabel.ZERO
    assert prediction.probability == 0.5
