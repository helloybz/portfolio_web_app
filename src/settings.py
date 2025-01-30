from enum import StrEnum, auto
from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Infrastructure(StrEnum):
    LOCAL = auto()
    NULL = auto()


class MnistPreprocessingSettings(BaseModel):
    infra: Infrastructure


class MnistPredictionSettings(BaseModel):
    infra: Infrastructure


class ServiceSettings(BaseModel):
    mnist_preprocessing: MnistPreprocessingSettings
    mnist_prediction: MnistPredictionSettings


class Settings(BaseSettings):
    service: ServiceSettings

    model_config = SettingsConfigDict(
        env_file=Path(".env"),
        env_prefix="PORTFOLIO_",
        env_nested_delimiter="__",
        env_ignore_empty=True,
    )
