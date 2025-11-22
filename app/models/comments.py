from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class CommentsModel(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    content = Column(String(1000))
    
rents = relationship("RentsModel", back_populates="comments")
users = relationship("UserModel", back_populates="comments")