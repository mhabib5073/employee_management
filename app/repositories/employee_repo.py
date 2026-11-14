from sqlalchemy.orm import Session
from app.models import Employee
from app.schemas import EmployeeCreate, EmployeeResponse, EmployeeUpdate

def create_employee(db: Session, employee: EmployeeCreate):
    new_employee = Employee(**employee.model_dump())

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee

def bulk_create_employee(db: Session, employees: list[dict]):
    try:
        employee_obj = [
            Employee(**employee) for employee in employees
        ]
        db.add_all(employee_obj)
        db.commit()

        return employee_obj
    except Exception:
        db.rollback()
        raise

def get_all_employees(db: Session):
    emp = db.query(Employee).all()
    return emp
def get_employee_by_id(db: Session, emp_id: int):
    employee = db.query(Employee).filter(Employee.id== emp_id).first()
    return employee

def search_employee(db:Session, email: str):
    employee = db.query(Employee).filter(Employee.email==email).first()
    return employee

def get_employee_by_department(db: Session):
    return ( 
        db.query(Employee)
        .order_by(Employee.department).all()
        )
    