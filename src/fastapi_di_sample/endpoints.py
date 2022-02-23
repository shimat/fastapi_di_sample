from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from .containers import Container
from .services import MyService

router = APIRouter()


class MyResponse(BaseModel):
    is_ok: bool


@router.get("/", response_model=MyResponse)
@inject
def read_root(
    word: str,
    search_service: MyService = Depends(Provide[Container.my_service]),
):
    result = search_service.run(word)
    return MyResponse(is_ok=result)
