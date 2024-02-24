from unittest.mock import patch
from app.schemas.invoice_detail import InvoiceDetail


def test_create_invoice_detail(test_client, invoice_detail_data):
    with patch("app.routers.invoice_detail.get_invoice_detail_service") as mock_service:
        mock_service.return_value.create_invoice_detail.return_value = InvoiceDetail(**invoice_detail_data, id=1)
        response = test_client.post("/invoice_detail/", json=invoice_detail_data)
        assert response.status_code == 201
        assert response.json()["invoice_id"] == invoice_detail_data["invoice_id"]


def test_read_invoice_detail(test_client, invoice_detail_data):
    invoice_detail_id = 1
    with patch("app.routers.invoice_detail.get_invoice_detail_service") as mock_service:
        mock_service.return_value.get_invoice_detail.return_value = InvoiceDetail(**invoice_detail_data, id=invoice_detail_id)
        response = test_client.get(f"/invoice_detail/{invoice_detail_id}")
        assert response.status_code == 200
        assert response.json()["id"] == invoice_detail_id
        assert response.json()["invoice_id"] == invoice_detail_data["invoice_id"]


def test_read_invoice_details(test_client, invoice_detail_data):
    with patch("app.routers.invoice_detail.get_invoice_detail_service") as mock_service:
        mock_service.return_value.get_all_invoice_details.return_value = [InvoiceDetail(**invoice_detail_data, id=1)]
        response = test_client.get("/invoice_detail/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert response.json()[0]["invoice_id"] == invoice_detail_data["invoice_id"]


def test_delete_invoice_detail(test_client):
    invoice_detail_id = 1
    with patch("app.routers.invoice_detail.get_invoice_detail_service") as mock_service:
        mock_service.return_value.delete_invoice_detail.return_value = None
        response = test_client.delete(f"/invoice_detail/{invoice_detail_id}")
        assert response.status_code == 204
