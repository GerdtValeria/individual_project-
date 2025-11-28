from sqlalchemy import select, and_, or_
from typing import Optional, List
from app.models.users import User
from app.repositories.base import BaseRepository

class UsersRepository(BaseRepository[User]):
    def __init__(self, session):
        super().__init__(session, User)

    async def get_by_email(self, email: str) -> Optional[User]:
        result = await self.session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def get_by_username(self, username: str) -> Optional[User]:
        result = await self.session.execute(
            select(User).where(User.username == username)
        )
        return result.scalar_one_or_none()

    async def get_active_users(self) -> List[User]:
        result = await self.session.execute(
            select(User).where(User.is_active == True)
        )
        return result.scalars().all()

    async def get_users_by_role(self, role_id: int) -> List[User]:
        result = await self.session.execute(
            select(User).where(User.role_id == role_id)
        )
        return result.scalars().all()