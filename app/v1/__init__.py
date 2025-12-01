from common.health_router import router as health
from fastapi import APIRouter

router = APIRouter()
router.include_router(health, prefix="/health", tags=["health"])
