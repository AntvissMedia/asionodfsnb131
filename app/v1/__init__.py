from fastapi import APIRouter

from app.v1.common.health_router import router as health

router = APIRouter()
router.include_router(health, prefix="/health", tags=["health"])
