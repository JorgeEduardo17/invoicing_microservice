from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.product import Product
from app.repositories.product import ProductRepository
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.repository = ProductRepository(db_session)

    def create_product(self, product_create: ProductCreate) -> Product:
        return self.repository.create_product(product_create)

    def get_product(self, product_id: int) -> Optional[Product]:
        return self.repository.get_product_by_id(product_id)

    def get_all_products(self) -> List[Product]:
        return self.repository.get_products()

    def update_product(self, product_id: int, product_update: ProductUpdate) -> Product:
        return self.repository.update_product(product_id, product_update)

    def delete_product(self, product_id: int):
        return self.repository.delete_product(product_id)
