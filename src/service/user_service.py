from src.dto.user import UserCreate, UserUpdate, UserUpdateStatus
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from sqlalchemy.future import select
from typing import List, Optional
from src.service.converter import Converter
from src.dao.db import transaction
from src.dao.models.user import User
from src.dao.users import all_user 

# Synchronous approach
# from sqlalchemy.orm import Session

class UserService:

    # def get_user_by_id(self, user_id: UUID, db: Session):
    #     """
    #     Service function to get a user by ID
    #     :param db: The session object
    #     :param user_id: The ID of the user to retrieve
    #     :return: User object
    #     """
    #     return db.query(User).filter(User.id == user_id).first()

    @transaction
    async def get_user_by_id(self, user_id: UUID, db: AsyncSession):
        """
        Service function to get a user by ID asynchronously.
        :param db: The session object
        :param user_id: The ID of the user to retrieve
        :return: User object or None
        """
        result = await db.execute(select(User).filter(User.id == user_id))
        user = result.scalar_one_or_none()  
        return user

    # def create_user_details(self, user_create: UserCreate, db: Session):
    #     """
    #     Service function to create a new user
    #     :param db: The session object
    #     :param user_create: The user creation DTO
    #     :return: Created User object
    #     """
    #     try:
    #         user_db = Converter.user_create_dto_to_db(user_create)
    #         db.add(user_db)
    #         db.commit()
    #         db.refresh(user_db)
    #         return Converter.user_db_to_dto(user_db)
    #     except Exception as e:
    #         db.rollback()
    #         raise e
        
    @transaction
    async def create_user_details(self, user_create: UserCreate, db: AsyncSession):
        """
        Service function to create a new user asynchronously.
        :param db: The session object
        :param user_create: The user creation DTO
        :return: Created User object (DTO)
        """
        user_db = Converter.user_create_dto_to_db(user_create)
        db.add(user_db)
        await db.commit()
        await db.refresh(user_db)  
        return Converter.user_db_to_dto(user_db)

    # def update_existing_user(self, user_id: UUID, user_update: UserUpdate, db: Session):
    #     """
    #     Service function to update an existing user
    #     :param db: The session object
    #     :param user_id: The ID of the user to update
    #     :param user_update: The user update DTO
    #     :return: Updated User object
    #     """
    #     try:
    #         user_db = db.query(User).filter(User.id == user_id).first()
    #         if not user_db:
    #             return None
    #         updated_user = Converter.user_update_dto_to_db(user_update, user_db)
    #         db.commit()
    #         db.refresh(updated_user)
    #         return Converter.user_db_to_dto(updated_user)
    #     except Exception as e:
    #         db.rollback()
    #         raise e

    @transaction
    async def update_existing_user(self, user_id: UUID, user_update: UserUpdate, db: AsyncSession):
        """
        Service function to update an existing user asynchronously.
        :param db: The session object
        :param user_id: The ID of the user to update
        :param user_update: The user update DTO
        :return: Updated User object (DTO) or None
        """
        result = await db.execute(select(User).filter(User.id == user_id))
        user_db = result.scalar_one_or_none()  
        if not user_db:
            return None

        updated_user = Converter.user_update_dto_to_db(user_update, user_db)
        await db.commit()
        await db.refresh(updated_user)
        return Converter.user_db_to_dto(updated_user)
        
    # def delete_existing_user(self, user_id: UUID, db: Session):
    #     """
    #     Service function to delete a user
    #     :param db: The session object
    #     :param user_id: The ID of the user to delete
    #     :return: Dictionary with success status
    #     """
    #     try:
    #         user_db = db.query(User).filter(User.id == user_id).first()
    #         if user_db:
    #             db.delete(user_db)
    #             db.commit()
    #             return {"status": "Success"}  # Status 204 (No Content) will be returned
    #         return {"status": f"Successfully deleted {user_id}"}
    #     except Exception as e:
    #         db.rollback()
    #         raise e

    @transaction
    async def delete_existing_user(self, user_id: UUID, db: AsyncSession):
        """
        Service function to delete a user asynchronously.
        :param db: The session object
        :param user_id: The ID of the user to delete
        :return: Dictionary with success status
        """
        result = await db.execute(select(User).filter(User.id == user_id))
        user_db = result.scalar_one_or_none()
        if user_db:
            await db.delete(user_db)
            return {"status": "Success"}  # User deleted successfully
        return {"status": f"User {user_id} not found."}

    # def get_all_users(self, db: Session, 
    #                   search: Optional[str] = None, 
    #                   sort_by: Optional[str] = "created_at", 
    #                   sort_order: Optional[str] = "asc", 
    #                   limit: Optional[int] = 10, 
    #                   offset: Optional[int] = 0
    #                   ):
    #     """
    #     Service function to get all users with filters
    #     :param db: The session object
    #     """
    #     users = all_user(db, search, sort_by, sort_order, limit, offset)
    #     return [Converter.user_db_to_dto(user) for user in users]
    
    @transaction
    async def get_all_users(self, db: AsyncSession,
                            search: Optional[str] = None, 
                            sort_by: Optional[str] = "created_at", 
                            sort_order: Optional[str] = "asc", 
                            limit: Optional[int] = 10, 
                            offset: Optional[int] = 0
                            ):
        """
        Service function to get all users asynchronously.
        :param db: The session object
        :return: List of User DTOs
        """
        users = await all_user(db, search, sort_by, sort_order, limit, offset)
        return [Converter.user_db_to_dto(user) for user in users]
    
    # def change_user_status(self, db: Session, user_id: UUID, user_update_status: UserUpdateStatus):
    #     """
    #     Service function to change the status of a user
    #     :param db: The session object
    #     :param user_id: The ID of the user to update
    #     :param user_update_status: The status update schema from user dto
    #     :return: Updated User object with new status
    #     """
    #     try:
    #         user_db = db.query(User).filter(User.id == user_id).first()
    #         if user_db:
    #             updated_user = Converter.user_update_status_dto_to_db(user_update_status, user_db)
    #             db.commit()
    #             db.refresh(updated_user)
    #             return Converter.user_db_to_dto(updated_user)
    #         return None
    #     except Exception as e:
    #         db.rollback()
    #         raise e
        
    @transaction
    async def change_user_status(self, db: AsyncSession, user_id: UUID, user_update_status: UserUpdateStatus):
        """
        Service function to change the status of a user asynchronously.
        :param db: The session object
        :param user_id: The ID of the user to update
        :param user_update_status: The status update schema from user dto
        :return: Updat
        """
        result = await db.execute(select(User).filter(User.id == user_id))
        user_db = result.scalar_one_or_none()
        if user_db:
            updated_user = Converter.user_update_status_dto_to_db(user_update_status, user_db)
            await db.commit()
            await db.refresh(updated_user)
            return Converter.user_db_to_dto(updated_user)
        return None
    
user_service = UserService()