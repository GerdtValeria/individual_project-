from app.services.base import BaseService
from app.repositories.categories import CategoriesRepository


class CategoryService(BaseService):
    async def get_all_categories(self):
        return await CategoriesRepository.get_all()