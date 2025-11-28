from sqlalchemy import select, and_
from typing import Optional, List
from app.models.users import UserModel
from app.repositories.base import BaseRepository

class UsersRepository(BaseRepository[UserModel]):
    def __init__(self, session):
        super().__init__(session, UserModel)

    async def get_all(self) -> List[UserModel]:
        return await super().get_all()

    async def get_by_email(self, email: str) -> Optional[UserModel]:
        result = await self.session.execute(
            select(UserModel).where(UserModel.email == email)
        )
        return result.scalar_one_or_none()

    async def get_by_role(self, role_id: int) -> List[UserModel]:
        result = await self.session.execute(
            select(UserModel).where(UserModel.role_id == role_id)
        )
        return result.scalars().all()
