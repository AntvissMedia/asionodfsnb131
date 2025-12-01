from functools import lru_cache

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    app_env: str = "local"
    app_debug: bool = True
    app_secret_key: str

    project_name: str = "NexTicket API"
    api_v1_prefix: str = "/v1"

    backend_cors_origins: list[str] = []  # strict, validator handles string->list

    jwt_algorithm: str = "HS256"

    rate_limit_requests_per_minute: int = 120

    cookie_secure: bool = False
    cookie_samesite: str = "lax"

    # FRONTEND
    frontend_url: str = Field(default="http://localhost:5173")

    @field_validator("backend_cors_origins", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: str | list[str] | None) -> list[str]:
        if v is None:
            return []
        if isinstance(v, list):
            return [str(i).strip() for i in v]
        if isinstance(v, str):
            v = v.strip()
            if not v:
                return []
            return [x.strip() for x in v.split(",")]
        return []


@lru_cache
def get_settings() -> Settings:
    settings: Settings = Settings()  # pyright: ignore[reportCallIssue]
    return settings
