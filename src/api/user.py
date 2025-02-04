from fastapi import Depends, APIRouter, status
from src.dao.db import get_db
from src.dto.user import UserResponse, UserCreate, UserUpdate, UserUpdateStatus
from sqlalchemy.ext.asyncio import AsyncSession
from src.dao.users import (
    get_user,
    create_user,
    update_user,
    delete_user,
    all_user,
    update_status,
)
from src.exceptions.user import UserNotFound, InvalidSortingAttribute, UserAlreadyExists
from src.api.common_endpoints import USER
from src.utils.constants import Status
from uuid import UUID
from typing import List, Optional

router = APIRouter(tags=["Users"])


@router.get(
    USER + "/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResponse
)
async def get_single_user(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """
    This endpoint gets single user details by user id
    """
    user = await get_user(db, user_id)
    if not user:
        raise UserNotFound(detail="No User found")
    return user


@router.post(USER, status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_new_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    This endpoint creates a new user.
    """
    return await create_user(db, user)


@router.put(
    USER + "/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResponse
)
async def update_existing_user(
    user_id: UUID, user: UserUpdate, db: AsyncSession = Depends(get_db)
):
    """
    This endpoint updates an existing user details in the database.
    """

    updated_user = await update_user(db, user_id, user)
    if not updated_user:
        raise UserNotFound(detail="No User found")
    return updated_user


@router.delete(USER + "/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_item(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """This endpoint deletes a user by given id."""

    deleted_user = await delete_user(db, user_id)
    if not deleted_user:
        raise UserNotFound(detail="No User found")
    return {"detail": "User deleted successfully"}


@router.get(USER, status_code=status.HTTP_200_OK, response_model=List[UserResponse])
async def get_all_user(
    db: AsyncSession = Depends(get_db),
    search: Optional[str] = None,
    sort_by: Optional[str] = "created_at",
    sort_order: Optional[str] = "asc",
    limit: Optional[int] = 5,
    offset: Optional[int] = 0,
):
    """
    This endpoint gets the user from the database by applying filtering, searching and sorting.
    """

    users = await all_user(
        db,
        search=search,
        sort_by=sort_by,
        sort_order=sort_order,
        limit=limit,
        offset=offset,
    )
    if not users:
        raise UserNotFound(
            status_code=status.HTTP_404_NOT_FOUND, detail="No User found"
        )
    return users


@router.patch(
    USER + "/{user_id}" + "/status",
    status_code=status.HTTP_200_OK,
    response_model=UserResponse,
)
async def change_user_status(
    user_id: UUID, new_status: Status, db: AsyncSession = Depends(get_db)
):
    """
    This endpoint updates an existing user's status in the database.
    """
    updated_user_status = await update_status(db, user_id, new_status)
    if not updated_user_status:
        raise UserNotFound(detail="User not found")
    return updated_user_status
