from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base
class PurchaseModel(Base):
 __tablename__ = 'purchases'

 id = Column(Integer, primary_key=True)
 id_user = Column(Integer, ForeignKey('users.id'))
 id_items = Column(Integer, ForeignKey('items.id'))
 quantity = Column(Integer) 
 cost = Column(Integer) 

 user = relationship("UserModel", back_populates="purchases")
 item = relationship("ItemModel", back_populates="purchases")
