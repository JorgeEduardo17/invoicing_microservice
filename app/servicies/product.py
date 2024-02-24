from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.product import Product
from app.repositories.product import ProductRepository
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:
    """
    Service class for managing CRUD operations for Product entities.

    Provides methods to create, retrieve (both single product and all products), update,
    and delete products. This abstraction layer simplifies interactions with the database
    for product-related operations, ensuring that clients do not need to directly manage
    database transactions.

    Attributes:
        db_session (Session): Database session for executing transactions.
        repository (ProductRepository): Repository handling the persistence operations of Product entities.

    Methods:
        __init__(self, db_session: Session): Constructs a ProductService with the given database session.
        create_product(self, product_create: ProductCreate) -> Product: Creates a new Product entity.
        get_product(self, product_id: int) -> Optional[Product]: Retrieves a Product entity by its ID.
        get_all_products(self) -> List[Product]: Retrieves all Product entities.
        update_product(self, product_id: int, product_update: ProductUpdate) -> Product: Updates an existing Product entity.
        delete_product(self, product_id: int): Deletes a Product entity by its ID.
    """

    def __init__(self, db_session: Session):
        """
        Initializes the ProductService with a database session and a repository.

        Args:
            db_session (Session): The SQLAlchemy session for database transactions.
        """
        self.db_session = db_session
        self.repository = ProductRepository(db_session)

    def create_product(self, product_create: ProductCreate) -> Product:
        """
        Creates a new Product record in the database.

        Args:
            product_create (ProductCreate): The Product data transfer object containing
                                            the necessary information to create a new Product.

        Returns:
            Product: The newly created Product entity.
        """
        return self.repository.create_product(product_create)

    def get_product(self, product_id: int) -> Optional[Product]:
        """
        Retrieves a single Product entity by its ID.

        Args:
            product_id (int): The unique identifier of the Product.

        Returns:
            Optional[Product]: The found Product entity or None if not found.
        """
        return self.repository.get_product_by_id(product_id)

    def get_all_products(self) -> List[Product]:
        """
        Retrieves all Product entities from the database.

        Returns:
            List[Product]: A list of all Product entities.
        """
        return self.repository.get_products()

    def update_product(self, product_id: int, product_update: ProductUpdate) -> Product:
        """
        Updates an existing Product record in the database.

        Args:
            product_id (int): The unique identifier of the Product to be updated.
            product_update (ProductUpdate): The Product data transfer object containing
                                            the updated information for the Product.

        Returns:
            Product: The updated Product entity.
        """
        return self.repository.update_product(product_id, product_update)

    def delete_product(self, product_id: int):
        """
        Deletes a Product record by its ID.

        Args:
            product_id (int): The unique identifier of the Product to be deleted.

        Returns:
            The result of the delete operation.
        """
        return self.repository.delete_product(product_id)
