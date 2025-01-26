from fastapi import APIRouter, Depends

from repository import ProductRepository
from schemas import Product, ProductId, ProductAdd

from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

router_front = APIRouter(prefix='', tags=['Фронтенд'])
templates = Jinja2Templates(directory='templates')

@router_front.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("pages/index.html",
                                      {"request": request})


router = APIRouter(
    prefix="/products",
    tags=["Продукты"],
)


@router.post(
    "/",
    description="Добавляет товар в базу_1",
    summary="Добавляет товар в базу данных",
    response_description="Ответ",
)
async def add_product(product: ProductAdd = Depends()) -> ProductId:
    new_product_id = await ProductRepository.add_product(product)
    return {"id": new_product_id}


@router.get("/")
async def get_products() -> list[Product]:
    prod = await ProductRepository.get_products()
    return prod


