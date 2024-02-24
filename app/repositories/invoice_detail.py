from sqlalchemy.orm import Session
from app.models.invoice_detail import InvoiceDetail
from app.schemas.invoice_detail import InvoiceDetailCreate #InvoiceDetailUpdate


class InvoiceDetailRepository:
    """
    Repository class for performing CRUD operations on InvoiceDetail entities.

    This class provides direct interaction with the database for querying, creating,
    and managing InvoiceDetail records. It abstracts away the complexities of direct
    database access from the service layer.

    Attributes:
        db (Session): Database session through which all database transactions are executed.

    Methods:
        __init__(self, db: Session): Initializes the repository with a database session.
        get_invoice_detail(self, id: int): Fetches a single InvoiceDetail by its ID.
        get_invoice_details(self, skip: int = 0, limit: int = 100): Retrieves a list of InvoiceDetails, with optional skipping and limit for pagination.
        create_invoice_detail(self, invoice_detail: InvoiceDetailCreate): Creates a new InvoiceDetail record in the database.
        delete_invoice_detail(self, id: int): Deletes an InvoiceDetail record from the database by its ID.
    """

    def __init__(self, db: Session):
        """
        Initialize the InvoiceDetailRepository with a database session.

        Args:
            db (Session): The database session used for executing database transactions.
        """
        self.db = db

    def get_invoice_detail(self, id: int):
        """
        Retrieves an invoice detail by its unique ID.

        Args:
            id (int): The unique identifier of the invoice detail.

        Returns:
            An instance of InvoiceDetail if found, else None.
        """
        return self.db.query(InvoiceDetail).filter(InvoiceDetail.id == id).first()

    def get_invoice_details(self, skip: int = 0, limit: int = 100):
        """
        Retrieves a list of invoice details, supports pagination through skip and limit parameters.

        Args:
            skip (int): Number of records to skip (for pagination).
            limit (int): Maximum number of records to return.

        Returns:
            A list of InvoiceDetail instances.
        """
        return self.db.query(InvoiceDetail).offset(skip).limit(limit).all()

    def create_invoice_detail(self, invoice_detail: InvoiceDetailCreate):
        """
        Creates a new invoice detail record in the database.

        Args:
            invoice_detail (InvoiceDetailCreate): The invoice detail data transfer object containing
                                                  the necessary information to create a new invoice detail.

        Returns:
            The newly created InvoiceDetail instance.
        """
        db_invoice_detail = InvoiceDetail(**invoice_detail.dict())
        self.db.add(db_invoice_detail)
        self.db.commit()
        self.db.refresh(db_invoice_detail)
        return db_invoice_detail

    def delete_invoice_detail(self, id: int):
        """
        Deletes an invoice detail record from the database.

        Args:
            id (int): The unique identifier of the invoice detail to be deleted.

        Returns:
            True if the deletion was successful, False otherwise.
        """
        db_invoice_detail = self.get_invoice_detail(id)
        if db_invoice_detail:
            self.db.delete(db_invoice_detail)
            self.db.commit()
            return True
        return False

    # def update_invoice_detail(self, id: int, invoice_detail: InvoiceDetailUpdate):
    #     db_invoice_detail = self.get_invoice_detail(id)
    #     if db_invoice_detail:
    #         update_data = invoice_detail.dict(exclude_unset=True)
    #         for key, value in update_data.items():
    #             setattr(db_invoice_detail, key, value)
    #         self.db.commit()
    #         self.db.refresh(db_invoice_detail)
    #         return db_invoice_detail
    #     return None


