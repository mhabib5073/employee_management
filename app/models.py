from sqlalchemy import Column, String, Integer, Float
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer,primary_key=True,index=True )
    name = Column(String(100), nullable=False)
    email = Column(String(100))
    department = Column(String(100))
    salary = Column(Float)
