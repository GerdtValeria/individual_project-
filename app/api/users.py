from fastapi import APIRouter
from app.services.users import UserService

router = APIRouter(prefix="/users",tags=["User"])

@router.get("/")
async def get_users():
    users = await UserService().get_all_users()   
    return users

@router.get("/{id}")
async def get_user(id:int):
    user = await UserService().get_all_users(id=id)   
    return user

@router.post("/")
async def add_user(user_data: SUserAdd):
    await UserService().add_user(user_data)

@router.put("/{id}")
async def edit_user(id:int, user_data: SUserAdd):
    data_user = await UserService().edit_user(id,user_data)
    return data_user

@router.delete("/{id}")
async def delete_user(id:int):
     await UserService().delete_user(id=id)   
