from pydantic import BaseSettings


class APISettings(BaseSettings):
    HOST: str = '0.0.0.0'
    PORT: int = 8080
    DEBUG: bool = True
    RELOAD: bool = True


api = APISettings()
