from fastapi import APIRouter, Depends, HTTPException, Body, Query
from sqlalchemy.orm import Session
from app import schemas, services, repositories
from app.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/add", response_model=schemas.UserCreate)
def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_service = services.UserService(repositories.UserRepository(db))
    return user_service.create_user(user)

@router.post("/users/delete/{user_id}", response_model=schemas.UserCreate)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_service = services.UserService(repositories.UserRepository(db))
    user = user_service.delete_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/products/add", response_model=schemas.ProductCreate)
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    product_service = services.ProductService(repositories.ProductRepository(db))
    return product_service.create_product(product)

@router.post("/products/delete/{product_id}", response_model=schemas.ProductCreate)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_service = services.ProductService(repositories.ProductRepository(db))
    product = product_service.delete_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/cart/add", response_model=schemas.CartItemCreate)
def add_to_cart(cart_item: schemas.CartItemCreate, db: Session = Depends(get_db)):
    cart_service = services.CartService(repositories.CartRepository(db))
    return cart_service.add_to_cart(cart_item)

@router.post("/cart/remove/{cart_item_id}", response_model=schemas.CartItemCreate)
def remove_from_cart(cart_item_id: int, db: Session = Depends(get_db)):
    cart_service = services.CartService(repositories.CartRepository(db))
    return cart_service.remove_from_cart(cart_item_id)


@router.post("/cart/update/{cart_item_id}", response_model=schemas.UpdateCartItem)
def update_cart(cart_item_id: int, item: schemas.UpdateCartItem, db: Session = Depends(get_db)):
    quantity = item.quantity
    print(f"Received update request for cart item {cart_item_id} with quantity: {quantity}")
    cart_service = services.CartService(repositories.CartRepository(db))
    return cart_service.update_cart(cart_item_id, quantity)

