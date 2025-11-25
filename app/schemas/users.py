from pydantic import BaseModel, EmailStr, Field, field_validator
import re

class SUser(BaseModel):
    id: int
    email: EmailStr = Field(..., description="Электронная почта")
    role_id: int = Field(..., ge=1, description="ID роли пользователя")
    id_rents: int = Field(..., ge=1, description="ID объявлений пользователя")
    password: str = Field(..., min_length=5, max_length=50, description="Пароль, от 5 до 50 знаков")

class SUserRegister(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта")
    role_id: int = Field(..., ge=1, description="ID роли пользователя")
    password: str = Field(..., min_length=5, max_length=50, description="Пароль, от 5 до 50 знаков")
    name: str = Field(..., min_length=3, max_length=50, description="Имя, от 3 до 50 символов")

    
class SUserAuth(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=5, max_length=50, description="Пароль, от 5 до 50 знаков")