from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, Field


class SRent(BaseModel):
    id: int
    id_category: int 
    id_image: int
    id_user: int
    title: str = Field(...)
    price: int = Field(...)
    description: str = Field(..., min_length=10, max_length=65535)
    active: bool | None = None
    
class SRentAdd(BaseModel):
    id: int
    id_category: int 
    id_image: int
    id_user: int
    title: str = Field(...)
    price: int = Field(...)
    description: str = Field(..., min_length=10, max_length=65535)