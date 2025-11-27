from app.services.base import BaseService
from app.repositories.images import ImagesRepository


class ImageService(BaseService):
    async def get_all_images(self):
        return await ImagesRepository.get_all()