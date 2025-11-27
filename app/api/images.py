from fastapi import APIRouter
from app.schemas.images import SImagesAdd
from app.services.images import ImageService

router = APIRouter(prefix="/image",tags=["Image"])


@router.post("/")
async def add_image(image_data: SImagesAdd):
     await ImageService().add_image(image_data)

@router.put("/{id}")
async def edit_image(id:int, image_data: SImagesAdd):
     await ImageService().edit_image(id,image_data)

@router.delete("/{id}")
async def delete_image(id:int):
     await ImageService().delete_image(id=id)   
