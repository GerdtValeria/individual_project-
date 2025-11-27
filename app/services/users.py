from app.services.base import BaseService
from app.repositories.users import UsersRepository


class UserService(BaseService):
    async def get_all_users(self):
        return await UsersRepository.get_all()