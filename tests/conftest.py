from pytest import fixture

from src.domain.service import MNISTPredictionService, MNISTPreprocessingService
from src.domain.vo import MNISTImage, MNISTLabel, MNISTPrediction


@fixture
def sample_mnist_image_bytes() -> bytes:
    with open("tests/data/mnist_0.jpg", "rb") as io:
        bytes = io.read()

    return bytes


@fixture
def fake_mnist_preprocessing_service() -> MNISTPreprocessingService:
    class FakeMNISTPreprocessingService(MNISTPreprocessingService):
        def _proccess_from_bytes(
            self,
            image_bytes: bytes,
        ) -> MNISTImage:
            if image_bytes == b"bad image bytes":
                raise Exception("Bad formatted image bytes")
            return MNISTImage(pixels=[1] * (28 * 28), size=(28, 28), label=None)

    return FakeMNISTPreprocessingService()


@fixture
def fake_mnist_prediction_service() -> MNISTPredictionService:
    class FakeMNISTPredictionService(MNISTPredictionService):
        def do(
            self,
            image: MNISTImage,
        ) -> MNISTPrediction:
            return MNISTPrediction(predicted_label=MNISTLabel.ZERO, probability=0.5)

    return FakeMNISTPredictionService()
