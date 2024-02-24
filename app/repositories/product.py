from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


class ProductRepository:
    """
    A repository class for managing CRUD operations on Product entities.

    This class abstracts the database interactions concerning products, offering methods to create,
    read, update, and delete products. It leverages SQLAlchemy for ORM capabilities and FastAPI's
    exception handling to provide informative error messages.

    Attributes:
        db (Session): An instance of `Session` from SQLAlchemy, representing the database session
                      for executing queries.

    Methods:
        __init__(self, db: Session): Initializes the repository with a database session.
        get_product_by_id(self, product_id: int) -> Product: Retrieves a product by its ID, raising
                                                             an HTTPException if not found.
        get_products(self, skip: int = 0, limit: int = 100) -> List[Product]: Fetches a list of products,
                                                                              supporting basic pagination.
        create_product(self, product: ProductCreate) -> Product: Creates a new product record in the database.
        update_product(self, product_id: int, product: ProductUpdate) -> Product: Updates an existing
                                                                                 product, identified by its ID.
        delete_product(self, product_id: int): Deletes a product by its ID, returning a confirmation upon success.
    """

    def __init__(self, db: Session):
        """
        Initializes the ProductRepository with a database session.

        Args:
            db (Session): The database session used to interact with the database.
        """
        self.db = db

    def get_product_by_id(self, product_id: int) -> Product:
        """
        Fetches a single product by its unique identifier.

        Args:
            product_id (int): The unique identifier of the product to be retrieved.

        Returns:
            The Product object if found.

        Raises:
            HTTPException: If no product with the specified ID was found.
        """
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    def get_products(self, skip: int = 0, limit: int = 100) -> List[Product]:
        """
        Retrieves a list of products, with support for pagination.

        Args:
            skip (int): The number of items to skip (for pagination).
            limit (int): The maximum number of items to return.

        Returns:
            A list of Product objects.
        """
        return self.db.query(Product).offset(skip).limit(limit).all()

    def create_product(self, product: ProductCreate) -> Product:
        """
        Creates a new product in the database.

        Args:
            product (ProductCreate): An instance of ProductCreate schema containing the product details.

        Returns:
            The newly created Product object.
        """
        db_product = Product(**product.dict())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def update_product(self, product_id: int, product: ProductUpdate) -> Product:
        """
        Updates an existing product's details.

        Args:
            product_id (int): The unique identifier of the product to be updated.
            product (ProductUpdate): An instance of ProductUpdate schema with the updated product details.

        Returns:
            The updated Product object.

        Raises:
            HTTPException: If the product to be updated is not found.
        """
        db_product = self.get_product_by_id(product_id)
        if not db_product:
            raise HTTPException(status_code=404, detail="Product not found")

        for var, value in vars(product).items():
            setattr(db_product, var, value) if value else None

        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def delete_product(self, product_id: int):
        """
        Deletes a product from the database by its ID.

        Args:
            product_id (int): The unique identifier of the product to be deleted.

        Returns:
            A confirmation message upon successful deletion.

        Raises:
            HTTPException: If the product to be deleted is not found.
        """
        db_product = self.get_product_by_id(product_id)
        if not db_product:
            raise HTTPException(status_code=404, detail="Product not found")
        self.db.delete(db_product)
        self.db.commit()
        return {"ok": True}
