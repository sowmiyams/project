
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine
from models import Employee

router = APIRouter(
    prefix='/employee',
    tags=['employee']
)

models.Base.metadata.create_all(bind=engine)


class EmployeeCreate(BaseModel):
    staff_name: str
    date_of_entry: str
    age: int
    date_of_birth: str
    phone_number: str
    address: str
    gender: str



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/employees')
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = Employee(
        staff_name=employee.staff_name,
        date_of_entry=employee.date_of_entry,
        age=employee.age,
        date_of_birth=employee.date_of_birth,
        phone_number=employee.phone_number,
        address=employee.address,
        gender=employee.gender
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

# Get all employees
@router.get('/employees')
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return employees

# Update an employee
@router.put('/employees/{staff_id}')
def update_employee(staff_id: int, employee: EmployeeCreate, db: Session = Depends(get_db)):
    existing_employee = db.query(Employee).filter(Employee.staff_id == staff_id).first()

    if not existing_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    existing_employee.staff_name = employee.staff_name
    existing_employee.date_of_entry = employee.date_of_entry
    existing_employee.age = employee.age
    existing_employee.date_of_birth = employee.date_of_birth
    existing_employee.phone_number = employee.phone_number
    existing_employee.address = employee.address
    existing_employee.gender = employee.gender

    db.commit()
    db.refresh(existing_employee)

    return existing_employee

# Delete an employee
@router.delete('/employees/{staff_id}')
def delete_employee(staff_id: int, db: Session = Depends(get_db)):
    existing_employee = db.query(Employee).filter(Employee.staff_id == staff_id).first()

    if not existing_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(existing_employee)
    db.commit()

    return {'message': 'Employee deleted successfully'}
