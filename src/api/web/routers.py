from fastapi import APIRouter
from pydantic import BaseModel


default_router: APIRouter = APIRouter()


class Status(BaseModel):
    status: str = "OK"


@default_router.get("/", response_model=Status)
@default_router.get("/healthz", response_model=Status)
@default_router.get("/readyz", response_model=Status)
@default_router.get("/livez", response_model=Status)
async def health() -> Status:
    return Status()
