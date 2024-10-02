from contextlib import asynccontextmanager

from fastapi import FastAPI

from db_connect import create_tables, init_tables
from repository import UserGoodRepository
from schemas import UserGoodDto


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    init_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def health():
    return "OK"


@app.post("/users/goods/add", response_model=UserGoodDto)
def add_good(request: UserGoodDto):
    return UserGoodRepository.add_good_to_user(request)


@app.post("/users/goods/del", response_model=UserGoodDto)
def del_good(request: UserGoodDto):
    return UserGoodRepository.del_good_from_user(request)


@app.post("/users/goods/update", response_model=UserGoodDto)
def update_good(request: UserGoodDto):
    return UserGoodRepository.update_goods_user(request)
