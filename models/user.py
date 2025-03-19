from sqlalchemy import Table, Column, Integer, String, MetaData
from database import Base



metadata = MetaData()

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(255), nullable=False),
    Column("email", String(255), unique=True, nullable=False),
    Column("password", String(255), nullable=False),
    Column("address", String(255), nullable=True),
    Column("phone_number", String(20), nullable=True)
)



