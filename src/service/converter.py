from src.dto.user import UserCreate, UserUpdate, UserResponse, UserUpdateStatus
from src.dao.models.user import User
from src.utils.constants import Status
from fastapi.encoders import jsonable_encoder


class Converter:

    def user_db_to_dto(user: UserResponse):
        """
        Convert a User database model to a UserResponse DTO.
        :param user: User database model
        :return: UserResponse DTO
        """
        user_dict = jsonable_encoder(user)
        return UserResponse(**user_dict)

    def user_create_dto_to_db(user_create: UserCreate):
        """
        Convert a UserCreate DTO to a User database model.
        :param user_create: UserCreate DTO
        :return: User database model
        """
        return User(
            first_name=user_create.first_name,
            last_name=user_create.last_name,
            email=user_create.email,
            phone_number=user_create.phone_number,
            gender=user_create.gender,
            status=Status.ENABLED,
        )

    def user_update_dto_to_db(user_update: UserUpdate, user: User):
        """
        Convert a UserUpdate DTO to a User database model (updating an existing user).
        :param user_update: UserUpdate DTO
        :param user: Existing User database model
        :return: Updated User database model
        """
        for key, value in user_update.model_dump(exclude_unset=True).items():
            setattr(user, key, value)
        return user

    def user_update_status_dto_to_db(user_update_status: UserUpdateStatus, user: User):
        """
        Convert a UserUpdateStatus DTO to a User database model (updating only the status).
        :param user_update_status: UserUpdateStatus DTO
        :param user: Existing User database model
        :return: Updated User database model
        """
        user.status = user_update_status.status
        return user
