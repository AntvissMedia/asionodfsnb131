from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.settings import get_settings
from app.v1 import router as v1

settings = get_settings()

app = FastAPI(
    title=settings.project_name,
    debug=settings.app_debug,
    openapi_url=f"{settings.api_v1_prefix}/openapi.json",
)

origins = (
    [str(o) for o in settings.backend_cors_origins]
    if settings.backend_cors_origins
    else ["*"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(v1, prefix=settings.api_v1_prefix)
