from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class BookingsModel(Base):
 __tablename__ = 'bookings'
 id = Column(Integer, primary_key=True)
 id_user = Column(Integer, ForeignKey('users.id'))
 id_rents = Column(Integer, ForeignKey('rents.id'))
 time = Column(Integer) 
 cost = Column(Integer) 

 users = relationship("UserModel", back_populates="bookings")
 rents = relationship("RentsModel", back_populates="bookings")
