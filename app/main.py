from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.routes import router
from app.database import SessionLocal, engine, Base, User, Product, CartItem
from sqlalchemy.orm import Session

app = FastAPI()
app.include_router(router)

templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    products = db.query(Product).all()
    cart_items = db.query(CartItem).all()
    cart_details = [
        {
            "id": item.id,
            "user_name": db.query(User).filter(User.id == item.user_id).first().name,
            "product_name": db.query(Product).filter(Product.id == item.product_id).first().name,
            "quantity": item.quantity
        }
        for item in cart_items
    ]
    return templates.TemplateResponse("index.html", {"request": request, "users": users, "products": products, "cart_details": cart_details})
