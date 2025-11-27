from app.services.base import BaseService
from app.repositories.rents import RentsRepository


class RentService(BaseService):
    async def get_all_rents(self):
        return await RentsRepository.get_all()