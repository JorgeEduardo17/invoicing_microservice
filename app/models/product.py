from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.db.postgresql import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    price = Column(Float)
    cost = Column(Float)
    unit_of_measure = Column(String)

    # Relationships
    invoice_details = relationship("InvoiceDetail", back_populates="product")
