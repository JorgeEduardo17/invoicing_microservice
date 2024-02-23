from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    description: str
    price: float
    cost: float
    unit_of_measure: str


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    description: Optional[str] = None
    price: Optional[float] = None
    cost: Optional[float] = None
    unit_of_measure: Optional[str] = None

    class Config:
        orm_mode = True


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
