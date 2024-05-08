"""Module for defining base configurations."""

from toolkit.parsers import TOMLParser

from .database.base import DatabaseConnection
from .logging.base import LoggingConfig

# Database
db = DatabaseConnection()

# Logging
log = LoggingConfig()
