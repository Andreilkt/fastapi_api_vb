from fastapi import APIRouter, Depends

from database import Product_vb
from repository import ProductRepository
from schemas import Product, ProductId, ProductAdd

from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from schemas import ProductAdd, Product, ProductId

router_front = APIRouter(prefix='/product_front', tags=['Фронтенд'])
templates = Jinja2Templates(directory='templates')


# @router_front.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse("pages/index.html",
#                                       {"request": request, })

@router_front.post(
    "/",
    description="Добавляет товар в базу_1",
    summary="Добавляет товар в базу данных",
    response_description="Ответ",
)
async def add_product(product: ProductAdd = Depends()) -> ProductId:
    new_product_id = await ProductRepository.add_product(product)
    return {"id": new_product_id}


@router_front.get("/")
async def product_front(request: Request) -> list[Product]:
    product = await ProductRepository.get_products()
    return templates.TemplateResponse("pages/product.html", {"request": request, }, product=product)


@router_front.get("/front")
async def get_products_front() -> list[Product]:
    prod = await ProductRepository.get_products()
    return prod


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
