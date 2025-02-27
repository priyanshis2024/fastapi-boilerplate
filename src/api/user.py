from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.dao.db import get_db
from src.dto.user import UserCreate, UserUpdate, UserResponse, UserUpdateStatus
from src.service.user_service import user_service
from src.api.common_endpoints import USER
from uuid import UUID
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(tags=["Users"])


@router.get(USER + "/{user_id}", response_model=UserResponse)
# def get_single_user(user_id: UUID, db_obj: Session = Depends(get_db)):
#     """
#     Synchronous approach
#     This endpoint gets single user details by user id
#     """
#     return user_service.get_user_by_id(user_id, db_obj=db_obj)


async def get_single_user(user_id: UUID, db_obj: AsyncSession = Depends(get_db)):
    """
    This endpoint gets single user details by user id
    """
    return await user_service.get_user_by_id(user_id=user_id, db_obj=db_obj)


@router.post(USER, response_model=UserResponse)
# def create_new_user(user_create: UserCreate, db_obj: Session = Depends(get_db)):
#     """
#     Synchronous approach
#     This endpoint creates a new user.
#     """
#     return user_service.create_user_details(user_create, db_obj=db_obj)


async def create_new_user(
    user_create: UserCreate, db_obj: AsyncSession = Depends(get_db)
):
    """
    This endpoint creates a new user.
    """
    return await user_service.create_user_details(user_create, db_obj=db_obj)


@router.patch(USER + "/{user_id}", response_model=UserResponse)
# def update_existing_user(user_id: UUID, user_update: UserUpdate, db_obj: Session = Depends(get_db)):
#     """
#     Synchronous approach
#     This endpoint updates an existing user details in the database.
#     """
#     return user_service.update_existing_user(user_id, user_update, db_obj=db_obj)


async def update_existing_user(
    user_id: UUID, user_update: UserUpdate, db_obj: AsyncSession = Depends(get_db)
):
    """
    This endpoint updates an existing user details in the database.
    """
    return await user_service.update_existing_user(user_id, user_update, db_obj=db_obj)


@router.delete(USER + "/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_existing_user(user_id: UUID, db_obj: Session = Depends(get_db)):
#     """
#     Synchronous approach
#     This endpoint deletes a user by given id.
#     """
#     return user_service.delete_existing_user(user_id, db_obj=db_obj)


async def delete_existing_user(user_id: UUID, db_obj: AsyncSession = Depends(get_db)):
    """
    This endpoint deletes a user by given id.
    """
    return await user_service.delete_existing_user(user_id, db_obj=db_obj)


@router.get(USER, response_model=List[UserResponse])
# def get_all_users(
#     db_obj: Session = Depends(get_db),
#     search: Optional[str] = None,
#     sort_by: Optional[str] = "created_at",
#     sort_order: Optional[str] = "asc",
#     limit: Optional[int] = 10,
#     offset: Optional[int] = 0,
# ):
#     """
#     Synchronous approach
#     This endpoint gets the user from the database by applying filtering, searching and sorting.
#     """
#     return user_service.get_all_users(
#         db_obj=db_obj,
#         search=search,
#         sort_by=sort_by,
#         sort_order=sort_order,
#         limit=limit,
#         offset=offset,
#     )


async def get_all_users(
    db_obj: AsyncSession = Depends(get_db),
    search: Optional[str] = None,
    sort_by: Optional[str] = "created_at",
    sort_order: Optional[str] = "asc",
    limit: Optional[int] = 10,
    offset: Optional[int] = 0,
):
    """
    This endpoint gets the user from the database by applying filtering, searching and sorting.
    """
    return await user_service.get_all_users(
        db_obj=db_obj,
        search=search,
        sort_by=sort_by,
        sort_order=sort_order,
        limit=limit,
        offset=offset,
    )


@router.patch(USER + "/{user_id}" + "/status", response_model=UserResponse)
# def change_user_status(
#     user_id: UUID,
#     user_update_status: UserUpdateStatus,
#     db_obj: Session = Depends(get_db),
# ):
#     """
#     Synchronous approach
#     This endpoint updates an existing user's status in the database.
#     """
#     return user_service.change_user_status(
#         user_id=user_id, user_update_status=user_update_status, db_obj=db_obj
#     )


async def change_user_status(
    user_id: UUID,
    user_update_status: UserUpdateStatus,
    db_obj: AsyncSession = Depends(get_db),
):
    """
    This endpoint updates an existing user's status in the database.
    """
    return await user_service.change_user_status(
        user_id=user_id, user_update_status=user_update_status, db_obj=db_obj
    )
