from typing import Optional

from pydantic import BaseModel


class PersonBase(BaseModel):
    name: str
    surname: str
    document_type: str
    document: str


class PersonCreate(PersonBase):
    pass


class PersonUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    document_type: Optional[str] = None
    document: Optional[str] = None

    class Config:
        from_attributes = True


class Person(PersonBase):
    id: int

    class Config:
        from_attributes = True
