from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.person import Person
from app.repositories.person import PersonRepository
from app.schemas.person import PersonCreate, PersonUpdate


class PersonService:
    """
    Service class for managing CRUD operations for Person entities.

    This service provides methods to create, retrieve (single and all), update, and delete
    Person entities, abstracting the complexity of direct database interactions away from
    the client code.

    Attributes:
        db_session (Session): Database session for executing transactions.
        repository (PersonRepository): Repository handling the persistence operations of Person entities.

    Methods:
        __init__(self, db_session: Session): Initializes a PersonService with the given database session.
        create_person(self, person_create: PersonCreate) -> Person: Creates a new Person entity.
        get_person(self, person_id: int) -> Optional[Person]: Retrieves a Person entity by its ID.
        get_all_persons(self) -> List[Person]: Retrieves all Person entities.
        update_person(self, person_id: int, person_update: PersonUpdate) -> Person: Updates an existing Person entity.
        delete_person(self, person_id: int): Deletes a Person entity by its ID.
    """

    def __init__(self, db_session: Session):
        """
        Initializes the PersonService with a database session and a repository.

        Args:
            db_session (Session): The SQLAlchemy session for database transactions.
        """
        self.db_session = db_session
        self.repository = PersonRepository(db_session)

    def create_person(self, person_create: PersonCreate) -> Person:
        """
        Creates a new Person record in the database.

        Args:
            person_create (PersonCreate): The Person data transfer object containing
                                          the necessary information to create a new Person.

        Returns:
            Person: The newly created Person entity.
        """
        return self.repository.create_person(person_create)

    def get_person(self, person_id: int) -> Optional[Person]:
        """
        Retrieves a single Person entity by its ID.

        Args:
            person_id (int): The unique identifier of the Person.

        Returns:
            Optional[Person]: The found Person entity or None if not found.
        """
        return self.repository.get_person_by_id(person_id)

    def get_all_persons(self) -> List[Person]:
        """
        Retrieves all Person entities from the database.

        Returns:
            List[Person]: A list of all Person entities.
        """
        return self.repository.get_all_persons()

    def update_person(self, person_id: int, person_update: PersonUpdate) -> Person:
        """
        Updates an existing Person record in the database.

        Args:
            person_id (int): The unique identifier of the Person to be updated.
            person_update (PersonUpdate): The Person data transfer object containing
                                          the updated information for the Person.

        Returns:
            Person: The updated Person entity.
        """
        return self.repository.update_person(person_id, person_update)

    def delete_person(self, person_id: int):
        """
        Deletes a Person record by its ID.

        Args:
            person_id (int): The unique identifier of the Person to be deleted.

        Returns:
            The result of the delete operation.
        """
        return self.repository.delete_person(person_id)
