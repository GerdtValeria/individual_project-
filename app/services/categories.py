from app.services.base import BaseService
from app.repositories.categories import CategoriesRepository


class CategoryService(BaseService):
    async def get_all_categories(self):
        return await CategoriesRepository.get_all()
    
    async def add_category(self):
        return await CategoriesRepository.add_category()
    
    async def edit_category(self):
        return await CategoriesRepository.edit_category()
    
    async def delete_category(self):
        return await CategoriesRepository.delete_category()