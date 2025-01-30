from src.domain.service import MNISTPredictionService, MNISTPreprocessingService
from src.domain.vo import MNISTImage, MNISTLabel, MNISTPrediction


def test_preprocessing_service_returns_mnist_image(
    fake_mnist_preprocessing_service: MNISTPreprocessingService,
) -> None:
    # When
    image = fake_mnist_preprocessing_service.process_from_bytes(b"")

    # Then
    assert isinstance(image, MNISTImage)


def test_prediction_service_returns_prediction(
    fake_mnist_prediction_service: MNISTPredictionService,
) -> None:
    # When
    prediction = fake_mnist_prediction_service.do(
        MNISTImage(pixels=[1] * (28 * 28), size=(28, 28), label=None)
    )

    # Then
    assert isinstance(prediction, MNISTPrediction)
