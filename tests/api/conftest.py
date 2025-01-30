from pathlib import Path
from fastapi.testclient import TestClient
from pytest import fixture

from src.api.web import routers
from src.api.web.app import create_web_app
from src.container import Container
from src.domain.service import MNISTPredictionService, MNISTPreprocessingService
from src.settings import Settings


@fixture
def client(
    fake_mnist_preprocessing_service: MNISTPreprocessingService,
    fake_mnist_prediction_service: MNISTPredictionService,
) -> TestClient:
    app = create_web_app()

    container = Container()
    settings = Settings(
        _env_file=Path(".env.test"),
        _env_prefix="PORTFOLIO_",
    )
    container.config.from_pydantic(settings)
    container.service.mnist_preprocessing_service.override(
        fake_mnist_preprocessing_service
    )
    container.service.mnist_prediction_service.override(fake_mnist_prediction_service)

    container.wire(modules=[routers])

    return TestClient(app)
