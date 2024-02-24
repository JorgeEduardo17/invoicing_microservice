from unittest.mock import patch
from app.schemas.invoice_header import InvoiceHeader


def test_create_invoice_header(test_client, invoice_header_data):
    with patch("app.routers.invoice_header.get_invoice_header_service") as mock_service:
        mock_service.return_value.create_invoice_header.return_value = InvoiceHeader(**invoice_header_data, id=1)
        response = test_client.post("/invoice_header/", json=invoice_header_data)
        assert response.status_code == 201
        assert response.json()["invoice_number"] == invoice_header_data["invoice_number"]


def test_read_invoice_header(test_client, invoice_header_data):
    invoice_header_id = 1
    with patch("app.routers.invoice_header.get_invoice_header_service") as mock_service:
        mock_service.return_value.get_invoice_header.return_value = InvoiceHeader(**invoice_header_data, id=invoice_header_id)
        response = test_client.get(f"/invoice_header/{invoice_header_id}")
        assert response.status_code == 200
        assert response.json()["id"] == invoice_header_id
        assert response.json()["invoice_number"] == invoice_header_data["invoice_number"]


def test_read_invoice_headers(test_client, invoice_header_data):
    with patch("app.routers.invoice_header.get_invoice_header_service") as mock_service:
        mock_service.return_value.get_all_invoice_headers.return_value = [InvoiceHeader(**invoice_header_data, id=1)]
        response = test_client.get("/invoice_header/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert response.json()[0]["invoice_number"] == invoice_header_data["invoice_number"]


def test_delete_invoice_header(test_client):
    invoice_header_id = 1
    with patch("app.routers.invoice_header.get_invoice_header_service") as mock_service:
        mock_service.return_value.delete_invoice_header.return_value = None
        response = test_client.delete(f"/invoice_header/{invoice_header_id}")
        assert response.status_code == 204
        