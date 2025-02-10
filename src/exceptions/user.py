from fastapi import HTTPException, status


class UserNotFound(HTTPException):
    """This class is for user not found exception"""

    def __init__(self, detail: str = "User not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class UserAlreadyExists(HTTPException):
    """This class is for user already exists exception"""

    def __init__(self, detail: str = "User already exist"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)


class InvalidSortingAttribute(HTTPException):
    """
    Exception raised when the provided attribute for sorting is invalid.
    """

    def __init__(self, attribute: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid attribute '{attribute}' for sorting",
        )

class InvalidStatusAttribute(HTTPException):
    """
    Exception raised when the provided attribute for status number is invalid.
    """

    def __init__(self, attribute: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid attribute '{attribute}' for status",
        )
