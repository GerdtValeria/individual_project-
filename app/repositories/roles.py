from sqlalchemy import select
from typing import List, Optional
from app.models.roles import RoleModel
from app.repositories.base import BaseRepository

class RolesRepository(BaseRepository[RoleModel]):
    def __init__(self, session):
        super().__init__(session, RoleModel)

    async def get_all(self) -> List[RoleModel]:
        return await super().get_all()

    async def get_by_name(self, name: str) -> Optional[RoleModel]:
        result = await self.session.execute(
            select(RoleModel).where(RoleModel.name == name)
        )
        return result.scalar_one_or_none()