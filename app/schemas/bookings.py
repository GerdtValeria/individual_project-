from datetime import date
from pydantic import BaseModel, ConfigDict


class SBookingsAddRequest(BaseModel):
    id_rent: int
    date_from: date
    date_to: date


class SBookingsAdd(SBookingsAddRequest):
    user_id: int
    price: int


class SBookingGet(SBookingsAdd):
    id: int
    total_cost: int
    model_config = ConfigDict(from_attributes=True)


class SBookingsPatchRequest(BaseModel):
    room_id: int | None = None
    date_from: date | None = None
    date_to: date | None = None


class SBookingPatch(SBookingsPatchRequest):
    user_id: int | None = None
    price: int | None = None