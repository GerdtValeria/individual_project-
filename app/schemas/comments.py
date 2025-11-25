from pydantic import BaseModel, Field


class SComments(BaseModel):
    id: int
    id_user: int = Field(..., ge=1, description="ID пользователя")
    content: str = Field(..., description="Содержимое комментария")

class SCommentsAdd(BaseModel):
    id_user: int = Field(..., ge=1, description="ID пользователя")
    content: str = Field(..., description="Содержимое комментария")

class SMCommentsUpdDesc(BaseModel):
    id_user: int = Field(..., ge=1, description="ID пользователя")
    content: str = Field(..., description="Содержимое комментария")