from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
     SECRET_KEY: str
     ALGORITHM: str
     model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )  

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