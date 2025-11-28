from typing import Optional, List
from sqlalchemy import select
from app.models.users import UserModel
from app.repositories.base import BaseRepository

class UserRepository(BaseRepository[UserModel]):
    def __init__(self, session):
        super().__init__(session, UserModel)

    async def get_by_email(self, email: str) -> Optional[UserModel]:
        result = await self.session.execute(
            select(UserModel).where(UserModel.email == email)
        )
        return result.scalar_one_or_none()

    async def get_active_users(self) -> List[UserModel]:
        result = await self.session.execute(
            select(UserModel).where(UserModel.is_active == True)
        )
        return result.scalars().all()