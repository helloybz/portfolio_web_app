from fastapi import APIRouter, FastAPI
from src.api.web.routers import default_router


def _build_router() -> APIRouter:
    router = APIRouter()

    router.include_router(default_router)

    return router


def create_web_app() -> FastAPI:
    app = FastAPI()
    router = _build_router()
    app.include_router(router)

    return app
