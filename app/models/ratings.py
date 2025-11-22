from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class RatingsModel(Base):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True)
    estimation = Column(Integer)
    
rents = relationship("RentsModel", back_populates="ratings")
