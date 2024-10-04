"""Module for handling all the settings in the application."""

import os
from functools import lru_cache
from typing import Literal, Type

from pydantic import AnyHttpUrl, Field
from pydantic_settings import (
    BaseSettings,
    DotEnvSettingsSource,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)

from .openapi import OpenAPISettings


class Settings(BaseSettings):
    """
    Class for handling all the settings in the application.

    Notes
    -----
    The `model_config` attribute is a `SettingsConfigDict` instance. It contains the
    following attributes:
        - toml_file: str
            The file path to the TOML settings file.
        - env_file: str
            The file path to the environments variable settings file.
    """

    # TOML Settings
    env: Literal["development", "production", "testing"]
    openapi: OpenAPISettings

    # .env Settings
    database_url: str = Field(..., description="Database connection URL.")
    origins: list[str] = Field(..., description="List of allowed API origins.")
    api_token: str = Field(..., description="Sample API token for authentication.")
    back_plane_url: AnyHttpUrl = Field(..., description="The back plane url.")
    apikey: str = Field(..., description="API key needed for permissions.")
    module: str = Field(..., description="The module name, needed for permissions.")

    # Settings config
    model_config = SettingsConfigDict(
        toml_file="settings.toml",
        env_file=f"config/environments/.env.{os.getenv('ENV', 'development')}",
        case_sensitive=False,
        extra="ignore",
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        """Customize the settings sources."""
        return (
            init_settings,  # Initial settings
            TomlConfigSettingsSource(settings_cls),  # Read from .toml file
            DotEnvSettingsSource(settings_cls),  # Read from .env file
            env_settings,  # Read from environments variables
            file_secret_settings,  # Read from any file secret settings if applicable
        )


@lru_cache
def get_settings() -> Settings:
    """Create a new Settings object."""
    return Settings()  # type: ignore
