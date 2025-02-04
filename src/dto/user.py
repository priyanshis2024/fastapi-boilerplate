"""This module handles request body, response body and field validation"""

from typing import Optional
from fastapi_camelcase import CamelModel
from pydantic import Field, EmailStr
from uuid import UUID
from datetime import datetime


class UserCreate(CamelModel):
    first_name: str = Field(
        ..., title="First Name", description="The first name of the user"
    )
    last_name: str = Field(
        ..., title="Last Name", description="The last name of the user"
    )
    gender: int = Field(..., title="Gender", description="The gender of the user")
    email: EmailStr = Field(
        ..., title="Email", description="The email address of the user"
    )
    phone_number: Optional[str] = Field(
        None, title="Phone Number", description="The phone number of the user"
    )
    status: Optional[int] = Field(
        None, title="Status", description="The status of the user"
    )


class UserResponse(CamelModel):
    id: UUID = Field(..., title="ID", description="The unique identifier of the user")
    first_name: Optional[str] = Field(
        None, title="First Name", description="The first name of the user"
    )
    last_name: str = Field(
        ..., title="Last Name", description="The last name of the user"
    )
    gender: int = Field(..., title="Gender", description="The gender of the user")
    email: EmailStr = Field(
        ..., title="Email", description="The email address of the user"
    )
    phone_number: Optional[str] = Field(
        None, title="Phone Number", description="The phone number of the user"
    )
    status: int = Field(..., title="Status", description="The status of the user")
    created_at: Optional[datetime] = Field(
        None,
        title="Created At",
        description="The timestamp when the user details were created",
    )
    updated_at: Optional[datetime] = Field(
        None,
        title="Updated At",
        description="The timestamp when the user details were last updated",
    )

    class Config:
        orm_mode = True


class UserUpdate(CamelModel):
    first_name: str = Field(
        ..., title="First Name", description="The first name of the user"
    )
    last_name: str = Field(
        ..., title="Last Name", description="The last name of the user"
    )
    gender: int = Field(..., title="Gender", description="The gender of the user")
    email: EmailStr = Field(
        ..., title="Email", description="The email address of the user"
    )
    phone_number: Optional[str] = Field(
        None, title="Phone Number", description="The phone number of the user"
    )
    status: int = Field(..., title="Status", description="The status of the user")


class UserUpdateStatus(CamelModel):
    status: int = Field(
        ...,
        title="User status",
        description="User status to check if they are disable, enable or blocked.",
    )
