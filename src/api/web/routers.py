from fastapi import APIRouter, Depends, HTTPException, UploadFile
from loguru import logger
from pydantic import BaseModel
from src.api.web.views import MNISTPredictionResponseView
from src.application.mnist import MNISTPredictionApplication
from src.container import Container
from src.domain.service import BadFormattedImageBytes

from dependency_injector.wiring import Provide, inject


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
@inject
async def mnist_predict_v1(
    image: UploadFile,
    app: MNISTPredictionApplication = Depends(
        Provide[Container.application.mnist_prediction_app]
    ),
) -> MNISTPredictionResponseView:
    logger.info(image)
    try:
        prediction = app.predict(
            image_bytes=await image.read(),
        )
    except BadFormattedImageBytes as e:
        logger.error(e)
        raise HTTPException(
            status_code=400,
            detail="Bad formatted image bytes",
        ) from e
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=500,
            detail="Internal server error",
        ) from e

    return MNISTPredictionResponseView.from_prediction(
        prediction=prediction,
    )
