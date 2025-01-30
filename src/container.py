from dependency_injector import containers, providers

from src.application.mnist import MNISTPredictionApplication
from src.infrastructure.local_mnist import (
    LocalMNISTPredictionService,
    LocalMNISTPreprocessingService,
)


class ServiceContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    mnist_preprocessing_service = providers.Selector(
        config.service.mnist_preprocessing.infra,
        null=providers.Object(),
        local=providers.Singleton(LocalMNISTPreprocessingService),
    )
    mnist_prediction_service = providers.Selector(
        config.service.mnist_prediction.infra,
        null=providers.Object(),
        local=providers.Singleton(LocalMNISTPredictionService),
    )


class ApplicationContainer(containers.DeclarativeContainer):
    service_container = providers.DependenciesContainer()

    mnist_prediction_app = providers.Singleton(
        MNISTPredictionApplication,
        mnist_preprocessing_service=service_container.mnist_preprocessing_service,
        mnist_prediction_service=service_container.mnist_prediction_service,
    )


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    service = providers.Container(
        ServiceContainer,
        config=config,
    )

    application = providers.Container(
        ApplicationContainer,
        service_container=service,
    )
