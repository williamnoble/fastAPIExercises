import os

from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData

from async_api.app import ping
from async_api.app.db import database

app = FastAPI()
app.include_router(ping.router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


