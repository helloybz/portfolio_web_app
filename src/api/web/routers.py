from fastapi import APIRouter, UploadFile
from loguru import logger
from pydantic import BaseModel
from src.api.web.views import (
    MNISTLabel,
    MNISTPredictionResponseView,
)


class Status(BaseModel):
    status: str = "OK"


default_router: APIRouter = APIRouter()


@default_router.get("/", response_model=Status)
@default_router.get("/healthz", response_model=Status)
@default_router.get("/readyz", response_model=Status)
@default_router.get("/livez", response_model=Status)
async def health() -> Status:
    return Status()


service_router: APIRouter = APIRouter()


@service_router.post("/v1/mnist-prediction")
async def mnist_predict_v1(
    image: UploadFile,
) -> MNISTPredictionResponseView:
    logger.info(image)
    return MNISTPredictionResponseView(
        label=MNISTLabel.ZERO,
        probability=0.5,
    )
