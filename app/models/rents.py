from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base

class RentsModel(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    price = Column(Integer)
    time = Column(Integer)
