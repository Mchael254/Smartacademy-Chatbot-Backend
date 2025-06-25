import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

BASE_DIR = Path(__file__).resolve().parent.parent
USE_ENV_FILE = os.getenv("USE_ENV_FILE", "true").lower() == "true"

class Settings(BaseSettings):
    SUPABASE_URL: str
    SUPABASE_KEY: str
    MODEL_API_URL: Optional[str] = None

    APP_PORT: int = 8000
    APP_HOST: str = "0.0.0.0"

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env") if USE_ENV_FILE else None, case_sensitive=False
    )

    @property
    def supabase_headers(self):
        return {
            "apikey": self.SUPABASE_KEY,
            "Authorization": f"Bearer {self.SUPABASE_KEY}",
        }


settings = Settings()
