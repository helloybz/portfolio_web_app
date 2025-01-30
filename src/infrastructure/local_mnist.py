from src.domain.service import MNISTPredictionService, MNISTPreprocessingService
from src.domain.vo import MNISTImage, MNISTLabel, MNISTPrediction


class LocalMNISTPreprocessingService(MNISTPreprocessingService):
    def _proccess_from_bytes(
        self,
        image_bytes: bytes,
    ) -> MNISTImage:
        return MNISTImage(pixels=[1] * (28 * 28), size=(28, 28), label=None)


class LocalMNISTPredictionService(MNISTPredictionService):
    def do(
        self,
        image: MNISTImage,
    ) -> MNISTPrediction:
        return MNISTPrediction(predicted_label=MNISTLabel.ZERO, probability=0.5)
