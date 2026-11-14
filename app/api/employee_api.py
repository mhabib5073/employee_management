from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import EmployeeCreate, EmployeeResponse
from app.services.employee_service import (get_employee_service, 
    create_employee_service,
    get_all_employees_service,
    import_employees_service,
    search_employee_service,
    department_service
)
 
router = APIRouter(
    prefix="/employee",
    tags=["Employee"]
)

@router.post("/import")
def import_employees(db: Session=Depends(get_db)):
    try: 
        employees = import_employees_service(db)
        return {
            "message": "Employees imported Successfully",
            "total_inserted": len(employees)
        }
    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc)
        )

@router.post("/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session=Depends(get_db)):
    try:
        return create_employee_service(db, employee)
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc)
        )

@router.get("/all", response_model=list[EmployeeResponse])
def employees(db: Session=Depends(get_db)):
    return get_all_employees_service(db)

@router.get("/{emp_id:int}", response_model=EmployeeResponse)
def get_employee(emp_id: int, db: Session=Depends(get_db)):
    return get_employee_service(db, emp_id)

@router.get("/email/{email}", response_model=EmployeeResponse)
def get_employee_by_email(email: str, db: Session=Depends(get_db)):
    try:
        return search_employee_service(db, email)
    except Exception as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc)
        )

@router.get("/departments")
def list_employees_department(db: Session=Depends(get_db)):
    try:
        return department_service(db)
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc)
        )