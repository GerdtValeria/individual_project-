from sqlalchemy import select
from typing import List, Optional
from app.models.categories import Category
from app.repositories.base import BaseRepository

class CategoriesRepository(BaseRepository[Category]):
    def __init__(self, session):
        super().__init__(session, Category)

    async def get_by_name(self, name: str) -> Optional[Category]:
        result = await self.session.execute(
            select(Category).where(Category.name == name)
        )
        return result.scalar_one_or_none()

    async def get_categories_with_items(self) -> List[Category]:
        # Пример с join, если у вас есть связь с items/rents
        result = await self.session.execute(
            select(Category)  # Добавьте joins при необходимости
        )
        return result.scalars().all()