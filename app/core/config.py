import os
from dotenv import load_dotenv
from pydantic import BaseModel, PostgresDsn

load_dotenv()  # Carga las variables de entorno desde un archivo .env


class Settings(BaseModel):
    """
    Configurations for the Invoicing Microservice application.

    This class uses Pydantic to define and validate the configurations required for the application.
    The configurations are loaded primarily from environment variables, with default values
    provided for some parameters.

    Attributes:
        ENVIRONMENT (str): Environment in which the application runs (e.g., 'development', 'production').
        PROJECT_NAME (str): Project or application name.
        DATABASE_URL (PostgresDsn): Connection URL to the PostgreSQL database.
        LOG_LEVEL (str): Log level for the application log output.
        IMAGES_DIRECTORY (str): Directory for storing loaded images.
    """

    # Project
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    PROJECT_NAME: str = os.getenv("APP_NAME", "Invoicing Microservice")

    # DataBase
    DATABASE_URL: PostgresDsn = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/invoicedb")

    # General
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")
    IMAGES_DIRECTORY: str = os.getenv("IMAGES_DIRECTORY", "app/images/")


# Instancia de la configuración
settings = Settings()

