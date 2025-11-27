from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base

class ImagesModel(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    image_url = Column(String(225))
    
rents = relationship("RentsModel", back_populates="images")
