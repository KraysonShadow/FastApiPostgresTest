from app.repositories import UserRepository, ProductRepository, CartRepository
from app.schemas import UserCreate, ProductCreate, CartItemCreate

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, user: UserCreate):
        return self.user_repo.create_user(user)

    def delete_user(self, user_id: int):
        return self.user_repo.delete_user(user_id)

class ProductService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    def create_product(self, product: ProductCreate):
        return self.product_repo.create_product(product)

    def delete_product(self, product_id: int):
        return self.product_repo.delete_product(product_id)

class CartService:
    def __init__(self, cart_repo: CartRepository):
        self.cart_repo = cart_repo

    def add_to_cart(self, cart_item: CartItemCreate):
        return self.cart_repo.add_to_cart(cart_item)

    def remove_from_cart(self, cart_item_id: int):
        return self.cart_repo.remove_from_cart(cart_item_id)

    def update_cart(self, cart_item_id: int, quantity: int):
        return self.cart_repo.update_cart(cart_item_id, quantity)