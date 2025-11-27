from pydantic import BaseModel, Field


class SComment(BaseModel):
    id:int
    id_user: int = Field(..., ge=1)
    id_rent: int = Field(..., ge=1)
    content: str = Field(...)

class SCommentAdd(BaseModel):
    id:int
    content: str = Field(...)
