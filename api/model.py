from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text
from database import Base

class Task(Base):
    tablename = "pets"	
    Name = Column(String(20))		
    Owner = Column(Text())