from fastapi import APIRouter, Depends

from repository import ProductRepository
from schemas import Product, ProductId, ProductAdd

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


