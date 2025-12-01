from fastapi import APIRouter

from app.v1.common.health_router import router as health
from app.v1.webhooks.new_routers import router as webhook

router = APIRouter()
router.include_router(health, prefix="/health", tags=["health"])
router.include_router(webhook, prefix="/webhook", tags=["supabase"])
