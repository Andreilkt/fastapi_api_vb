from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declarative_base
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


engine = create_async_engine("sqlite+aiosqlite:///vb.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class Product_vb(Model):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str]
    Article: Mapped[int]
    Price: Mapped[float]
    Product_rating: Mapped[int]
    Total_quantity: Mapped[int]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
