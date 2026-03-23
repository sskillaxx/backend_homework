from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from core.config import DB_URL

Base = declarative_base()
engine = create_async_engine(DB_URL)
AsyncSessionLocal = async_sessionmaker(class_=AsyncSession, autoflush=False, bind=engine)

async def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()