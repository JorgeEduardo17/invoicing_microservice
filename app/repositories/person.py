from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.person import Person
from app.schemas.person import PersonCreate, PersonUpdate


class PersonRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_person_by_id(self, person_id: int) -> Person:
        return self.db.query(Person).filter(Person.id == person_id).first()

    def get_all_persons(self, skip: int = 0, limit: int = 100) -> List[Person]:
        return self.db.query(Person).offset(skip).limit(limit).all()

    def create_person(self, person: PersonCreate) -> Person:
        db_person = Person(**person.dict())
        self.db.add(db_person)
        self.db.commit()
        self.db.refresh(db_person)
        return db_person

    def update_person(self, person_id: int, person: PersonUpdate) -> Person:
        db_person = self.get_person_by_id(person_id)
        if not db_person:
            raise HTTPException(status_code=404, detail="Person not found")
        for var, value in vars(person).items():
            setattr(db_person, var, value) if value else None
        self.db.commit()
        self.db.refresh(db_person)
        return db_person

    def delete_person(self, person_id: int):
        db_person = self.get_person_by_id(person_id)
        if not db_person:
            raise HTTPException(status_code=404, detail="Person not found")
        self.db.delete(db_person)
        self.db.commit()
        return {"ok": True}
