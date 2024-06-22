"""
Module serves the FastAPI instance for the backend application.

It initializes the FastAPI application, configures middleware, setting lifespan context
manager, and defines routes for handling various HTTP requests.
"""

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from config.base import log
from config.settings import settings
from config.settings.openapi import responses
from toolkit.api.exceptions import (
    BaseTokenError,
    CustomHTTPException,
    DoesNotExistError,
)

from .exception_handlers import (
    base_token_error_handler,
    custom_http_exception_handler,
    does_not_exist_exception_handler,
    request_validation_exception_handler,
)
from .lifespan import lifespan

# Setup logging
log.setup()


# Setup FastAPI instance
app = FastAPI(
    title=settings.openapi.title,
    version=settings.openapi.version,
    description=settings.openapi.description,
    contact=settings.openapi.contact.model_dump(),
    license_info=settings.openapi.license.model_dump(),
    openapi_tags=[tag.model_dump() for tag in settings.openapi.tags],
    responses=responses,
    redoc_url=None,
    lifespan=lifespan,
)

# Register routers
# app.include_router(admin_v1_participant_router)  # Add your routers.

# Register custom exception handlers
app.add_exception_handler(
    CustomHTTPException,
    custom_http_exception_handler,  # type: ignore
)
app.add_exception_handler(
    RequestValidationError,
    request_validation_exception_handler,  # type: ignore
)
app.add_exception_handler(
    DoesNotExistError,
    does_not_exist_exception_handler,  # type: ignore
)
app.add_exception_handler(
    BaseTokenError,
    base_token_error_handler,  # type: ignore
)

# Register middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
