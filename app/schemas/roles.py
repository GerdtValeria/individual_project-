from pydantic import BaseModel, Field


class SRoles(BaseModel):
    id: int
    name: str = Field(...)

class SRolesAdd(BaseModel):
    id: int
    name: str = Field(...)

