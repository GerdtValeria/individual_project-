from app.models.bookings import BookingsModel
from app.models.categories import CategoriesModel
from app.models.comments import CommentsModel
from app.models.rents import RentsModel
from app.models.users import UserModel
from app.models.images import ImagesModel
from app.models.roles import RoleModel
from app.repositories.mapper.base import DataMapper
from app.schemas.bookings import SBookingGet
from app.schemas.categories import SCategories
from app.schemas.comments import SComment
from app.schemas.rents import SRent
from app.schemas.users import SUser, SUserWithHashedPassword
from app.schemas.images import SImages
from app.schemas.roles import SRoles

class CommentsDataMapper(DataMapper):
    db_model = CommentsModel
    schema = SComment


class RentsDataMapper(DataMapper):
    db_model = RentsModel
    schema = SRent


class UserDataMapper(DataMapper):
    db_model = UserModel
    schema = SUser


class UserDataWithHashedPassword(DataMapper):
    db_model = UserModel
    schema = SUserWithHashedPassword


class BookingDataMapper(DataMapper):
    db_model = BookingsModel
    schema = SBookingGet


class CategoriesDataMapper(DataMapper):
    db_model = CategoriesModel
    schema = SCategories


class ImagesDataMapper(DataMapper):
    db_model = ImagesModel
    schema = SImages

class RolesDataMapper(DataMapper):
    db_model = RoleModel
    schema = SRoles