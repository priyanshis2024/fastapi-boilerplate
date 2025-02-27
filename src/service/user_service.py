from src.dto.user import UserCreate, UserUpdate, UserUpdateStatus
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import Optional
from src.service.converter import Converter
from src.dao.db import transaction
from src.dao.users import UserDAO

# Synchronous approach
from sqlalchemy.orm import Session


class UserService:

    # def get_user_by_id(self, user_id: UUID, db_obj: Session):
    #     """
    #     Service function to get a user by ID
    #     :param db_obj: The session object
    #     :param user_id: The ID of the user to retrieve
    #     :return: User object
    #     """
    #     result = UserDAO.get_user(user_id=user_id, db_obj=db_obj)
    #     return result

    @transaction
    async def get_user_by_id(self, user_id: UUID, db_obj: AsyncSession):
        """
        Service function to get a user by ID asynchronously.
        :param db_obj: The session object
        :param user_id: The ID of the user to retrieve
        :return: User object or None
        """
        result = await UserDAO.get_user(user_id=user_id, db_obj=db_obj)
        return result

    # def create_user_details(self, user_create: UserCreate, db_obj: Session):
    #     """
    #     Service function to create a new user
    #     :param db_obj: The session object
    #     :param user_create: The user creation DTO
    #     :return: Created User object
    #     """
    #     try:
    #         user_db = Converter.user_create_dto_to_db(user_create)
    #         db_obj.add(user_db)
    #         db_obj.commit()
    #         db_obj.refresh(user_db)
    #         return Converter.user_db_to_dto(user_db)
    #     except Exception as e:
    #         db_obj.rollback()
    #         raise e

    @transaction
    async def create_user_details(self, user_create: UserCreate, db_obj: AsyncSession):
        """
        Service function to create a new user asynchronously.
        :param db_obj: The session object
        :param user_create: The user creation DTO
        :return: Created User object (DTO)
        """
        user_db = Converter.user_create_dto_to_db(user_create)
        db_obj.add(user_db)
        await db_obj.commit()
        await db_obj.refresh(user_db)
        return Converter.user_db_to_dto(user_db)

    # def update_existing_user(
    #     self, user_id: UUID, user_update: UserUpdate, db_obj: Session
    # ):
    #     """
    #     Service function to update an existing user
    #     :param db_obj: The session object
    #     :param user_id: The ID of the user to update
    #     :param user_update: The user update DTO
    #     :return: Updated User object
    #     """
    #     try:
    #         user_db = UserDAO.get_user(user_id=user_id, db_obj=db_obj)
    #         if not user_db:
    #             return None
    #         updated_user = Converter.user_update_dto_to_db(user_update, user_db)
    #         db_obj.commit()
    #         db_obj.refresh(updated_user)
    #         return Converter.user_db_to_dto(updated_user)
    #     except Exception as e:
    #         db_obj.rollback()
    #         raise e

    @transaction
    async def update_existing_user(
        self, user_id: UUID, user_update: UserUpdate, db_obj: AsyncSession
    ):
        """
        Service function to update an existing user asynchronously.
        :param db_obj: The session object
        :param user_id: The ID of the user to update
        :param user_update: The user update DTO
        :return: Updated User object (DTO) or None
        """
        user_db = await UserDAO.get_user(user_id=user_id, db_obj=db_obj)
        if not user_db:
            return None

        updated_user = Converter.user_update_dto_to_db(user_update, user_db)
        await db_obj.commit()
        await db_obj.refresh(updated_user)
        return Converter.user_db_to_dto(updated_user)

    # def delete_existing_user(self, user_id: UUID, db_obj: Session):
    #     """
    #     Service function to delete a user
    #     :param db_obj: The session object
    #     :param user_id: The ID of the user to delete
    #     :return: Dictionary with success status
    #     """
    #     try:
    #         user_db = UserDAO.get_user(user_id=user_id, db_obj=db_obj)
    #         if user_db:
    #             db_obj.delete(user_db)
    #             db_obj.commit()
    #             return {"status": "Success"}
    #         return {"status": f"Successfully deleted {user_id}"}
    #     except Exception as e:
    #         db_obj.rollback()
    #         raise e

    @transaction
    async def delete_existing_user(self, user_id: UUID, db_obj: AsyncSession):
        """
        Service function to delete a user asynchronously.
        :param db_obj: The session object
        :param user_id: The ID of the user to delete
        :return: Dictionary with success status
        """
        user_db = await UserDAO.get_user(user_id=user_id, db_obj=db_obj)
        if user_db:
            await db_obj.delete(user_db)
            return {"status": "Success"}
        return {"status": f"User {user_id} not found."}

    # def get_all_users(
    #     self,
    #     db_obj: Session,
    #     search: Optional[str] = None,
    #     sort_by: Optional[str] = "created_at",
    #     sort_order: Optional[str] = "asc",
    #     limit: Optional[int] = 10,
    #     offset: Optional[int] = 0,
    # ):
    #     """
    #     Service function to get all users with filters
    #     :param db_obj: The session object
    #     """
    #     users = UserDAO.all_user(
    #         db_obj=db_obj,
    #         search=search,
    #         sort_by=sort_by,
    #         sort_order=sort_order,
    #         limit=limit,
    #         offset=offset,
    #     )
    #     return [Converter.user_db_to_dto(user) for user in users]

    async def get_all_users(
        self,
        db_obj: AsyncSession,
        search: Optional[str] = None,
        sort_by: Optional[str] = "created_at",
        sort_order: Optional[str] = "asc",
        limit: Optional[int] = 10,
        offset: Optional[int] = 0,
    ):
        """
        Service function to get all users asynchronously.
        :param db_obj: The session object
        :return: List of User DTOs
        """
        users = await UserDAO.all_user(
            db_obj=db_obj,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
            limit=limit,
            offset=offset,
        )
        return [Converter.user_db_to_dto(user) for user in users]

    # def change_user_status(
    #     self, db_obj: Session, user_id: UUID, user_update_status: UserUpdateStatus
    # ):
    #     """
    #     Service function to change the status of a user
    #     :param db_obj: The session object
    #     :param user_id: The ID of the user to update
    #     :param user_update_status: The status update schema from user dto
    #     :return: Updated User object with new status
    #     """
    #     try:
    #         user_db = UserDAO.get_user(user_id=user_id, db_obj=db_obj)
    #         if user_db:
    #             updated_user = Converter.user_update_status_dto_to_db(
    #                 user_update_status, user_db
    #             )
    #             db_obj.commit()
    #             db_obj.refresh(updated_user)
    #             return Converter.user_db_to_dto(updated_user)
    #         return None
    #     except Exception as e:
    #         db_obj.rollback()
    #         raise e

    @transaction
    async def change_user_status(
        self, db_obj: AsyncSession, user_id: UUID, user_update_status: UserUpdateStatus
    ):
        """
        Service function to change the status of a user asynchronously.
        :param db_obj: The session object
        :param user_id: The ID of the user to update
        :param user_update_status: The status update schema from user dto
        :return: Updat
        """
        user_db = await UserDAO.get_user(user_id=user_id, db_obj=db_obj)
        if user_db:
            updated_user = Converter.user_update_status_dto_to_db(
                user_update_status, user_db
            )
            await db_obj.commit()
            await db_obj.refresh(updated_user)
            return Converter.user_db_to_dto(updated_user)
        return None


user_service = UserService()
