from app.exceptions.base import MyAppException, MyAppHTTPException


class RealtyNotAvailableException(MyAppException):
    detail = "Номер недоступен для бронирования"


class RealtyNotAvailableHTTPException(MyAppHTTPException):
    status_code = 409
    detail = "Номер недоступен для бронирования"

class BookingNotFoundException(Exception):
    detail = "Бронирование не найдено"
    def __init__(self, booking_id: int):
        super().__init__(f"Booking with id {booking_id} not found")