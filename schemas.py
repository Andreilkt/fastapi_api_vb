from pydantic import BaseModel, ConfigDict


class ProductAdd(BaseModel):
    product_name: str
    Article: int
    Price: float
    Product_rating: int
    Total_quantity: int


class Product(ProductAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ProductId(BaseModel):
    id: int
