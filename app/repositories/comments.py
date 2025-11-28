from sqlalchemy import select, desc
from typing import List, Optional
from app.models.comments import Comment
from app.repositories.base import BaseRepository

class CommentsRepository(BaseRepository[Comment]):
    def __init__(self, session):
        super().__init__(session, Comment)

    async def get_comments_by_user(self, user_id: int) -> List[Comment]:
        result = await self.session.execute(
            select(Comment).where(Comment.user_id == user_id)
        )
        return result.scalars().all()

    async def get_comments_by_rent(self, rent_id: int) -> List[Comment]:
        result = await self.session.execute(
            select(Comment).where(Comment.rent_id == rent_id)
        )
        return result.scalars().all()

    async def get_recent_comments(self, limit: int = 10) -> List[Comment]:
        result = await self.session.execute(
            select(Comment).order_by(desc(Comment.created_at)).limit(limit)
        )
        return result.scalars().all()