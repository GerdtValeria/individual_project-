from fastapi import APIRouter
from app.services.roles import RoleService

router = APIRouter(prefix="/roles",tags=["Roles"])

@router.get("/")
async def get_roles():
 roles = await RoleService().get_all_roles()   
 return roles

@router.get("/{id}")
async def get_role(id:int):
    role = await RoleService().get_all_roles(id=id)   
    return role