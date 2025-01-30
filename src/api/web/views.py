from typing import Self
from pydantic import BaseModel

from src.domain.vo import MNISTLabel, MNISTPrediction


class MNISTPredictionResponseView(BaseModel):
    label: MNISTLabel
    probability: float

    @classmethod
    def from_prediction(cls, prediction: MNISTPrediction) -> Self:
        return cls(
            label=prediction.predicted_label,
            probability=prediction.probability,
        )
