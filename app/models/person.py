from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.postgresql import Base


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    document_type = Column(String)
    document = Column(String)

    # Relationships
    invoices = relationship("InvoiceHeader", back_populates="person")
