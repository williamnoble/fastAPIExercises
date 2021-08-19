import os

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, func
from databases import Database

DATABASE_URL = os.getenv("FAST_URL")

# To communicate with database
engine = create_engine(DATABASE_URL)

# To create schema
metadata = MetaData()

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False)
)

# Database instance
database = Database(DATABASE_URL)
