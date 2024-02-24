from sqlalchemy.orm import Session
from app.models.invoice_header import InvoiceHeader
from app.schemas.invoice_header import InvoiceHeaderCreate # InvoiceHeaderUpdate


class InvoiceHeaderRepository:
    """
    Repository class for performing CRUD operations on InvoiceHeader entities.

    Handles direct interactions with the database for creating, querying, and deleting
    InvoiceHeader records. Provides a layer of abstraction between the database session
    and the service layer, ensuring that database queries are centralized and manageable.

    Attributes:
        db (Session): Database session for executing database transactions.

    Methods:
        __init__(self, db: Session): Constructs the InvoiceHeaderRepository with a database session.
        get_invoice_header(self, id: int): Retrieves a single InvoiceHeader by its ID.
        get_invoice_headers(self, skip: int = 0, limit: int = 100): Fetches a list of InvoiceHeaders, supports pagination.
        create_invoice_header(self, invoice_header: InvoiceHeaderCreate): Creates a new InvoiceHeader record.
        delete_invoice_header(self, id: int): Removes an InvoiceHeader record from the database.
    """

    def __init__(self, db: Session):
        """
        Initializes the repository with a given database session for transactions.

        Args:
            db (Session): The database session used for transactional operations.
        """
        self.db = db

    def get_invoice_header(self, id: int):
        """
        Fetches an InvoiceHeader entity based on its ID.

        Args:
            id (int): The unique identifier of the InvoiceHeader.

        Returns:
            The InvoiceHeader entity if found, otherwise None.
        """
        return self.db.query(InvoiceHeader).filter(InvoiceHeader.id == id).first()

    def get_invoice_headers(self, skip: int = 0, limit: int = 100):
        """
        Retrieves a list of InvoiceHeader entities, with optional pagination.

        Args:
            skip (int): The number of records to skip from the start.
            limit (int): The maximum number of records to return.

        Returns:
            A list of InvoiceHeader entities.
        """
        return self.db.query(InvoiceHeader).offset(skip).limit(limit).all()

    def create_invoice_header(self, invoice_header: InvoiceHeaderCreate):
        """
        Creates a new InvoiceHeader record in the database.

        Args:
            invoice_header (InvoiceHeaderCreate): An instance containing all required data for creating a new InvoiceHeader.

        Returns:
            The newly created InvoiceHeader entity.
        """
        db_invoice_header = InvoiceHeader(**invoice_header.dict())
        self.db.add(db_invoice_header)
        self.db.commit()
        self.db.refresh(db_invoice_header)
        return db_invoice_header

    def delete_invoice_header(self, id: int):
        """
        Deletes an InvoiceHeader record identified by its ID.

        Args:
            id (int): The unique identifier of the InvoiceHeader to delete.

        Returns:
            True if the deletion was successful, False otherwise.
        """
        db_invoice_header = self.get_invoice_header(id)
        if db_invoice_header:
            self.db.delete(db_invoice_header)
            self.db.commit()
            return True
        return False

    # def update_invoice_header(self, id: int, invoice_header: InvoiceHeaderUpdate):
    #     db_invoice_header = self.get_invoice_header(id)
    #     if db_invoice_header:
    #         update_data = invoice_header.dict(exclude_unset=True)
    #         for key, value in update_data.items():
    #             setattr(db_invoice_header, key, value)
    #         self.db.commit()
    #         self.db.refresh(db_invoice_header)
    #         return db_invoice_header
    #     return None
