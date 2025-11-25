from pydantic import BaseModel, Field


class SCatigories(BaseModel):
    id: int
    name: str = Field(..., description="Название категория")

class SCategoriesAdd(BaseModel):
    name: str = Field(..., description="Название категория")

class SCategoriesUpdDesc(BaseModel):
    name: str = Field(..., description="Название категория")