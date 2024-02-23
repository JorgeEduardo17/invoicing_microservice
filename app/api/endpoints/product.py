from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import Response
from sqlalchemy.orm import Session

from app.db.postgresql import get_db
from app.schemas.product import ProductCreate, Product, ProductUpdate
from app.servicies.product import ProductService

router = APIRouter()


def get_product_service(db: Session = Depends(get_db)):
    return ProductService(db_session=db)


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product_create: ProductCreate, service: ProductService = Depends(get_product_service)):
    return service.create_product(product_create)


@router.get("/{product_id}", response_model=Product)
def read_product(product_id: int, service: ProductService = Depends(get_product_service)):
    product = service.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/", response_model=List[Product])
def read_products(service: ProductService = Depends(get_product_service)):
    return service.get_all_products()


@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product_update: ProductUpdate,
                   service: ProductService = Depends(get_product_service)):
    return service.update_product(product_id, product_update)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, service: ProductService = Depends(get_product_service)):
    service.delete_product(product_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
