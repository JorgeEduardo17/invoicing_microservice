from unittest.mock import patch
from app.schemas.product import Product


def test_create_product(test_client, product_data):
    with patch("app.routers.product.get_product_service") as mock_service:
        mock_service.return_value.create_product.return_value = Product(**product_data, id=1)
        response = test_client.post("/product/", json=product_data)
        assert response.status_code == 201
        assert response.json()["name"] == product_data["name"]


def test_read_product(test_client, product_data):
    product_id = 1
    with patch("app.routers.product.get_product_service") as mock_service:
        mock_service.return_value.get_product.return_value = Product(**product_data, id=product_id)
        response = test_client.get(f"/product/{product_id}")
        assert response.status_code == 200
        assert response.json()["id"] == product_id
        assert response.json()["name"] == product_data["name"]


def test_read_products(test_client, product_data):
    with patch("app.routers.product.get_product_service") as mock_service:
        mock_service.return_value.get_all_products.return_value = [Product(**product_data, id=1)]
        response = test_client.get("/product/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert response.json()[0]["name"] == product_data["name"]


def test_update_product(test_client, product_data, product_update_data):
    product_id = 1
    with patch("app.routers.product.get_product_service") as mock_service:
        mock_service.return_value.update_product.return_value = Product(**product_update_data, id=product_id)
        response = test_client.put(f"/product/{product_id}", json=product_update_data)
        assert response.status_code == 200
        assert response.json()["name"] == product_update_data["name"]


def test_delete_product(test_client):
    product_id = 1
    with patch("app.routers.product.get_product_service") as mock_service:
        mock_service.return_value.delete_product.return_value = None
        response = test_client.delete(f"/product/{product_id}")
        assert response.status_code == 204
