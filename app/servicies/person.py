from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.person import Person
from app.repositories.person import PersonRepository
from app.schemas.person import PersonCreate, PersonUpdate


class PersonService:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.repository = PersonRepository(db_session)

    def create_person(self, person_create: PersonCreate) -> Person:
        return self.repository.create_person(person_create)

    def get_person(self, person_id: int) -> Optional[Person]:
        return self.repository.get_person_by_id(person_id)

    def get_all_persons(self) -> List[Person]:
        return self.repository.get_all_persons()

    def update_person(self, person_id: int, person_update: PersonUpdate) -> Person:
        return self.repository.update_person(person_id, person_update)

    def delete_person(self, person_id: int):
        return self.repository.delete_person(person_id)
