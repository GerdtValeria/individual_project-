from sqlalchemy import select, and_
from typing import List, Optional
from datetime import datetime
from app.models.rents import Rent
from app.repositories.base import BaseRepository

class RentsRepository(BaseRepository[Rent]):
    def __init__(self, session):
        super().__init__(session, Rent)

    async def get_user_rents(self, user_id: int) -> List[Rent]:
        result = await self.session.execute(
            select(Rent).where(Rent.user_id == user_id)
        )
        return result.scalars().all()

    async def get_active_rents(self) -> List[Rent]:
        result = await self.session.execute(
            select(Rent).where(Rent.status == "active")
        )
        return result.scalars().all()

    async def get_rents_by_status(self, status: str) -> List[Rent]:
        result = await self.session.execute(
            select(Rent).where(Rent.status == status)
        )
        return result.scalars().all()

    async def get_overdue_rents(self) -> List[Rent]:
        result = await self.session.execute(
            select(Rent).where(
                and_(
                    Rent.status == "active",
                    Rent.end_date < datetime.now()
                )
            )
        )
        return result.scalars().all()