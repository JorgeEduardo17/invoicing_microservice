from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional
from app.schemas.invoice_detail import InvoiceDetail


class InvoiceHeaderBase(BaseModel):
    number: int
    date: date


class InvoiceHeaderCreate(InvoiceHeaderBase):
    person_id: int


# class InvoiceHeaderUpdate(BaseModel):
#     number: Optional[int] = Field(None, description="The invoice number")
#     date: Optional[date] = Field(None, description="The invoice date")
#     person_id: Optional[int] = Field(None, description="The customer ID associated with the invoice")
#
#     class Config:
#         from_attributes = True


class InvoiceHeader(InvoiceHeaderBase):
    id: int
    person_id: int
    details: List[InvoiceDetail] = []

    class Config:
        from_attributes = True
