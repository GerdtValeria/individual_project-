from sqlalchemy import select
from typing import List, Optional
from app.models.images import Image
from app.repositories.base import BaseRepository

class ImagesRepository(BaseRepository[Image]):
    def __init__(self, session):
        super().__init__(session, Image)

    async def get_images_by_rent(self, rent_id: int) -> List[Image]:
        result = await self.session.execute(
            select(Image).where(Image.rent_id == rent_id)
        )
        return result.scalars().all()

    async def get_primary_images(self) -> List[Image]:
        result = await self.session.execute(
            select(Image).where(Image.is_primary == True)
        )
        return result.scalars().all()