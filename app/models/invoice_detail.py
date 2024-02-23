from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db.postgresql import Base


class InvoiceDetail(Base):
    __tablename__ = 'invoice_details'
    id = Column(Integer, primary_key=True, index=True)
    invoice_header_id = Column(Integer, ForeignKey('invoice_headers.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Float)

    # Relationships
    invoice_header = relationship("InvoiceHeader", back_populates="details")
    product = relationship("Product", back_populates="invoice_details")
