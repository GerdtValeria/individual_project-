from app.services.base import BaseService
from app.repositories.images import ImagesRepository


class ImageService(BaseService):
    async def get_all_images(self):
        return await ImagesRepository.get_all()
    
    async def add_image(self):
        return await ImagesRepository.add_image()
    
    async def edit_image(self):
        return await ImagesRepository.edit_image()
    
    async def delete_image(self):
        return await ImagesRepository.delete_image()