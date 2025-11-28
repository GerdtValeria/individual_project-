from fastapi import APIRouter
from app.schemas.bookings import SBookingAdd
from app.services.bookings import BookingService

router = APIRouter(prefix="/sample",tags=["Sample"])

@router.get("/", summary="Просмотр всех бронирований")
async def get_bookings():
    bookings = await BookingService().get_all_bookings()   
    return bookings

@router.get("/me", summary="Просмотр бронирований текущего пользователя")
async def get_booking(id:int):
    booking = await BookingService().get_all_bookings(id=id)   
    return booking

@router.post("/", summary="Бронирование недвижимости")
async def add_booking(booking_data: SBookingAdd):
    await BookingService().add_booking(booking_data)
