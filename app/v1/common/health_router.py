from fastapi import APIRouter

router = APIRouter()


@router.get("/status", tags=["health"])
def status() -> dict[str, str]:
    return {"status": "ok"}
