from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.core.config import settings
import asyncio

# # For synchronous way by using create_engine
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import declarative_base
# from sqlalchemy.orm import Session


# SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


async def get_db():
    """
    This function creates a new database async session.
    """
    async with async_session() as session:
        yield session

def transaction(func):
    """
    This function is a decorator that wraps the function it's applied to.
    It attempts to commit changes, and if there are any errors, it rolls back those changes.
    This helps avoid leaving behind partially-committed transactions when things go wrong.

    :param func: Pass the function that is being wrapped
    :return: The response of the function it decorates
    """

    async def async_inner(*args, **kwargs):
        db: AsyncSession = kwargs.get("db")
        if db is None:
            raise ValueError("Database session 'db' is required in the arguments.")
        
        try:
            # Execute the function
            response = await func(*args, **kwargs)
            # Commit the transaction
            await db.commit()
            return response
        except Exception as database_exception:
            # Rollback in case of an exception
            await db.rollback()
            raise database_exception
        finally:
            # Ensure the session is closed after the transaction
            await db.close()

    def inner(*args, **kwargs):
        db = kwargs.get("db")
        if db is None:
            raise ValueError("Database session 'db' is required in the arguments.")
        
        try:
            # Execute the function
            response = func(*args, **kwargs)
            # Commit the transaction
            db.commit()
            return response
        except Exception as database_exception:
            # Rollback in case of an exception
            db.rollback()
            raise database_exception
        finally:
            # Ensure the session is closed after the transaction
            db.close()

    if asyncio.iscoroutinefunction(func):
        return async_inner
    else:
        return inner