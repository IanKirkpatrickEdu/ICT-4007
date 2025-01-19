from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .core import router as core_router
from .week1 import router as week1_router
from .week2 import router as week2_router

# global route collection
api_router = APIRouter(default_response_class=JSONResponse)
api_router.include_router(core_router, prefix="", tags=[])
api_router.include_router(week1_router, prefix="/week1", tags=["Week 1"])
api_router.include_router(week2_router, prefix="/week2", tags=["Week 2"])
