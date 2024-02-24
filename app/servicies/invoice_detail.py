from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.invoice_detail import InvoiceDetail
from app.repositories.invoice_detail import InvoiceDetailRepository
from app.schemas.invoice_detail import InvoiceDetailCreate  # InvoiceDetailUpdate


class InvoiceDetailService:
    """
    Service for handling CRUD operations for invoice details.

    This service uses an invoice detail repository to perform database operations,
    abstracting away the specific implementation details of the repository used.

    Attributes:
        db_session (Session): Database session for executing transactions.
        repository (InvoiceDetailRepository): Repository handling the persistence operations of invoice detail.

    Methods:
        __init__(self, db_session: Session): Initializes the service with a database session.
        create_invoice_detail(self, invoice_detail_create: InvoiceDetailCreate) -> InvoiceDetail: Creates a new invoice detail.
        get_invoice_detail(self, invoice_detail_id: int) -> Optional[InvoiceDetail]: Retrieves an invoice detail by its ID.
        get_all_invoice_details(self) -> List[InvoiceDetail]: Retrieves all invoice details.
        delete_invoice_detail(self, invoice_detail_id: int): Deletes an invoice detail by its ID.
    """

    def __init__(self, db_session: Session):
        """
            Initializes the invoice detail service with a database session and a repository.

            Args:
                db_session (Session): The SQLAlchemy session for interacting with the database.
            """
        self.db_session = db_session
        self.repository = InvoiceDetailRepository(db_session)

    def create_invoice_detail(self, invoice_detail_create: InvoiceDetailCreate) -> InvoiceDetail:
        """
        Creates a new invoice detail in the database.

        Args:
            invoice_detail_create (InvoiceDetailCreate): The data needed to create a new invoice detail.

        Returns:
            InvoiceDetail: The created invoice detail instance.
        """
        return self.repository.create_invoice_detail(invoice_detail_create)

    def get_invoice_detail(self, invoice_detail_id: int) -> Optional[InvoiceDetail]:
        """
        Retrieves an invoice detail by its ID.

        Args:
            invoice_detail_id (int): The ID of the invoice detail to retrieve.

        Returns:
            Optional[InvoiceDetail]: The invoice detail instance if found, otherwise None.
        """
        return self.repository.get_invoice_detail(invoice_detail_id)

    def get_all_invoice_details(self) -> List[InvoiceDetail]:
        """
        Retrieves all existing invoice details.

        Returns:
            List[InvoiceDetail]: A list of all invoice details.
        """
        return self.repository.get_invoice_details()

    def delete_invoice_detail(self, invoice_detail_id: int):
        """
        Deletes an invoice detail by its ID.

        Args:
            invoice_detail_id (int): The ID of the invoice detail to delete.

        Returns:
            The result of the delete operation.
        """
        return self.repository.delete_invoice_detail(invoice_detail_id)

    # def update_invoice_detail(self, invoice_detail_id: int,
    #                           invoice_detail_update: InvoiceDetailUpdate) -> InvoiceDetail:
    #     return self.repository.update_invoice_detail(invoice_detail_id, invoice_detail_update)

