from fastapi import APIRouter
from app.schemas.categories import SCategoriesAdd
from app.services.categories import CategoryService

router = APIRouter(prefix="/categories",tags=["Category"])

@router.get("/")
async def get_categories():
 categories = await CategoryService().get_all_categories()   
 return categories

@router.get("/{id}")
async def get_category(id:int):
    category = await CategoryService().get_all_categories(id=id)   
    return category

@router.post("/")
async def add_category(category_data: SCategoriesAdd):
    await CategoryService().add_category(category_data)

@router.put("/{id}")
async def edit_category(id:int, category_data: SCategoriesAdd):
    data_comment = await CategoryService().edit_category(id,category_data)
    return data_comment

@router.delete("/{id}")
async def delete_category(id:int):
     await CategoryService().delete_category(id=id)   
