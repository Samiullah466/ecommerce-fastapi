from fastapi import FastAPI

from app.api.routes import (
    auth_routes,
    product_routes,
    cart_routes,
    order_routes,
    profile_routes
)

app = FastAPI(title="Ecommerce API")


app.include_router(auth_routes.router)
app.include_router(product_routes.router)
app.include_router(cart_routes.router)
app.include_router(order_routes.router)
app.include_router(profile_routes.router)


@app.get("/")
def home():
    return {"msg": "Welcome to Ecommerce API"}

