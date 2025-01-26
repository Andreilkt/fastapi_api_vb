from sqlalchemy import select
from database import Product_vb, new_session
from schemas import ProductAdd, Product


class ProductRepository:
    @classmethod
    async def add_product(cls, product: ProductAdd) -> int:
        async with new_session() as session:
            data = product.model_dump()
            new_product = Product_vb(**data)

            session.add(new_product)
            await session.flush()
            await session.commit()
            return new_product.id

    @classmethod
    async def get_products(cls) -> list[Product]:
        async with new_session() as session:
            query = select(Product_vb)
            result = await session.execute(query)
            product_models = result.scalars().all()
            product = [Product.model_validate(product_model) for product_model in product_models]
            return product
