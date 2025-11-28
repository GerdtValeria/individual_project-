from sqlalchemy import select, and_, or_
from typing import List, Optional
from datetime import datetime, date
from app.models.bookings import BookingsModel
from app.repositories.base import BaseRepository

class BookingsRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, BookingsModel)

    async def get_user_bookings(self, user_id: int) -> List[BookingsModel]:
        result = await self.session.execute(
            select(BookingsModel).where(BookingsModel.id_user == user_id)
        )
        return result.scalars().all()

    async def get_active_bookings(self) -> List[BookingsModel]:
        result = await self.session.execute(
            select(BookingsModel).where(BookingsModel.status == "active")
        )
        return result.scalars().all()

    async def get_bookings_by_date_range(self, date_start: date, date_end: date) -> List[BookingsModel]:
        result = await self.session.execute(
            select(BookingsModel).where(
                and_(
                    BookingsModel.booking_date >= date_start,
                    BookingsModel.booking_date <= date_end
                )
            )
        )
        return result.scalars().all()

    async def get_overdue_bookings(self) -> List[BookingsModel]:
        result = await self.session.execute(
            select(BookingsModel).where(
                and_(
                    BookingsModel.status == "active",
                    BookingsModel.end_date < datetime.now().date()
                )
            )
        )
        return result.scalars().all()