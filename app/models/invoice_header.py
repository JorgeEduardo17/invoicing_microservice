from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.postgresql import Base


class InvoiceHeader(Base):
    __tablename__ = 'invoice_headers'
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True)
    date = Column(Date)
    person_id = Column(Integer, ForeignKey('person.id'))

    # Relationships
    person = relationship("Person", back_populates="invoices")
    details = relationship("InvoiceDetail", back_populates="invoice_header")
