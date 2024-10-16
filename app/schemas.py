from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
class ProductCreate(BaseModel):
    name: str
class CartItemCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class UpdateCartItem(BaseModel):
    quantity: int