"""Module for setting lifespan context manager for FastAPI application."""

import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from config.base import db
from toolkit.database.orm import Base

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Set lifespan context manager for FastAPI application."""
    engine = db.get_engine()
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables have been created successfully!")
    yield
    logger.info("Disposing database engine...")
    engine.dispose()
