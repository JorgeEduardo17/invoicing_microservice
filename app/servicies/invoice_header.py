from typing import List, Optional

from app.repositories.invoice_header import InvoiceHeaderRepository
from sqlalchemy.orm import Session

from app.models.invoice_header import InvoiceHeader
from app.schemas.invoice_header import InvoiceHeaderCreate  # InvoiceHeaderUpdate


class InvoiceHeaderService:
    """
    Service class for managing invoice header CRUD operations.

    Provides functionality to create, retrieve (both single and all entries), and delete
    invoice headers, abstracting the complexity of direct database interactions away
    from the client code.

    Attributes:
        db_session (Session): Database session for executing transactions.
        repository (InvoiceHeaderRepository): Repository handling the persistence operations of invoice headers.

    Methods:
        __init__(self, db_session: Session): Constructs an InvoiceHeaderService with the given database session.
        create_invoice_header(self, invoice_header_create: InvoiceHeaderCreate) -> InvoiceHeader: Creates a new invoice header.
        get_invoice_header(self, invoice_header_id: int) -> Optional[InvoiceHeader]: Retrieves an invoice header by its ID.
        get_all_invoice_headers(self) -> List[InvoiceHeader]: Retrieves all invoice headers.
        delete_invoice_header(self, invoice_header_id: int): Deletes an invoice header by its ID.
    """
    def __init__(self, db_session: Session):
        """
        Initializes the InvoiceHeaderService with a database session and a repository.

        Args:
            db_session (Session): The SQLAlchemy session for database transactions.
        """
        self.db_session = db_session
        self.repository = InvoiceHeaderRepository(db_session)

    def create_invoice_header(self, invoice_header_create: InvoiceHeaderCreate) -> InvoiceHeader:
        """
        Creates a new invoice header record in the database.

        Args:
            invoice_header_create (InvoiceHeaderCreate): The invoice header data transfer object containing
                                                         the necessary information to create a new invoice header.

        Returns:
            InvoiceHeader: The newly created invoice header entity.
        """
        return self.repository.create_invoice_header(invoice_header_create)

    def get_invoice_header(self, invoice_header_id: int) -> Optional[InvoiceHeader]:
        """
        Retrieves a single invoice header by its ID.

        Args:
            invoice_header_id (int): The unique identifier of the invoice header.

        Returns:
            Optional[InvoiceHeader]: The found invoice header entity or None if not found.
        """
        return self.repository.get_invoice_header(invoice_header_id)

    def get_all_invoice_headers(self) -> List[InvoiceHeader]:
        """
        Retrieves all invoice header records from the database.

        Returns:
            List[InvoiceHeader]: A list of all invoice header entities.
        """
        return self.repository.get_invoice_headers()

    def delete_invoice_header(self, invoice_header_id: int):
        """
        Deletes an invoice header record by its ID.

        Args:
            invoice_header_id (int): The unique identifier of the invoice header to be deleted.

        Returns:
            The result of the delete operation.
        """
        return self.repository.delete_invoice_header(invoice_header_id)

    # def update_invoice_header(self, invoice_header_id: int,
    #                           invoice_header_update: InvoiceHeaderUpdate) -> InvoiceHeader:
    #     return self.repository.update_invoice_header(invoice_header_id, invoice_header_update)
