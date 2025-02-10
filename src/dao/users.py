from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.dao.models.user import User
from src.dto.user import UserCreate, UserUpdate
from uuid import UUID
from src.utils.constants import Status
from typing import Optional
from sqlalchemy import or_
from src.dao.models.user import User

# For synchronous manner
# from sqlalchemy.orm import Session


async def get_user(db: AsyncSession, user_id: UUID):
    """
    This function gets a user details from the database by using their user id.
    :param user_id: id of the user.
    :param db: AsyncSession: Pass the database asynchronous session object to the function
    """
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()

# def get_user(db:Session, user_id: UUID):
#     """
#     Synchronous code execution function which gets a user details from the database by using their user id.
#     :param user_id: id of the user.
#     :param db: AsyncSession: Pass the database asynchronous session object to the function
#     """
#     result = db.query(User).filter(User.id == user_id)
#     return result.first()

async def create_user(db: AsyncSession, user: UserCreate):
    """
    This function creates a user in the database.

    :param user: User creation request payload schema.
    :param db: database object
    """
    db_user = User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

# def create_user(db: Session, user: UserCreate):
#     """
#     Synchronous code execution function which creates a user in the database.
#     :param user: User creation request payload schema.
#     :param db: database object
#     """
#     db_user = User(**user.dict())
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

async def update_user(db: AsyncSession, user_id: UUID, user: UserUpdate):
    """
    This function update a user details in the database.

    :param user: User update request payload schema.
    :param user_id: Id of the user to be updated .
    :param db: database object
    """
    db_user = await get_user(db, user_id)
    if db_user:
        for key, value in user.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        await db.commit()
        await db.refresh(db_user)
    return db_user

# def update_user(db: Session, user_id: UUID, user: UserUpdate):
#     """
#     Synchronous code execution function which update a user details in the database.

#     :param user: User update request payload schema.
#     :param user_id: Id of the user to be updated .
#     :param db: database object
#     """
#     db_user = db.query(User).filter(User.id == user_id).first()
#     if db_user:
#         for key, value in user.dict(exclude_unset=True).items():
#             setattr(db_user, key, value)
#         db.commit()
#         db.refresh(db_user)
#     return db_user

async def delete_user(db: AsyncSession, user_id: UUID):
    """
    This function deletes the user details from the database.
    :param user_id: Id of the user to be deleted.
    :param db: database object

    """
    db_user = await get_user(db, user_id)
    if db_user:
        await db.delete(db_user)
        await db.commit()
    return db_user

# def delete_user(db: Session, user_id: UUID):
#     """
#     Synchronous code execution function which deletes the user details from the database.
#     :param user_id: Id of the user to be deleted.
#     :param db: database object

#     """
#     db_user = get_user(db, user_id)
#     if db_user:
#         db.delete(db_user)
#         db.commit()
#         return db_user
#     return None

async def all_user(
    db: AsyncSession,
    search: Optional[str] = None,
    sort_by: Optional[str] = "created_at",
    sort_order: Optional[str] = "asc",
    limit: Optional[int] = 10,
    offset: Optional[int] = 0,
):
    """
    The all_user function is used to retrieve all the users in the database.
    It takes in a number of parameters that are used to filter and sort the results.
    :param search: Used to searching
    :param sort_order: Determine if the query should be sorted in ascending or descending order
    :param sort_by: Sort the results by a particular column
    :param limit: Limit the number of results returned
    :param offset: Skip the first n records
    :param db: database object

    :return: all user by applying filter and sorting
    """
    query = select(User)

    if search:
        query = query.where(
            or_(
                User.gender.ilike(f"%{search}%"),
                User.email.ilike(f"%{search}%"),
                User.first_name.ilike(f"%{search}%"),
                User.last_name.ilike(f"%{search}%"),
                User.phone_number.ilike(f"%{search}%"),
                User.status.ilike(f"%{search}%"),
            )
        )

    if sort_by:
        if sort_order == "asc":
            query = query.order_by(getattr(User, sort_by).asc())
        elif sort_order == "desc":
            query = query.order_by(getattr(User, sort_by).desc())

    query = query.limit(limit).offset(offset)
    result = await db.execute(query)
    return result.scalars().all()

# def all_user(
#     db: Session,
#     search: Optional[str] = None,
#     sort_by: Optional[str] = "created_at",
#     sort_order: Optional[str] = "asc",
#     limit: Optional[int] = 10,
#     offset: Optional[int] = 0,
# ):
#     """
#     Synchronous code execution function which is used to retrieve all the users in the database.
#     It takes in a number of parameters that are used to filter and sort the results.
#     :param search: Used to searching
#     :param sort_order: Determine if the query should be sorted in ascending or descending order
#     :param sort_by: Sort the results by a particular column
#     :param limit: Limit the number of results returned
#     :param offset: Skip the first n records
#     :param db: database object

#     :return: all user by applying filter and sorting
#     """
#     # query = select(User)
#     query = db.query(User)

#     if search:
#         query = query.filter(
#             or_(
#                 User.gender.ilike(f"%{search}%"),
#                 User.email.ilike(f"%{search}%"),
#                 User.first_name.ilike(f"%{search}%"),
#                 User.last_name.ilike(f"%{search}%"),
#                 User.phone_number.ilike(f"%{search}%"),
#                 User.status.ilike(f"%{search}%"),
#             )
#         )

#     if sort_by:
#         if sort_order == "asc":
#             query = query.order_by(getattr(User, sort_by).asc())
#         elif sort_order == "desc":
#             query = query.order_by(getattr(User, sort_by).desc())

#     query = query.limit(limit).offset(offset)    

#     result = query.all()
#     return result

async def update_status(db: AsyncSession, user_id: UUID, new_status: Status):
    """
    The update_status function is used to update the status of user for the given user id.

    :param user_id: Get the user details by id
    :param new_status: Updated new user status
    :param db: database object

    """
    db_user = await get_user(db, user_id)
    if db_user:
        db_user.status = new_status
        await db.commit()
        await db.refresh(db_user)
        return db_user
    return None

# def update_status(db: Session, user_id: UUID, new_status: Status):
#     """
#     Synchronous code execution function which is used to update the status of user for the given user id.

#     :param user_id: Get the user details by id
#     :param new_status: Updated new user status
#     :param db: database object

#     """
#     db_user = get_user(db, user_id)
#     if db_user:
#         db_user.status = new_status
#         db.commit()
#         db.refresh(db_user)
#         return db_user
#     return None