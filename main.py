from fastapi import FastAPI
from routers import router_user, router_product
from database.db import database as db

app = FastAPI()

app.include_router(
    router_user.router,
    prefix='/api/users',
    tags=['auth']
)

app.include_router(
    router_product.router,
    prefix='/api/products',
    tags=['product']
)


@app.on_event('startup')
async def startup():
    await db.connect()


@app.on_event('shutdown')
async def shutdown():
    await db.disconnect()


