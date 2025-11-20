from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_NAME: str
    JWT_ALGORITHM: str
    JWT_SECRET_KEY: str
    
    @property
    def db_url(self):
        return f"aiosqlite//{self.DB_NAME}"

    @property
    def auth_data(self):
        return {"algorithm": {self.JWT_ALGORITHM}, "secret_key": {self.JWT_SECRET_KEY}}

settings = Settings()

def get_db_url():
    return (
        f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@"
        f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    )

    
def get_auth_data():
    return {"secret_key": settings.SECRET_KEY, "algorithm": settings.ALGORITHM}