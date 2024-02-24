from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.person import Person
from app.schemas.person import PersonCreate, PersonUpdate


class PersonRepository:
    """
    Repository class for performing CRUD operations on Person entities.

    This class encapsulates the logic for interacting with Person records in the database,
    providing a clear API for creating, reading, updating, and deleting Person entities.

    Attributes:
        db (Session): The database session used to execute queries and transactions.

    Methods:
        __init__(self, db: Session): Initializes the repository with a database session.
        get_person_by_id(self, person_id: int) -> Person: Fetches a person by their unique ID.
        get_all_persons(self, skip: int = 0, limit: int = 100) -> List[Person]: Retrieves a list of persons with pagination.
        create_person(self, person: PersonCreate) -> Person: Adds a new person to the database.
        update_person(self, person_id: int, person: PersonUpdate) -> Person: Updates an existing person's information.
        delete_person(self, person_id: int): Removes a person from the database.
    """

    def __init__(self, db: Session):
        """
        Initializes the repository with the provided database session.

        Args:
            db (Session): The database session for executing queries.
        """
        self.db = db

    def get_person_by_id(self, person_id: int) -> Person:
        """
        Retrieves a Person entity by its ID.

        Args:
            person_id (int): The unique identifier of the person.

        Returns:
            The Person entity if found, otherwise None.
        """
        return self.db.query(Person).filter(Person.id == person_id).first()

    def get_all_persons(self, skip: int = 0, limit: int = 100) -> List[Person]:
        """
        Fetches a list of Person entities, supports pagination.

        Args:
            skip (int): Number of records to skip.
            limit (int): Maximum number of records to return.

        Returns:
            A list of Person entities.
        """
        return self.db.query(Person).offset(skip).limit(limit).all()

    def create_person(self, person: PersonCreate) -> Person:
        """
        Creates a new Person entity in the database.

        Args:
            person (PersonCreate): The person data transfer object containing the details to create a new Person.

        Returns:
            The newly created Person entity.
        """
        db_person = Person(**person.dict())
        self.db.add(db_person)
        self.db.commit()
        self.db.refresh(db_person)
        return db_person

    def update_person(self, person_id: int, person: PersonUpdate) -> Person:
        """
        Updates an existing Person entity with new data.

        Args:
            person_id (int): The unique identifier of the person to update.
            person (PersonUpdate): The person data transfer object containing the
        Returns:
                The updated Person entity.

            Raises:
                HTTPException: If the person with the specified ID does not exist.
            """
        db_person = self.get_person_by_id(person_id)
        if not db_person:
            raise HTTPException(status_code=404, detail="Person not found")
        update_data = person.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_person, key, value)
        self.db.commit()
        self.db.refresh(db_person)
        return db_person

    def delete_person(self, person_id: int):
        """
        Deletes a Person entity from the database.

        Args:
            person_id (int): The unique identifier of the person to delete.

        Returns:
            A dictionary confirming the deletion.

        Raises:
            HTTPException: If the person with the specified ID does not exist.
        """
        db_person = self.get_person_by_id(person_id)
        if not db_person:
            raise HTTPException(status_code=404, detail="Person not found")
        self.db.delete(db_person)
        self.db.commit()
        return {"ok": True}
