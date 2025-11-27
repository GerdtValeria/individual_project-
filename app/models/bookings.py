from sqlalchemy import Column, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class BookingsModel(Base):
 __tablename__ = 'bookings'
 id = Column(Integer, primary_key=True)
 id_user = Column(Integer, ForeignKey('users.id'))
 id_rents = Column(Integer, ForeignKey('rent.id'))
 date_start = Column(Date) 
 date_end = Column(Date) 
 cost = Column(Integer) 

 users = relationship("UserModel", back_populates="bookings")
 rents = relationship("RentsModel", back_populates="bookings")
