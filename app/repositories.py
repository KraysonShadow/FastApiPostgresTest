from sqlalchemy.orm import Session
from app.database import User, Product, CartItem
from app import schemas

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: schemas.UserCreate):
        db_user = User(name=user.name)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int):
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
        return db_user

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product: schemas.ProductCreate):
        db_product = Product(name=product.name)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def delete_product(self, product_id: int):
        db_product = self.db.query(Product).filter(Product.id == product_id).first()
        if db_product:
            self.db.delete(db_product)
            self.db.commit()
        return db_product

class CartRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_to_cart(self, cart_item: schemas.CartItemCreate):
        db_cart_item = CartItem(user_id=cart_item.user_id, product_id=cart_item.product_id, quantity=cart_item.quantity)
        self.db.add(db_cart_item)
        self.db.commit()
        self.db.refresh(db_cart_item)
        return db_cart_item

    def remove_from_cart(self, cart_item_id: int):
        db_cart_item = self.db.query(CartItem).filter(CartItem.id == cart_item_id).first()
        if db_cart_item:
            self.db.delete(db_cart_item)
            self.db.commit()
        return db_cart_item

    def update_cart(self, cart_item_id: int, quantity: int):
        db_cart_item = self.db.query(CartItem).filter(CartItem.id == cart_item_id).first()
        if db_cart_item:
            db_cart_item.quantity = quantity
            self.db.commit()
            self.db.refresh(db_cart_item)
        return db_cart_item
