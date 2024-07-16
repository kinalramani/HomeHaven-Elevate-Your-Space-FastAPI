from sqlalchemy import Column,String,Boolean,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base
import uuid
from datetime import datetime




class DeliveryBoy(Base):
    __tablename__ = "deliveryboy"
    
    id = Column(String(100), primary_key=True, default=str(uuid.uuid4()))
    order_id=Column(String(100),ForeignKey('order.id'),nullable=False)
    user_name=Column(String(100),nullable=False)
    address=Column(String(200),nullable=False)
    payment=Column(String(100))
    status=Column(String(200),nullable=False )
    is_deleted = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
   