from sqlalchemy import select
from typing import Optional
from app.models.roles import Role
from app.repositories.base import BaseRepository

class RolesRepository(BaseRepository[Role]):
    def __init__(self, session):
        super().__init__(session, Role)

    async def get_by_name(self, name: str) -> Optional[Role]:
        result = await self.session.execute(
            select(Role).where(Role.name == name)
        )
        return result.scalar_one_or_none()