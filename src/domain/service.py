from abc import ABC, abstractmethod

from src.domain.vo import MNISTImage, MNISTPrediction


class BadFormattedImageBytes(Exception): ...


class MNISTPreprocessingService(ABC):
    def process_from_bytes(
        self,
        image_bytes: bytes,
    ) -> MNISTImage:
        try:
            return self._proccess_from_bytes(
                image_bytes=image_bytes,
            )
        except Exception as e:
            raise BadFormattedImageBytes(e) from e

    @abstractmethod
    def _proccess_from_bytes(
        self,
        image_bytes: bytes,
    ) -> MNISTImage:
        raise NotImplementedError


class MNISTPredictionService(ABC):
    @abstractmethod
    def do(
        self,
        image: MNISTImage,
    ) -> MNISTPrediction:
        raise NotImplementedError
