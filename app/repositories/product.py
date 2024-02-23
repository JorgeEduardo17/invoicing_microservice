from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_product_by_id(self, product_id: int) -> Product:
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    def get_products(self, skip: int = 0, limit: int = 100) -> List[Product]:
        return self.db.query(Product).offset(skip).limit(limit).all()

    def create_product(self, product: ProductCreate) -> Product:
        db_product = Product(**product.dict())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def update_product(self, product_id: int, product: ProductUpdate) -> Product:
        db_product = self.get_product_by_id(product_id)
        if not db_product:
            raise HTTPException(status_code=404, detail="Product not found")

        for var, value in vars(product).items():
            setattr(db_product, var, value) if value else None

        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def delete_product(self, product_id: int):
        db_product = self.get_product_by_id(product_id)
        if not db_product:
            raise HTTPException(status_code=404, detail="Product not found")
        self.db.delete(db_product)
        self.db.commit()
        return {"ok": True}
