"""This module include external settings or configurations,
for example secret keys, database credentials"""

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """class for reading configurations from env file"""

    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_USERNAME: str

    class Config:
        """
        settings for Settings configurations
        this class is to setup environment variables locally
        """

        env_file = ".env"
        extra = "allow"


settings = Settings()