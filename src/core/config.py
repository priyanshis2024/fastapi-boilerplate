"""This module include external settings or configurations,
for example secret keys, database credentials"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """class for reading configurations from env file"""

    DATABASE_HOST: str = "hostname"
    DATABASE_PORT: int = 1234
    DATABASE_PASSWORD: str = "Paasword1234 "
    DATABASE_NAME: str = "name"
    DATABASE_USERNAME: str = "username"

    class Config:
        """
        settings for Settings configurations
        this class is to setup environment variables locally
        """

        env_file = ".env"
        extra = "allow"


settings = Settings()
