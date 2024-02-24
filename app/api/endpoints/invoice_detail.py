from typing import List

from app.db.postgresql import get_db
from app.servicies.invoice_detail import InvoiceDetailService
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import Response
from sqlalchemy.orm import Session

from app.schemas.invoice_detail import InvoiceDetailCreate, InvoiceDetail #InvoiceDetailUpdate

router = APIRouter()


def get_invoice_detail_service(db: Session = Depends(get_db)):
    return InvoiceDetailService(db_session=db)


@router.post("/", response_model=InvoiceDetail, status_code=status.HTTP_201_CREATED)
def create_invoice_detail(invoice_detail_create: InvoiceDetailCreate,
                          service: InvoiceDetailService = Depends(get_invoice_detail_service)):
    return service.create_invoice_detail(invoice_detail_create)


@router.get("/{invoice_detail_id}", response_model=InvoiceDetail)
def read_invoice_detail(invoice_detail_id: int, service: InvoiceDetailService = Depends(get_invoice_detail_service)):
    invoice_detail = service.get_invoice_detail(invoice_detail_id)
    if invoice_detail is None:
        raise HTTPException(status_code=404, detail="InvoiceDetail not found")
    return invoice_detail


@router.get("/", response_model=List[InvoiceDetail])
def read_invoice_details(service: InvoiceDetailService = Depends(get_invoice_detail_service)):
    return service.get_all_invoice_details()


# @router.put("/{invoice_detail_id}", response_model=InvoiceDetail)
# def update_invoice_detail(invoice_detail_id: int, invoice_detail_update: InvoiceDetailUpdate,
#                           service: InvoiceDetailService = Depends(get_invoice_detail_service)):
#     return service.update_invoice_detail(invoice_detail_id, invoice_detail_update)


@router.delete("/{invoice_detail_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_invoice_detail(invoice_detail_id: int, service: InvoiceDetailService = Depends(get_invoice_detail_service)):
    service.delete_invoice_detail(invoice_detail_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
