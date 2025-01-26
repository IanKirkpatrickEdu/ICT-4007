from fastapi import FastAPI
from loguru import logger

from router.server import api_router
from core.logging import init_logging
from core.settings import Settings, get_settings
from middleware.logging import LoggingMiddleware

import contextlib
from typing import AsyncGenerator

# from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

import fastapi

settings: Settings = get_settings()


@contextlib.asynccontextmanager
async def app_lifespan(_app: fastapi.FastAPI) -> AsyncGenerator:
    """Application lifespan."""
    # Startup
    await init_logging(settings)
    logger.info("Application Started")
    yield
    # Shutdown
    logger.info("Application Teardown")


def init_app() -> fastapi.FastAPI:
    """Create FastAPI application."""

    server = fastapi.FastAPI(
        title=settings.API_NAME,
        docs_url=settings.SWAGGER_URL,
        redoc_url=settings.REDOC_URL,
        lifespan=app_lifespan,
        # terms_of_service="http://example.com/terms/",
        contact={
            "name": "Ian Kirkpatrick",
            # "url": "http://ian.kirkpatrick.com",
            "email": "ian.kirkpatrick@du.edu",
        },
        license_info={
            "name": "GNU General Public License v3.0",
            "identifier": "GPL-3.0-only",
            "url": "https://www.gnu.org/licenses/gpl-3.0.html",
        }
    )

    # see ./middleware
    server.add_middleware(LoggingMiddleware)

    origins = [
        # "http://localhost:4202", # UI
        "*"
    ]

    # server.add_middleware(
    #     TrustedHostMiddleware, allowed_hosts=[origins]
    # )

    server.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # see: https://www.starlette.io/middleware/#gzipmiddleware
    server.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=9)  # default 500  # 1-9

    server.include_router(api_router)

    return server


app = init_app()