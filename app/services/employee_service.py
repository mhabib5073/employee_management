import json
from pathlib import Path

from sqlalchemy.orm import Session
from app.repositories.employee_repo import (create_employee, 
    get_all_employees, 
    get_employee_by_id,bulk_create_employee,
    search_employee,
    get_employee_by_department

    
    )
from app.schemas import EmployeeCreate

def import_employees_service(db: Session):
    file_path = (Path(__file__).resolve().parents[1]/"emp.json")
    with open(file_path, "r",encoding="utf-8") as file:
        employees = json.load(file)
    if not isinstance(employees, list):
        raise ValueError("JSON file must contain a list of employees")
    return bulk_create_employee(db, employees)

def create_employee_service(db: Session, employee: EmployeeCreate):
    return create_employee(db, employee)

def get_all_employees_service(db: Session):
    return get_all_employees(db)

def get_employee_service(db: Session, emp_id: int):
    employee = get_employee_by_id(db, emp_id)
    if not employee:
        raise ValueError("Employee not found")
    return employee

def search_employee_service(db: Session, email: str):
    emp_obj = search_employee(db, email)
    if not emp_obj:
        raise ValueError("Employee not found")
    return emp_obj

def department_service(db: Session):
    emp_obj = get_employee_by_department(db)
    if not emp_obj:
        raise ValueError("Employee not Found")
    department_data = {}
    for emp in emp_obj:
        department = emp.department
        if department not in department_data:
            department_data[department]= []
        department_data[department].append({
            "id": emp.id,
            "name": emp.name,
            "email": emp.email,
            "salary": emp.salary
        })
    return department_data
