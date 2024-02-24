from unittest.mock import patch
from app.schemas.person import Person


def test_create_person(test_client, person_data):
    with patch("app.routers.person.get_person_service") as mock_service:
        mock_service.return_value.create_person.return_value = Person(**person_data, id=1)
        response = test_client.post("/person/", json=person_data)
        assert response.status_code == 201
        assert response.json()["name"] == person_data["name"]


def test_read_person(test_client, person_data):
    person_id = 1
    with patch("app.routers.person.get_person_service") as mock_service:
        mock_service.return_value.get_person.return_value = Person(**person_data, id=person_id)
        response = test_client.get(f"/person/{person_id}")
        assert response.status_code == 200
        assert response.json()["id"] == person_id
        assert response.json()["name"] == person_data["name"]


def test_read_persons(test_client, person_data):
    with patch("app.routers.person.get_person_service") as mock_service:
        mock_service.return_value.get_all_persons.return_value = [Person(**person_data, id=1)]
        response = test_client.get("/person/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert response.json()[0]["name"] == person_data["name"]


def test_update_person(test_client, person_data, person_update_data):
    person_id = 1
    with patch("app.routers.person.get_person_service") as mock_service:
        mock_service.return_value.update_person.return_value = Person(**person_update_data, id=person_id)
        response = test_client.put(f"/person/{person_id}", json=person_update_data)
        assert response.status_code == 200
        assert response.json()["name"] == person_update_data["name"]


def test_delete_person(test_client):
    person_id = 1
    with patch("app.routers.person.get_person_service") as mock_service:
        mock_service.return_value.delete_person.return_value = None
        response = test_client.delete(f"/person/{person_id}")
        assert response.status_code == 204
