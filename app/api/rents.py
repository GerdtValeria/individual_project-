from fastapi import APIRouter
from app.schemas.rents import SRentAdd
from app.services.rents import RentService

router = APIRouter(prefix="/rents",tags=["Rent"])

@router.get("/")
async def get_rents():
 rents = await RentService().get_all_rents()   
 return rents

@router.get("/{id}")
async def get_rent(id:int):
    rent = await RentService().get_all_rents(id=id)   
    return rent

@router.post("/")
async def add_rent(rent_data: SRentAdd):
    await RentService().add_rent(rent_data)

@router.put("/{id}")
async def edit_rent(id:int, rent_data: SRentAdd):
    data_comment = await RentService().edit_rent(id,rent_data)
    return data_comment

@router.delete("/{id}")
async def delete_rent(id:int):
     await RentService().delete_rent(id=id)   
