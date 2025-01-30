from enum import IntEnum

import msgspec


class MNISTLabel(IntEnum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9


class MNISTImage(msgspec.Struct):
    pixels: list[int]
    size: tuple[int, int]
    label: MNISTLabel | None = None


class MNISTPrediction(msgspec.Struct):
    predicted_label: MNISTLabel
    probability: float
