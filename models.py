from database import Base
from sqlalchemy import Column, Integer, String, Date


class Employee(Base):
    __tablename__ = 'employees'

    staff_id = Column(Integer, primary_key=True, index=True)
    date_of_entry = Column(String)
    age = Column(Integer)
    staff_name = Column(String)
    date_of_birth = Column(String)
    phone_number = Column(String)
    address = Column(String)
    gender = Column(String)
