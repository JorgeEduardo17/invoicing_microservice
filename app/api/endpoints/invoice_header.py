from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import Response
from sqlalchemy.orm import Session

from app.db.postgresql import get_db
from app.schemas.invoice_header import InvoiceHeaderCreate, InvoiceHeader  #InvoiceHeaderUpdate
from app.servicies.invoice_header import InvoiceHeaderService

router = APIRouter()


def get_invoice_header_service(db: Session = Depends(get_db)):
    return InvoiceHeaderService(db_session=db)


@router.post("/", response_model=InvoiceHeader, status_code=status.HTTP_201_CREATED)
def create_invoice_header(invoice_header_create: InvoiceHeaderCreate,
                          service: InvoiceHeaderService = Depends(get_invoice_header_service)):
    return service.create_invoice_header(invoice_header_create)


@router.get("/{invoice_header_id}", response_model=InvoiceHeader)
def read_invoice_header(invoice_header_id: int, service: InvoiceHeaderService = Depends(get_invoice_header_service)):
    invoice_header = service.get_invoice_header(invoice_header_id)
    if invoice_header is None:
        raise HTTPException(status_code=404, detail="InvoiceHeader not found")
    return invoice_header


@router.get("/", response_model=List[InvoiceHeader])
def read_invoice_headers(service: InvoiceHeaderService = Depends(get_invoice_header_service)):
    return service.get_all_invoice_headers()


# @router.put("/{invoice_header_id}", response_model=InvoiceHeader)
# def update_invoice_header(invoice_header_id: int, invoice_header_update: InvoiceHeaderUpdate,
#                           service: InvoiceHeaderService = Depends(get_invoice_header_service)):
#     return service.update_invoice_header(invoice_header_id, invoice_header_update)


@router.delete("/{invoice_header_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_invoice_header(invoice_header_id: int, service: InvoiceHeaderService = Depends(get_invoice_header_service)):
    service.delete_invoice_header(invoice_header_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
