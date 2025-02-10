from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, func, String
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP, INTEGER
import uuid

Base = declarative_base()


class User(Base):
    """This class maps to a table user that holds
    the user details."""

    __tablename__ = "user"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        default=uuid.uuid4,
    )
    first_name = Column(String(512), nullable=False)
    last_name = Column(String(512), nullable=False)
    gender = Column(INTEGER, nullable=False)
    email = Column(String(1024), nullable=True)
    phone_number = Column(String(20), nullable=True)
    status = Column(INTEGER, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
