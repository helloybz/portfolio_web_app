from src.domain.service import (
    BadFormattedImageBytes,
    MNISTPredictionService,
    MNISTPreprocessingService,
)
from src.domain.vo import MNISTPrediction


class MNISTPredictionApplication:
    def __init__(
        self,
        mnist_preprocessing_service: MNISTPreprocessingService,
        mnist_prediction_service: MNISTPredictionService,
    ) -> None:
        self.mnist_preprocessing_service = mnist_preprocessing_service
        self.mnist_prediction_service = mnist_prediction_service

    def predict(
        self,
        image_bytes: bytes,
    ) -> MNISTPrediction:
        try:
            image = self.mnist_preprocessing_service.process_from_bytes(
                image_bytes=image_bytes,
            )
        except Exception as e:
            raise BadFormattedImageBytes(e) from e

        return self.mnist_prediction_service.do(
            image=image,
        )
