from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables, delete_tables
from router import router as product_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База создана")
    yield
    await delete_tables()
    print("База очищена")


app = FastAPI(lifespan=lifespan)

app.include_router(product_router)
