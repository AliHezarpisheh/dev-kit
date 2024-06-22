"""Module for defining base configurations."""

from .database.base import DatabaseConnection
from .logging.base import LoggingConfig

# Database
db = DatabaseConnection()

# Logging
log = LoggingConfig()
