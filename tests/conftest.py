"""
This module defines pytest fixtures for testing FastAPI endpoints. It includes fixtures for creating
a test client for sending requests to the application, and various data fixtures for testing CRUD
operations on the Person, Product, InvoiceDetail, and InvoiceHeader models. These fixtures simplify
the setup of test data, making it easier to write and maintain tests.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def test_client():
    """
    Provides a fixture for a FastAPI TestClient instance, enabling tests to make requests
    to the application. Use this client to simulate GET, POST, PUT, and DELETE requests in tests.
    """
    with TestClient(app) as client:
        yield client


@pytest.fixture
def person_data():
    """
    Provides a fixture for person data, suitable for testing person creation endpoints.
    Returns a dictionary with sample person data.
    """
    return {"name": "Jorge Quin", "age": 30}


@pytest.fixture
def person_update_data():
    """
    Provides a fixture for updated person data, suitable for testing person update endpoints.
    Returns a dictionary with sample updated person data.
    """
    return {"name": "Eduardo Quin", "age": 31}


@pytest.fixture
def product_data():
    """
    Provides a fixture for product data, suitable for testing product creation endpoints.
    Returns a dictionary with sample product data.
    """
    return {"name": "Test Product", "description": "This is a test product", "price": 10.0, "tax": 1.0}


@pytest.fixture
def product_update_data():
    """
    Provides a fixture for updated product data, suitable for testing product update endpoints.
    Returns a dictionary with sample updated product data.
    """
    return {"name": "Updated Product", "description": "This is an updated test product", "price": 12.0, "tax": 1.2}


@pytest.fixture
def invoice_detail_data():
    """
    Provides a fixture for invoice detail data, suitable for testing invoice detail creation endpoints.
    Returns a dictionary with sample invoice detail data.
    """
    return {"invoice_id": 1, "product_id": 1, "quantity": 2, "unit_price": 100.0}


@pytest.fixture
def invoice_detail_update_data():
    """
    Provides a fixture for updated invoice detail data, suitable for testing invoice detail update endpoints.
    Returns a dictionary with sample updated invoice detail data.
    """
    return {"invoice_id": 1, "product_id": 1, "quantity": 3, "unit_price": 100.0}


@pytest.fixture
def invoice_header_data():
    """
    Provides a fixture for invoice header data, suitable for testing invoice header creation endpoints.
    Returns a dictionary with sample invoice header data.
    """
    return {"customer_id": 1, "invoice_date": "2024-01-01", "due_date": "2024-01-15", "invoice_number": "INV-001"}


@pytest.fixture
def invoice_header_update_data():
    """
    Provides a fixture for updated invoice header data, suitable for testing invoice header update endpoints.
    Returns a dictionary with sample updated invoice header data.
    """
    return {"customer_id": 2, "invoice_date": "2024-01-02", "due_date": "2024-01-16", "invoice_number": "INV-002"}
