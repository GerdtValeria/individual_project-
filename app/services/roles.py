from app.services.base import BaseService
from app.repositories.roles import RolesRepository


class RoleService(BaseService):
    async def get_all_roles(self):
        return await RolesRepository.get_all()
