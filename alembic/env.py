from app.database import DATABASE_URL
from sqlalchemy.ext.asyncio import create_async_engine

config.set_main_option("sqlalchemy.url", DATABASE_URL)
engine = create_async_engine(DATABASE_URL)
