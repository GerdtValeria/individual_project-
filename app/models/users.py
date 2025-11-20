from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    role_id = Column(Integer, ForeignKey('roles.id'))

role = relationship("RoleModel", back_populates="users")
purchases = relationship("PurchaseModel", back_populates="user")