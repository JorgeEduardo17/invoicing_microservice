
from pydantic import BaseModel, Field
from typing import Optional


class InvoiceDetailBase(BaseModel):
    invoice_header_id: int
    product_id: int
    quantity: float


class InvoiceDetailCreate(InvoiceDetailBase):
    pass


# class InvoiceDetailUpdate(BaseModel):
#     invoice_header_id: Optional[int] = Field(None, description="The ID of the invoice header this detail belongs to")
#     product_id: Optional[int] = Field(None, description="The ID of the product")
#     quantity: Optional[float] = Field(None, description="The quantity of the product")
#
#     class Config:
#         from_attributes = True


class InvoiceDetail(InvoiceDetailBase):
    id: int

    class Config:
        from_attributes = True
