from fastapi import FastAPI
from routers import router_user, router_product

app = FastAPI()

app.include_router(
    router_user.router,
    prefix='/api/user',
    tags=['auth']
)

app.include_router(
    router_product.router,
    prefix='/api/products',
    tags=['product']
)
