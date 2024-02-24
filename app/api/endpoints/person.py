from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import Response
from sqlalchemy.orm import Session

from app.db.postgresql import get_db
from app.schemas.person import PersonCreate, Person, PersonUpdate
from app.servicies.person import PersonService

router = APIRouter()


def get_person_service(db: Session = Depends(get_db)):
    return PersonService(db_session=db)


@router.post("/", response_model=Person, status_code=status.HTTP_201_CREATED)
def create_person(person_create: PersonCreate, service: PersonService = Depends(get_person_service)):
    return service.create_person(person_create)


@router.get("/{person_id}", response_model=Person)
def read_person(person_id: int, service: PersonService = Depends(get_person_service)):
    person = service.get_person(person_id)
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person


@router.get("/", response_model=List[Person])
def read_persons(service: PersonService = Depends(get_person_service)):
    return service.get_all_persons()


@router.put("/{person_id}", response_model=Person)
def update_person(person_id: int, person_update: PersonUpdate, service: PersonService = Depends(get_person_service)):
    return service.update_person(person_id, person_update)


@router.delete("/{person_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_person(person_id: int, service: PersonService = Depends(get_person_service)):
    service.delete_person(person_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
