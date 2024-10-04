"""Module for defining base configurations."""

from .database import DatabaseConnection
from .logging import LoggingConfig

# Database
db = DatabaseConnection()

# Logging
log = LoggingConfig()
