from sqlalchemy import select, desc
from typing import List, Optional
from app.models.comments import CommentsModel
from app.repositories.base import BaseRepository

class CommentsRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, CommentsModel)

    async def get_all(self) -> List[CommentsModel]:
        return await super().get_all()

    async def get_by_user_id(self, user_id: int) -> List[CommentsModel]:
        result = await self.session.execute(
            select(CommentsModel).where(CommentsModel.id_user == user_id)
        )
        return result.scalars().all()

    async def get_by_rent_id(self, rent_id: int) -> List[CommentsModel]:
        result = await self.session.execute(
            select(CommentsModel).where(CommentsModel.id_rent == rent_id)
        )
        return result.scalars().all()

    async def get_recent_comments(self, limit: int = 10) -> List[CommentsModel]:
        result = await self.session.execute(
            select(CommentsModel).order_by(desc(CommentsModel.id)).limit(limit)
        )
        return result.scalars().all()