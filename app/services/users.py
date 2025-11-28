from app.services.base import BaseService
from app.repositories.users import UsersRepository


class UserService(BaseService):
    async def get_all_users(self):
        return await UsersRepository.get_all()
    
    async def add_user(self):
        return await UsersRepository.add_user()
    
    async def edit_user(self):
        return await UsersRepository.edit_user()
    
    async def delete_user(self):
        return await UsersRepository.delete_user()