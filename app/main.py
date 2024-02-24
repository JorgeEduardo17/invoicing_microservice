"""
This file is the main entry point for the FastAPI application.
It configures the application, including routes, startup and shutdown events, and logging settings.
"""
from fastapi import FastAPI

from app.api.endpoints import person, product, invoice_header, invoice_detail
from app.core.config import settings
from app.core.logger import setup_logging
from app.db.postgresql import init_db

app = FastAPI(title=settings.PROJECT_NAME)  # Create a FastAPI instance for the application.

# Incluir los routers de los endpoints
app.include_router(person.router, prefix="/person", tags=["person"])
app.include_router(product.router, prefix="/product", tags=["product"])
app.include_router(invoice_header.router, prefix="/invoice", tags=["invoice"])
app.include_router(invoice_detail.router, prefix="/invoice_detail", tags=["invoice_detail"])

setup_logging()  # Setup of logging module


@app.on_event("startup")
def startup_db_client():
    init_db()
